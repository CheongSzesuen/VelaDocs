<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/tools/dev/official-site-tutorial.html -->
<!-- 最近更新日期: 2026-05-26 -->

# AI 自动化生成

> 一行命令安装 AI 开发工作流，从需求描述到可运行代码，全程自动化。

* * *

## 概述

vela 快应用 AI 工作流是一套 AI 辅助开发工具包，内置了 vela 平台的完整知识体系（组件、API、布局规范、最佳实践），让 AI 像一位资深 vela 开发工程师一样帮你写代码。

**你只需要提供** ：

  * 一段需求描述（文字、飞书文档、Markdown 均可）
  * 一个设计稿（Figma 链接或截图，可选）

**AI 自动完成** ：

  * 生成产品需求文档（PRD）
  * 生成技术方案
  * 生成完整可运行的项目代码
  * 自动校验代码质量

* * *

## 快速安装

确保已安装 [Node.js (opens new window)](<https://nodejs.org/>) >= 16，然后执行：

```bash
npx create-vela-workflow my-app
```

安装完成后，根据你使用的 IDE 选择对应方式开始开发。

* * *

## 两种使用方式

维度 | 方式一：Copilot Agent | 方式二：Kiro Workflow （推荐）
---|---|---
IDE | AIoT IDE / VS Code | Kiro
AI 引擎 | GitHub Copilot（GPT-4o 等） | Kiro AI（Claude）
安装命令 | `npx create-vela-workflow . --mode copilot` | `npx create-vela-workflow . --mode kiro`
启动方式 | Copilot Chat 选择 Agent | 对话框引用 workflow_starter.md
断点恢复 | — | ✅ Session 机制
自动校验 | Agent 内置检查 | Hooks 事件驱动
适合 | 已有 Copilot 订阅的团队 | 追求深度自动化的团队
调试方式 | AIOT-IDE内置插件 | AIOT-IDE内置插件 

* * *

## 方式一：AIoT IDE / VS Code + GitHub Copilot

### 前置要求

  * [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>) 或 [VS Code (opens new window)](<https://code.visualstudio.com/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>) 扩展（需订阅）
  * Node.js >= 16

### 安装

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

安装后项目中会多出 `.github/` 目录：

```
.github/
├── agents/                      # 自定义 Agent（Copilot Chat 中可选）
│   ├── vela-workflow.agent.md   # 🎯 工作流入口
│   ├── vela-s1-prd.agent.md    # S1: PRD 生成
│   ├── vela-s2-tech.agent.md   # S2: 技术方案
│   ├── vela-s3-coding.agent.md # S3: 代码生成
│   └── vela-knowledge.agent.md # 知识库查询
├── rules/                       # 编码规则（自动注入，AI 强制遵守）
│   ├── vela-platform.md        # 组件 + API 白名单
│   ├── vela-layout.md          # Flexbox + 圆屏适配
│   └── ...
└── prompts/                     # 知识参考（按需加载）
    ├── vela-components.prompt.md
    ├── vela-apis.prompt.md
    └── ...
```

### 使用

  1. 在 IDE 中打开项目
  2. 打开 **Copilot Chat** 面板
  3. 在 Agent 下拉菜单中选择 **「Vela 快应用工作流」**
  4. 输入需求：

```
创建一个天气应用，显示当前温度和未来3天天气预报，目标设备 Xiaomi Watch S5
```
  5. AI 会引导你选择模式：

     * **完整流程** ：S1 PRD → S2 技术方案 → S3 代码（推荐，产出更规范）
     * **快速模式** ：跳过文档，直接生成代码（更快速）
  6. 每个阶段完成后，输入 `y` 确认、`e` 修改、`n` 重做

### Figma 设计稿集成（可选，推荐）

如果有 Figma 设计稿，需要额外配置 Figma MCP：

在 VS Code 的 `~/Library/Application Support/Code/User/mcp.json` 中添加：

```json
{
  "servers": {
    "figma": {
      "command": "uvx",
      "args": ["mcp-figma"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "你的Token"
      }
    }
  }
}
```

> Token 获取：Figma → 头像 → Settings → Personal access tokens → Generate

在Copilot的完成，在对话Configure Tools里能看到Figma MCP，说明当前工作区配置成功。接着对话中直接粘贴 Figma 链接，让AI 读取链接内容生成项目。例如你可以直接输入：

```
生成vela快应用，根据设计稿：https://www.figma.com/design/dhoPQU6dFpV5TDI7BnUAjU/APP?XXXX
```

由于Figma MCP免费获取会限流，建议开通Figma 桌面版，然后开通Dev账号生成。配置json如下：

```json
{
  "servers": {
    "Figma Desktop": {
      "type": "http",
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

打开Figma客户端Dev模式，确认MCP处于连接状态后，例如你可以直接输入：

```
@sym:Figma Desktop 帮我根据当前打开的设计稿里的内容，生成对应的vela快应用
```

* * *

## 方式二：Kiro + Workflow

### 前置要求

  * [Kiro IDE (opens new window)](<https://kiro.dev/>)
  * Node.js >= 16

### 安装

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode kiro

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode kiro
```

安装后项目中会多出 `.kiro/` 和 `.workflow/` 目录：

```
.kiro/
├── skills/vela-js-app/SKILL.md  # 完整 vela 知识库
├── steering/                    # 工作流规范（自动加载到每次对话）
├── hooks/                       # 自动化钩子
│   ├── validate-ux-files        # 编辑 .ux 时自动语法检查
│   ├── figma-design-check       # 写入代码后自动对比设计稿
│   └── post-coding-validation   # 任务完成后自动质量校验
└── settings/mcp.json            # Figma MCP 配置

.workflow/
├── workflow_starter.md           # 🎯 工作流入口
├── stages/                      # 三阶段编排
│   ├── s1_prd.md
│   ├── s2_tech_design.md
│   └── s3_coding.md
└── scripts/                     # 引擎脚本（Session、上下文、检查点）
```

### 使用

  1. 在 Kiro 中打开项目
  2. 在对话框中输入：

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```
  3. 按提示输入需求内容（支持多种来源）：

     * 直接文字描述
     * 本地 Markdown 文件路径
     * 飞书文档链接
     * 网页链接
  4. 提供设计稿（可选）：

     * Figma 链接
     * 拖入设计图片
     * 输入"跳过"
  5. 选择工作流模式后，AI 自动执行

### Kiro 独有特性

**Session 断点恢复** ：开发中途可以输入 `q` 保存进度，下次打开自动检测并提示恢复。

**自动化 Hooks** ：

  * 每次保存 `.ux` 文件 → 自动检查语法错误
  * 代码生成完成 → 自动校验路由一致性、API 声明
  * 有 Figma 设计稿 → 自动对比设计还原度

**Steering 全局规范** ：Vela 平台约束（禁止第三方库、强制 Flexbox、圆屏安全区域等）自动注入每次对话，无需手动引用。

### Figma 设计稿集成（同方式一里的集成方式）

* * *

## 工作流演示

### 完整流程示例

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

### 快速模式示例（带设计稿）

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

* * *

## 生成代码规范

AI 生成的代码自动遵循以下规范（无需手动配置）：

规范 | 说明
---|---
组件白名单 | 仅使用 vela 内置组件（div, text, image, list 等）
API 白名单 | 仅使用 @system.xxx 系统 API
禁止第三方库 | 不引入 axios、lodash、echarts 等
Flexbox 布局 | 默认 flex-direction: column
圆屏适配 | 自动添加安全区域 padding（上下 50px，左右 36px）
资源格式 | 图片仅 PNG，禁止 SVG
路由一致性 | manifest.json 路由与实际页面文件自动对齐
API 声明 | import 的 API 自动在 features 中声明
内存优化 | onDestroy 清理定时器，static 标记静态节点 

* * *

## 设备尺寸参考

设备 | 像素尺寸 | 屏幕形状 | designWidth
---|---|---|---
Xiaomi Watch S5 | 480×480 | 圆屏 | 480
Xiaomi Watch S3/S4/H1 | 466×466 | 圆屏 | 466
REDMI Watch 5 | 432×514 | 方屏 | 432
小米手环 9 | 192×490 | 跑道屏 | 192 

工作流启动时可指定任意目标设备屏幕规格，AI 会自动适配布局和安全区域。

* * *

## 更新工作流

当工具包发布新版本时，一行命令即可更新：

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

* * *

## 常见问题

### 安装相关

**Q:`npx create-vela-workflow` 执行失败？**

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

**Q: 两种方式可以同时安装吗？**

可以。`.github/` 和 `.kiro/` \+ `.workflow/` 互不冲突，团队成员可以根据自己的 IDE 选择对应方式。

### 使用相关

**Q: 生成的代码能直接运行吗？**

可以。生成的项目包含完整的 `package.json` 和构建配置：

```bash
# 新建项目并安装
npx create-vela-workflow my-app --mode copilot

# 或在已有项目中安装
cd your-project
npx create-vela-workflow . --mode copilot
```

可以使用 [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>) 打开项目，直接点击调试按钮启动模拟器。

**Q: 生成的代码需要调试怎么办？**

使用AIoT IDE运行模拟器，可以让 AI 对比 Figma 设计稿自动调试

**Q: 可以自定义 AI 的编码规则吗？**

可以。直接编辑安装后的配置文件：

  * 方式一：修改 `.github/rules/` 下的 Markdown 文件
  * 方式二：修改 `.kiro/steering/` 下的 Markdown 文件

**Q: 为什么生成的项目代码没有完全按照设计稿来？**

  * 检查工作区是否正确配置了对应的 MCP（如：mcp-figma）
  * 不同模型生成的代码会有差异
  * 建议增加检查，如输入：`请结合figma设计稿，走查项目代码，保证宽高正确，字体正确，生成相关完全一致`
  * 图形未导入情况，可输入：`请将设计稿图片资源导入项目common并引用`

**Q: 支持哪些需求输入方式？**

输入方式 | 方式一 | 方式二
---|---|---
文字描述 | ✅ | ✅
Markdown 文件 | ✅ | ✅
飞书文档链接 | — | ✅（需飞书 MCP）
网页链接 | ✅ | ✅
Figma 设计稿 | ✅（需 Figma MCP） | ✅（需 Figma Desktop）
设计截图 | ✅ | ✅ 

* * *

## 相关资源

  * [vela 快应用开发文档 (opens new window)](<https://iot.mi.com/vela/quickapp/>)
  * [AIoT IDE 下载 (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>)
  * [Kiro IDE 下载 (opens new window)](<https://kiro.dev/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>)
  * npm 包：`npx create-vela-workflow --help`
