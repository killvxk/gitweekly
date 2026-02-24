# Firefox SpiderMonkey Wasm：一个字符的笔误，一条通往 RCE 的路

> 原文：https://kqx.io/post/firefox0day/
>
> CVE 于 2026 年 2 月披露，漏洞仅影响 Firefox 149 Nightly，从未进入正式发布版本。

## 漏洞根因

在提交 `fcc2f20e35ec` 中，`WasmGcObject.cpp` 里出现了一个经典的单字符笔误——把按位或 `|` 写成了按位与 `&`：

```cpp
// 有 bug 的写法：结果恒为 0
oolHeaderOld->word = uintptr_t(oolHeaderNew) & 1;

// 正确写法：设置 LSB 作为转发标记
oolHeaderOld->word = uintptr_t(oolHeaderNew) | 1;
```

由于指针天然是对齐的（低位为 0），`& 1` 的结果永远是 0，转发指针被直接清零。

## 背景知识：内联数组与外置数组

SpiderMonkey 的 Wasm GC 对数组有两种存储方式：

- **内联（Inline, IL）**：小数组直接跟在对象后面存储
- **外置（Out-of-Line, OOL）**：大数组通过 `BufferAllocator` 单独分配堆内存，OOL 块以一个单字的 `OOLDataHeader` 开头，后面才是实际数据

区分两者的方式是检查 header word 的最低位（LSB）：

```cpp
static inline bool isDataInline(uint8_t* data) {
  // ...
  return (headerWord & 1) == 0;  // LSB=0 表示内联
}
```

转发指针被清零后，OOL 数组会被误判为内联数组——这就是问题的核心。

## 漏洞触发路径

Bug 存在于 `WasmArrayObject::obj_moved()` 函数中。当 GC 移动一个 Wasm 数组（从 nursery 到 nursery，或从 nursery 到 tenured）时，OOL 数组的旧缓冲区 header 应该被写入一个 LSB=1 的转发指针，这样 Ion（SpiderMonkey 的 JIT 编译器）就能找到新位置。

但因为 bug，转发指针变成了 0。于是 `isDataInline()` 返回 true，接下来在 `wasm::Instance::updateFrameForMovingGC` 中：

```cpp
if (WasmArrayObject::isDataInline(oldDataPointer)) {
    WasmArrayObject* newArray = (WasmArrayObject*)gc::MaybeForwarded(oldArray);
    if (newArray != oldArray) { /* 永远不会走到这里 */ }
}
```

`MaybeForwarded` 没有看到转发标记，直接返回了旧地址。栈帧不会被更新，Ion JIT 继续引用已经被释放的内存——经典的 **Use-After-Free**。

注意：这个漏洞只在 Ion 优化后的 Wasm 函数中才能触发，Baseline 编译器不受影响。

## 利用过程

### 第一步：确认崩溃

构造一个 Wasm 模块，分配 128 元素的 `i8` 数组，每次迭代写入数据并触发 `minorgc()`，同时预热函数以触发 Ion 优化。在 debug 构建中，会在 `0x00802d2d2d28`（GC 毒化值）处产生 SEGV 崩溃。

### 第二步：任意读写

关闭额外的 GC 毒化（`--setpref extra_gc_poisoning=false`）后，通过堆喷射大量填充 `0x41414141` 的 `Uint32Array` 缓冲区来占位被释放的 OOL header。下一次 GC 时，`updateFrameForMovingGC` 会把喷射的值 `0x414141414141` 当作转发指针读取，去掉标记位后得到 `0x414141414140`，并将其视为 OOL 数组的基地址——实现**任意地址读写**。

### 第三步：绕过 ASLR

喷射 `Uint8Array(256)` 对象（其中包含相对于二进制基址的指针），让它们与 UAF 的数组重叠。通过 Wasm 线性内存读取其中的指针，减去已知偏移 `0x2c9bd8`，即可恢复 JS 引擎的基地址。

### 第四步：RCE

拿到基地址后：

1. 定位 `system` 函数、虚表 `_ZL23gCommonCleanupFunctions`，以及一个 ROP gadget：
   ```
   mov rdi, qword ptr [rdi + 0x188]; call qword ptr [rdi + 0x48]
   ```
2. 通过任意写原语覆盖虚表条目（重新触发 UAF，用新的喷射数据瞄准虚表地址）
3. 在受控内存区域写入 `/bin/sh\x00`
4. 跳转到 `call system` 指令（而非直接跳 `system`，以保持栈对齐）
5. 脚本销毁时虚表被调用，劫持 RIP，弹出 shell

作者自己也说这个利用"非常脏"，高度依赖堆喷射，需要针对具体环境做调整。

## 时间线

| 日期 | 事件 |
|------|------|
| 2026-01-19 | 引入漏洞的提交合入 |
| 2026-02-03 | 独立研究员提交 bug #2013739 |
| 2026-02-03 | 作者在 72 小时内提交报告 #2014014 |
| 2026-02-09 | 修复提交 `05ffcde` 合入 |
| 2026-02-11 | 赏金发放，两位报告者共享 |

漏洞仅存在于 Firefox 149 Nightly 中，从未影响正式发布版本。修复方式也极其简单——把 `& 1` 改回 `| 1`。

## 小结

一个 `&` 和 `|` 的差别，让 OOL 数组的转发指针归零，GC 移动后栈帧指向已释放内存，最终从 UAF 一路走到任意读写、ASLR 绕过、虚表劫持、RCE。整个利用链虽然粗糙但完整，再次说明了底层内存安全中"差之毫厘，谬以千里"的道理。
