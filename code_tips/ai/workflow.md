# cline-workflow.yaml

version: 1
name: Cline 工作流：分阶段执行 + 测试门禁 + 不确定性处理
created_by: user
description: >
  在任何代码编写前，必须先产出并确认需求分析与设计文档；每个子任务在编写代码前先输出测试用例，
  编写代码后产出测试代码与测试工具配置；每个阶段结束必须运行并通过单测，若测试失败则先修复再继续。
  遇到不确定时，先查 context7 文档，仍不确定再进行网络搜索。

global_policies:
  staged_execution: true
  unit_test_gate: true
  fix_on_failure_before_continue: true
  uncertainty_handling:
    priority_sources:
      - context7
      - user_clarification
      - official_docs_and_specs
      - reputable_community_sources
      - other_blogs_or_forums
    steps:
      - identify_uncertainty
      - search_context7_first
      - if_still_uncertain_search_web
      - cross_verify_at_least_two_sources
      - if_conflict_prefer_context7_and_note_risks

discovery:
  context7_lookup:
    what_to_find:
      - 架构/设计/ADR
      - API/协议/数据结构定义
      - 运行/运维/排障手册
      - 测试框架与命令（package.json/Makefile/pom.xml/pytest.ini/go.mod 等）
      - CI/CD 规则与门禁
    outputs:
      - paths_index.md
      - testing_conventions.md
  test_command_detection:
    order_to_try:
      - npm test
      - pnpm test
      - yarn test
      - pytest
      - pytest -q
      - go test ./...
      - mvn -q -Dtest=\* test
      - gradle test
      - make test
    rule: 优先使用 context7 中明确指定的命令，若无则按顺序探测，确定后固化为 test_command。

artifacts_and_locations:
  docs:
    requirements: docs/requirements.md
    design: docs/design.md
    subtask_test_cases_template: tests/cases/{subtask-id}-cases.md
  code:
    implementation_notes: docs/impl-notes/{subtask-id}.md
  tests:
    test_code_root: tests/
    coverage_report: coverage/
  records:
    decisions: docs/adr/
    phase_reports: docs/reports/{phase-id}.md

phases:
  - id: 0-setup-and-context7-scan
    goals:
      - 扫描 context7 与项目结构，记录关键位置与测试基建
      - 识别不确定点并按不确定性处理流程执行
    outputs:
      - discovery/paths_index.md
      - discovery/testing_conventions.md
      - resolved_or_open_uncertainties.md
      - test_command.txt
    gates:
      - description: 若测试基建缺失，先最小化补齐（依赖、样例测试、CI 任务草案）
        required: true
      - description: 记录 test_command
        required: true
    tests:
      run: false  # 如需补齐样例测试，补齐后再运行

  - id: 1-requirements-analysis
    goals:
      - 在任何代码编写前，完成并输出需求分析文档
    outputs:
      - docs/requirements.md
    template:
      sections:
        - 背景与目标
        - 业务范围与不在范围
        - 术语与上下文
        - 角色与用例/用户故事
        - 功能需求与验收标准
        - 非功能需求（性能/安全/合规/可观测/国际化等）
        - 依赖与约束（版本、环境、接口契约）
        - 风险与打开问题（需在后续澄清）
    gates:
      - description: 与用户/干系人确认需求文档，无阻塞的打开问题
        required: true
    tests:
      run: false

  - id: 2-design
    goals:
      - 在任何代码编写前，完成并输出设计文档
    outputs:
      - docs/design.md
    template:
      sections:
        - 架构视图（上下文/容器/组件/部署）
        - 数据模型与接口契约（OpenAPI/Proto/Schema/DTO）
        - 关键流程与时序图
        - 错误处理与幂等/一致性策略
        - 存储/缓存/队列/第三方依赖
        - 迁移与向后兼容策略
        - 观测性（日志/指标/追踪）
        - 测试策略与覆盖范围目标
    gates:
      - description: 设计评审通过（至少覆盖关键路径与兼容性）
        required: true
    tests:
      run: false

  - id: 3-implementation-loop
    loop: true
    loop_description: 对每一个子任务按以下子阶段执行，所有阶段均需单测门禁
    subphases:
      - name: 3.1-subtask-plan
        goals:
          - 明确子任务边界、影响面与回滚策略
        outputs:
          - docs/impl-notes/{subtask-id}.md
        gates:
          - description: 子任务目标、范围、验收标准清晰
            required: true
        tests:
          run: false

      - name: 3.2-pre-code-test-cases
        goals:
          - 在编写代码前，输出该子任务的测试用例（非测试代码，是用例规格）
        outputs:
          - tests/cases/{subtask-id}-cases.md
        template:
          case_sections:
            - 标题/ID
            - 前置条件/夹具
            - 步骤
            - 期望结果（含边界与异常）
            - 覆盖到的需求/设计条目引用
        gates:
          - description: 用例覆盖关键路径、边界与异常
            required: true
        tests:
          run: false

      - name: 3.3-implement-code
        goals:
          - 按设计实现代码，小步提交
        outputs:
          - 源码改动
        gates:
          - description: 严禁跨越多个模块的一次性大改，遵循原子化提交
            required: true
        tests:
          run: false

      - name: 3.4-post-code-test-impl
        goals:
          - 在实现完成后，产出测试代码与配置/工具
        outputs:
          - tests/**/*
          - 测试工具与配置（如 pytest.ini、jest.config、Makefile、docker-compose.test.yml 等）
        actions:
          - 将 3.2 中的用例转化为可执行测试代码
          - 如需，引入/配置测试工具（mock、fixtures、testcontainers 等）
        gates:
          - description: 新增/修改代码路径应被测试覆盖（若有覆盖率阈值需达标）
            required: true
        tests:
          run: true
          command: ${test_command}  # 从 test_command.txt 读取

      - name: 3.5-test-and-fix
        goals:
          - 运行测试，若失败，则诊断与修复，直至全部通过
        strategy:
          - 重现失败 -> 定位根因 -> 最小修复 -> 追加/修正测试 -> 再次运行
          - 如涉及不确定性，遵循不确定性处理流程（先 context7 后网络）
        tests:
          run: true
          command: ${test_command}
        gates:
          - description: 测试全部通过（含 CI 如有）
            required: true

      - name: 3.6-stage-done
        goals:
          - 记录阶段结果，进入下一个子任务或收尾
        outputs:
          - docs/reports/{subtask-id}.md
        tests:
          run: false

  - id: 4-finalize
    goals:
      - 整体验收、文档与变更记录完善
    checklist:
      - 所有阶段单测通过，关键路径覆盖
      - 静态检查/安全扫描/格式化无误（遵循 context7 的规则）
      - 文档同步更新（README/变更日志/运维手册/ADR）
    outputs:
      - CHANGELOG.md（如适用）
      - docs/adr/（新增或更新）
      - 最终报告：docs/reports/final.md
    tests:
      run: true
      command: ${test_command}

controls_and_rules:
  before_any_code_changes:
    - 必须完成并通过评审：docs/requirements.md 与 docs/design.md
  before_each_coding_subtask:
    - 必须先输出测试用例规格：tests/cases/{subtask-id}-cases.md
  after_each_coding_subtask:
    - 必须产出对应测试代码与测试工具配置，然后运行单测
  on_test_failure:
    - 停止继续开发，进入诊断与修复循环，直到全部测试通过
  uncertainty_mandate:
    - 遇到不确定，先查 context7；仍不确定，再进行网络搜索并交叉验证；输出结论需附来源

recordkeeping:
  keep:
    - 不确定点列表与处理结论（含 context7 路径与外部链接）
    - 每阶段的测试结果摘要（命令、失败原因、修复点）
    - 覆盖率与关键覆盖点
    - 回滚方案与已知风险
  storage:
    - docs/reports/
    - docs/adr/
    - tests/cases/

notes:
  - 如项目缺少测试基建，应在 0 阶段最小化补齐（依赖、样例测试、CI）。
  - 对依赖外部服务的测试，优先使用 mock/fixtures/localstack/testcontainers，禁止访问生产资源。
  - 若 context7 与外部资料冲突，以 context7 为准，并在报告中注明差异与风险。
