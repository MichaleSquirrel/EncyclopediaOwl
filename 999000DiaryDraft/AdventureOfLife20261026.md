Monday October 26 Day 299 week 44 of 2026

## 1.TodoList
1. 《Kong入门与实战》学习



## 2.MCA课程学习进度

2026年10月26号学习进展：
1. 复习
2. 阅读
   大概用时：小时


## 3.

《我看见的世界：李飞飞自传》

remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/MichaleSquirrel/EncyclopediaOwl.git/'


## 4.中期服务辅导总结


### 4.1 中期服务辅导（员工）

OpenResty是一个基于Nginx与LuaJIT的高性能Web平台


> https://openresty.org/cn/



OpenResty® 是一个基于 Nginx 与 Lua 的高性能 Web 平台，其内部集成了大量精良的 Lua 库、第三方模块以及大多数的依赖项。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。

用于搭建能够处理超高并发、扩展性极高的动态Wed应用服务和动态网关。

Kong入门与实践

读者可以使用Lua脚本在Nginx请求处理的各个阶段实施拦截并执行各种Lua代码，调用Nginx支持的各种C及Lua模块来实现各种个性化的业务需求。总之，OpenResty使你不再需要用C、C++编写复杂的扩展模块，使用Lua就能够快速地构建高性能网关系统。

OpenResty汇集了众多设计精良的 组件，搭建了一个完善的高性能服务器开发环境，基于OpenResty可以轻易地开发出支持超高并发的Web应用和动态网关。


以下是两个项目设计文档讲解的总结，可直接用于中期服务辅导填写：

---

## 一、项目总体定位（姊妹系统，端到端 Agent 调用链）

**调用链**：员工 → 员工助手(中台Agent) → **Agent 网关**(A2A 协议，Agent↔Agent) → 业务Agent → **MCP 网关**(MCP 协议，Agent→工具) → MCP Server → 业务系统。两者独立部署、独立演进，通过 `X-Agent-Id` / `X-Agent-Token` / `X-End-User-Delegation-Token` 等约定头衔接身份链，共同保障多跳 Agent 调用中终端用户身份的安全、可审计传递。

## 二、Agent 网关（A2A Gateway，设计文档 V2.0.19）

- **架构**：管理面（Spring Boot 3.2 + MyBatis-Plus + MySQL 17 张表）+ 数据面（OpenResty + Lua + 每节点本地 Redis，无状态可水平扩展）+ React 前端控制台。
- **核心能力**：Agent Card 托管与路径式发现（url 重写为网关地址、ETag/304）；双协议代理（A2A JSON-RPC 透传含 SSE 流式；OPENAI_CHAT 适配层支持 RAP 等 OpenAI 风格上游，双向协议转换+合成虚拟 Task）；订阅审批流（开放订阅/审批制，状态机）；上游凭证代换（API_KEY/BEARER/BASIC/OAUTH2/MTLS，AES-256-GCM 加密存储，客户端凭证擦除）；分/时/日三窗口限流；Push 模式配置同步（sync_task 3 秒级推送、失败可重试可观测）。
- **认证安全**：AI-Auth 校验 Agent 动态 Token（身份以 Token 解析结果为准）；人员委托 Token 透传并解析 userId 记日志；管理面 IAM SSO 登录 + 三层角色同步（Manager/Owner→AGENT_MANAGER，其余→VIEWER）+ 应用级 RBAC（菜单级+按钮级）。
- **可观测**：访问日志 JSON 化 → Filebeat → ES（.keyword 子字段查询、索引模板代码化、多节点故障切换），前端日志追踪/看板；V2.0.19 新增调试预览（Debug Preview 全链路）。

## 三、MCP 网关（MCP Gateway，设计文档 V2.0.15）

- **架构**：与 Agent 网关同构（Portal 8080 + OpenResty 数据面 9080 + 本地 Redis），MCP 市场（Server/Tool/提示词/资源注册、卡片式展示、授权管理、审计查询）。
- **协议兼容**：完整支持 MCP 2025-11-25 Streamable HTTP（会话粘滞、Last-Event-ID 断线续传、202 语义），并必选兼容 2024-11-05 旧版 HTTP+SSE 双端点传输（endpoint 事件 URI 改写难点）。
- **认证模型（V2.0.14 重构）**：废弃 Token Exchange，按 `auth_mode` 四值严格区分入口认证——service（Agent Token→AI-Auth）/personal（Cookie→iDaas）/role（Cookie→iDaas+iAuth）/none；上游认证独立由 `upstream_credential` 8 种类型（含 COOKIES 委托换取、APIG）注入。
- **授权与防攻击**：Tool 级策略求值（DENY-first、default-deny、fail-closed，快照+网关本地求值），六层防线防 Confused Deputy（aud 受众绑定、act 委托链验证、参数绑定、头部 hygiene 等）；V2.0.15 完善流控（IP 维度限流反 DoS + 策略约束限流 + 全局设置）。
- **特色**：平台服务接入（选 API→生成 fastmcp Python 代码→本地进程管理→1 API:1 工具绑定）；配置 Pull 轮询同步（5s 水位+全量快照降级，V2.0.16 计划改 Push）。

## 四、个人收获

通过 owner 讲解，理解了两个网关“**声明与凭证分离、透传为主轻量校验、数据面无状态、敏感数据全链路加密、失败收敛**”等设计原则；掌握了控制面/数据面分离、本地 Redis + 配置同步（Pull vs Push 两种模式）、委托 Token 身份链传递、多租户(app)隔离与 RBAC 等通用架构模式，以及 MCP/A2A 两类协议在企业场景下的落地要点。

---

如需精简版（100 字左右）或英文版，或想突出某一部分（如安全设计/协议细节），告诉我即可。


### 4.2 中期服务辅导（员工）
服务owner不定期讲解了MCP网关与Agent网关的关键设计理念和用到的相关技术，包括:
1. OpenResty汇集了众多设计精良的组件，搭建了一个完善的高性能服务器开发环境，基于OpenResty可以轻易地开发出支持超高并发、扩展性极高的动态Wed应用服务和动态网关。
2. 使用SpringBoot、MyBatisPlus、MySQL搭建管理面，使用OpenResty、Lua 、每节点本地Redis搭建运行面，使用React、Vite搭建前端控制台。
3. 认证对接企业内部AI身份认证中心（AI-Auth），Agent调用网关时传递从AI-Auth获取的动态Token
4. 对接IAM SSO登录，应用级RBAC权限模型，IAM 用户权限同步
5. MCP支持新版协议(Version 2026-07-28)并兼容旧版(2024-11-05)
6. 使用Docker/K8s 容器化部署
   通过服务owner讲解 MCP 网关与 Agent 网关设计文档，我重点掌握了基于 OpenResty + Lua 的数据面网关设计（认证、限流、策略求值、SSE 转发）、Spring Boot 微服务管理面架构、Docker/K8s 容器化部署，以及本地 Redis、控制面/数据面分离、委托 Token 身份传递等关键设计，理解了 MCP/A2A 协议的企业级落地的流程。





