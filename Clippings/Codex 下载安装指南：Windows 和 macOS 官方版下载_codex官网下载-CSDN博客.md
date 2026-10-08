---
title: "Codex 下载安装指南：Windows 和 macOS 官方版下载_codex官网下载-CSDN博客"
source: "https://blog.csdn.net/weixin_44733660/article/details/161521752"
author:
  - "[[whyfail]]"
published: 2026-05-29
created: 2026-10-02
description: "文章浏览阅读10w+次，点赞80次，收藏126次。本文整理 OpenAI Codex 的官方下载与安装方式，包含 Windows 版、macOS 版直接下载链接，以及官方脚本安装、npm 安装方式。建议只从 OpenAI 官方渠道下载，不要使用第三方下载站提供的所谓“完整版”“绿色版”“破解版”，避免账号、代码和本地文件安全风险。_codex官网下载"
tags:
  - "clippings"
---
本文整理 OpenAI 官方桌面应用中 Codex 工作模式的下载与安装方式，覆盖 Windows、macOS Apple Silicon 和 macOS Intel，并补充 Windows 企业/离线部署入口。

> OpenAI 当前官方文档使用的产品名称是 **ChatGPT desktop app（ChatGPT 桌面应用）** 。Codex 已集成在该桌面应用中，不再只是一个单独命名的 GUI 客户端。安装后可在应用内选择 ChatGPT 或 Codex。

建议只从 OpenAI、Microsoft 等官方渠道下载。不要使用第三方下载站提供的“完整版”“绿色版”“破解版”，避免账号、代码仓库和本地文件泄露。

### 一、先确认你要安装什么

本文主要介绍带图形界面的 **ChatGPT 桌面应用及其中的 Codex** ，不是单独的 Codex CLI 命令行工具。

桌面应用支持项目和并行任务、Git 与 worktree、内置终端和浏览器、文件预览、插件、技能、定时任务等工作流。Windows 版可以使用原生 PowerShell 和 Windows 沙箱，也可以切换到 WSL2。

官方文档：

- [ChatGPT 桌面应用 / Codex App](https://developers.openai.com/codex/app)
- [Windows 桌面应用](https://developers.openai.com/codex/app/windows)
- [快速开始](https://developers.openai.com/codex/quickstart)

### 二、官方下载入口

#### 1\. macOS Apple Silicon

适用于 M1、M2、M3、M4、M5 等 Apple 芯片 Mac。

[下载官方 DMG（Apple Silicon）](https://persistent.oaistatic.com/codex-app-prod/Codex.dmg)

安装方法：

1. 下载并打开 `Codex.dmg` 。
2. 将应用拖入“应用程序（Applications）”文件夹。
3. 从“应用程序”中打开 ChatGPT。
4. 登录后选择 Codex，或创建/打开项目目录开始使用。

#### 2\. macOS Intel

适用于 Intel 处理器 Mac。可在“苹果菜单 > 关于本机”中查看芯片或处理器类型。

[下载官方 DMG（Intel）](https://persistent.oaistatic.com/codex-app-prod/Codex-latest-x64.dmg)

安装方法与 Apple Silicon 版相同。两种 DMG 的架构不同，不要混用。

#### 3\. Windows：普通用户推荐方式

OpenAI 面向普通用户提供的是 Microsoft 签名的网页安装器：

[下载 Windows 官方网页安装器](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)

截至本文核对时间，该链接下载的文件名是 `ChatGPT Installer.exe` ，大小约 1.4 MB。它是引导安装器，不是完整离线安装包；安装或更新过程中可能会调用 Microsoft Store 相关组件，但通常不需要用户手动打开商店页面。

也可以在 PowerShell 或 Windows 终端中执行官方文档给出的命令：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
powershell1
```

其中 `9PLM9XGG6VKS` 是 ChatGPT 桌面应用的 Microsoft Store 产品 ID。

### 三、Windows 无法使用 Microsoft Store 时

#### 1\. 先尝试网页安装器

直接运行官方 [`ChatGPT Installer.exe`](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) 。用户不需要浏览 Microsoft Store，但安装和自动更新仍可能使用 Microsoft 的应用分发组件。

#### 2\. 再尝试 winget

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
powershell1
```

如果 `msstore` 源异常，可以先检查并重置来源：

```powershell
winget source list
winget source reset --force
powershell12
```

然后重新执行安装命令。

#### 3\. 官方 MSIX：企业、受管设备或离线部署

这部分是相较旧版指南最重要的变化。OpenAI 现已提供最新的 **Store 签名 MSIX** ，用于无法通过 Microsoft 应用分发服务完成初次安装的环境：

- [下载 Windows x64 MSIX](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix) ：适用于绝大多数 Intel/AMD Windows 电脑
- [下载 Windows Arm64 MSIX](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) ：适用于 Snapdragon 等 Arm64 Windows 设备
- [下载离线许可证 ChatGPT-License.xml](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml) ：离线部署流程需要许可证文件时使用

这些稳定链接始终指向 OpenAI 最新发布的 Store 签名包。官方主要将它们用于 Microsoft Intune、MDM 或其他企业软件部署平台；普通个人用户仍应优先使用网页安装器或 `winget` 。

企业管理员应根据设备架构选择对应 MSIX，并按组织的 MDM/软件分发平台要求导入 MSIX 和（需要时）离线许可证。完成初次安装后，只要设备可访问 `persistent.oaistatic.com` ，应用即可按组织的更新策略获取后续更新。

详细说明见： [Windows 应用企业部署文档](https://developers.openai.com/codex/enterprise/windows-deployment) 。

### 四、安装后的首次使用

1. 打开 ChatGPT 桌面应用。
2. 使用 ChatGPT 账号登录。桌面应用、Codex CLI 和 IDE 扩展的本地工作也支持 API Key 登录。
3. 新建聊天、创建项目，或打开一个本地文件夹。
4. 在应用中选择 ChatGPT 或 Codex；使用 Codex 时，从 `New chat` 开始并描述要完成的任务。

使用 ChatGPT 登录时，Codex 权限、用量和数据控制取决于你的 ChatGPT 套餐及工作区策略。使用 API Key 时，费用按 OpenAI Platform 的标准 API 价格结算，依赖 ChatGPT 工作区或云服务的部分功能可能受限或不可用。

认证方式详见： [OpenAI authentication](https://developers.openai.com/codex/auth) 。

### 五、Windows 原生与 WSL2 怎么选

Windows 桌面应用默认使用 Windows 原生 Codex agent ，并在 PowerShell 中运行命令。也可以在设置中切换为 WSL，但切换后需要重启应用才会生效。

- 使用 Windows 原生 agent：项目优先放在 Windows 文件系统中；从 WSL 访问时使用 `/mnt/<盘符>/...`。
- 使用 WSL2 agent：可通过“添加新项目”打开 `\\wsl$\` 下 Linux 发行版中的目录。
- WSL1：从 Codex `0.115` 起不再受支持，应使用 WSL2。

在发送任务前，可在输入框下方选择 `Ask for approval` 以启用相应沙箱保护。 `Full access` 会扩大 Codex 可访问的范围，应只在明确理解风险时使用。

详见： [Windows 桌面应用与 WSL2](https://developers.openai.com/codex/app/windows) 。

### 六、不要把桌面应用和 Codex CLI 混淆

如果你需要图形界面，请使用第二节的 DMG、Windows 网页安装器或 MSIX。

如果你需要的是终端中的 **Codex CLI** ，请以官方 CLI 页面当前显示的安装方式为准。例如：

```bash
npm install -g @openai/codex
bash1
```

安装后在项目目录运行：

```bash
codex
bash1
```

CLI 与桌面应用是不同的使用入口，安装 CLI 不等于安装 Windows/macOS 图形界面客户端。

官方 CLI 文档： [Codex CLI](https://developers.openai.com/codex/cli) 。

### 七、常见问题

#### Windows 安装器为什么只有约 1.4 MB？

因为它是网页引导安装器，会在安装过程中获取完整应用。需要企业或离线部署时，请改用与设备架构匹配的官方 MSIX。

#### Windows x64 和 Arm64 应该选哪个？

大多数 Intel 或 AMD 处理器电脑选择 x64；Snapdragon 等 Arm Windows 设备选择 Arm64。可在“设置 > 系统 > 系统信息 > 系统类型”中确认。

#### macOS 应该选 Apple Silicon 还是 Intel？

在“苹果菜单 > 关于本机”中查看：显示 Apple M 系列芯片时选择 Apple Silicon；显示 Intel 处理器时选择 Intel。

#### Microsoft Store 被公司禁用，还能安装吗？

可以先试网页安装器。若 Microsoft 应用分发服务整体不可用，组织管理员可使用 OpenAI 官方 Store 签名 MSIX 和离线许可证，经 Intune、MDM 或软件部署平台分发。

#### 能否使用 API Key 登录？

可以。API Key 适用于本地 Codex 工作，但按 API 用量计费，且部分依赖 ChatGPT 工作区或云服务的功能会受限。日常个人使用通常优先选择 ChatGPT 账号登录。

### 八、官方来源与安全校验

本文只使用以下官方域名：

- `developers.openai.com` ：OpenAI 官方 Codex 文档
- `learn.chatgpt.com` ：OpenAI 官方 ChatGPT / Codex 文档的当前站点
- `persistent.oaistatic.com` ：OpenAI 官方安装包静态资源
- `get.microsoft.com` ：Microsoft 官方网页安装器
- `chatgpt.com` ：ChatGPT 与 Codex 官方服务
- `github.com/openai/codex` ：OpenAI Codex 开源仓库

核心官方页面：

不要从来源不明的网站下载“绿色版”“破解版”“免登录版”或重新打包的安装程序。Codex 可以访问本地项目和执行命令，篡改过的客户端可能造成登录凭证、源代码和本地文件泄露。