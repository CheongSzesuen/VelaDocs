<!-- 源地址: https://iot.mi.com/vela/quickapp/en/tools/dev/official-site-tutorial.html -->
<!-- 最近更新日期: 2026-05-26 -->

# AI-Powered Automated Workflow Generation

> Install an AI-powered development workflow with a single command, automating the entire process from requirement description to runnable code.

* * *

## Overview

The Vela Quick App AI Workflow is an AI-assisted development toolkit that incorporates the complete knowledge base of the Vela platform (components, APIs, layout specifications, best practices), enabling AI to write code like a seasoned Vela developer.

**All you need to provide** :

  * A requirement description (text, Feishu document, Markdown)
  * A design mockup (Figma link or screenshot, optional)

**AI automatically completes** :

  * Generates Product Requirement Document (PRD)
  * Creates technical solution
  * Produces complete runnable project code
  * Validates code quality

* * *

## Quick Installation

Ensure [Node.js (opens new window)](<https://nodejs.org/>) >= 16 is installed, then execute:

```bash
npx create-vela-workflow my-app
```

After installation, choose the appropriate development method based on your IDE.

* * *

## Two Usage Methods

Dimension | Method 1: Copilot Agent | Method 2: Kiro Workflow (Recommended)
---|---|---
IDE | AIoT IDE / VS Code | Kiro
AI Engine | GitHub Copilot (GPT-4o, etc.) | Kiro AI (Claude)
Installation Command | `npx create-vela-workflow . --mode copilot` | `npx create-vela-workflow . --mode kiro`
Startup Method | Select Agent in Copilot Chat | Reference workflow_starter.md in dialog
Breakpoint Resumption | — | ✅ Session mechanism
Auto Validation | Built-in Agent checks | Hooks event-driven
Best For | Teams with existing Copilot subscriptions | Teams pursuing deep automation
Debugging Method | AIoT-IDE built-in plugin | AIoT-IDE built-in plugin 

* * *

## Method 1: AIoT IDE / VS Code + GitHub Copilot

### Prerequisites

  * [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/en/tools/aiot-ide.html>) or [VS Code (opens new window)](<https://code.visualstudio.com/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>) extension (subscription required)
  * Node.js >= 16

### Installation

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

The following directories will be added to your project:

```
.github/
├── agents/                      # Custom Agents (selectable in Copilot Chat)
│   ├── vela-workflow.agent.md   # 🎯 Workflow entry
│   ├── vela-s1-prd.agent.md    # S1: PRD generation
│   ├── vela-s2-tech.agent.md   # S2: Technical solution
│   ├── vela-s3-coding.agent.md # S3: Code generation
│   └── vela-knowledge.agent.md # Knowledge base queries
├── rules/                       # Coding rules (auto-injected, AI must follow)
│   ├── vela-platform.md        # Component + API whitelist
│   ├── vela-layout.md          # Flexbox + round screen adaptation
│   └── ...
└── prompts/                     # Knowledge references (loaded as needed)
    ├── vela-components.prompt.md
    ├── vela-apis.prompt.md
    └── ...
```

### Usage

  1. Open project in IDE
  2. Open **Copilot Chat** panel
  3. Select **"Vela Quick App Workflow"** from Agent dropdown
  4. Enter requirements:

```
Create a weather app showing current temperature and 3-day forecast for Xiaomi Watch S5
```
  5. AI will guide you to choose mode:

     * **Full workflow** : S1 PRD → S2 Technical solution → S3 Code (recommended for standardized output)
     * **Quick mode** : Skip documentation, generate code directly (faster)
  6. After each stage completes, enter `y` to confirm, `e` to edit, or `n` to redo

### Figma Mockup Integration (Optional, Recommended)

For Figma mockups, additional Figma MCP configuration is required:

Add to `mcp.json` in VS Code's `~/Library/Application Support/Code/User/`:

```json
{
  "servers": {
    "figma": {
      "command": "uvx",
      "args": ["mcp-figma"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "your_token"
      }
    }
  }
}
```

> Token acquisition: Figma → Profile → Settings → Personal access tokens → Generate

When Copilot completes, you should see Figma MCP in Configure Tools dialog, indicating successful workspace configuration. Then paste Figma link directly in conversation for AI to generate project from mockup contents. Example:

```
Generate Vela quick app from design: https://www.figma.com/design/dhoPQU6dFpV5TDI7BnUAjU/APP?XXXX
```

Due to Figma MCP's free tier rate limiting, we recommend Figma Desktop with Dev account. Configure as follows:

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

Open Figma client in Dev mode and confirm MCP connection, then you can use commands like:

```
@sym:Figma Desktop Generate Vela quick app from current design
```

* * *

## Method 2: Kiro + Workflow

### Prerequisites

  * [Kiro IDE (opens new window)](<https://kiro.dev/>)
  * Node.js >= 16

### Installation

```bash
# Create new project and install
npx create-vela-workflow my-app --mode kiro

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode kiro
```

The following directories will be added to your project:

```
.kiro/
├── skills/vela-js-app/SKILL.md  # Complete Vela knowledge base
├── steering/                    # Workflow specifications (auto-loaded in each conversation)
├── hooks/                       # Automation hooks
│   ├── validate-ux-files        # Auto syntax check when editing .ux files
│   ├── figma-design-check       # Auto compare with design after writing code
│   └── post-coding-validation   # Auto quality validation after task completion
└── settings/mcp.json            # Figma MCP configuration

.workflow/
├── workflow_starter.md           # 🎯 Workflow entry
├── stages/                      # Three-stage orchestration
│   ├── s1_prd.md
│   ├── s2_tech_design.md
│   └── s3_coding.md
└── scripts/                     # Engine scripts (Session, context, checkpoints)
```

### Usage

  1. Open project in Kiro
  2. Enter in dialog:

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```
  3. Enter requirement content as prompted (supports multiple sources):

     * Direct text description
     * Local Markdown file path
     * Feishu document link
     * Web page link
  4. Provide design mockup (optional):

     * Figma link
     * Drag and drop design image
     * Enter "skip"
  5. Select workflow mode and AI executes automatically

### Kiro-Unique Features

**Session Breakpoint Resumption** : Enter `q` during development to save progress, which will be automatically detected and prompted for resumption next time.

**Automation Hooks** :

  * After saving `.ux` file → Auto syntax check
  * After code generation → Auto validate route consistency and API declarations
  * With Figma design → Auto compare design fidelity

**Steering Global Specifications** : Vela platform constraints (no third-party libraries, forced Flexbox, round screen safe areas, etc.) are automatically injected into each conversation without manual reference.

### Figma Mockup Integration (Same as Method 1)

* * *

## Workflow Demonstration

### Full Workflow Example

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

### Quick Mode Example (with design mockup)

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

* * *

## Generated Code Specifications

AI-generated code automatically follows these specifications (no manual configuration needed):

Specification | Description
---|---
Component Whitelist | Only uses Vela built-in components (div, text, image, list, etc.)
API Whitelist | Only uses @system.xxx system APIs
No Third-Party Libraries | No axios, lodash, echarts, etc.
Flexbox Layout | Default flex-direction: column
Round Screen Adaptation | Auto safe area padding (50px top/bottom, 36px left/right)
Asset Format | PNG images only, no SVG
Route Consistency | manifest.json routes automatically align with actual page files
API Declarations | Imported APIs automatically declared in features
Memory Optimization | onDestroy cleans timers, static marks static nodes 

* * *

## Device Size Reference

Device | Pixel Dimensions | Screen Shape | designWidth
---|---|---|---
Xiaomi Watch S5 | 480×480 | Round | 480
Xiaomi Watch S3/S4/H1 | 466×466 | Round | 466
REDMI Watch 5 | 432×514 | Square | 432
Xiaomi Band 9 | 192×490 | Track | 192 

Target device screen specs can be specified at workflow startup for automatic layout and safe area adaptation.

* * *

## Updating Workflow

When a new toolkit version is released, update with a single command:

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

* * *

## FAQ

### Installation Issues

**Q:`npx create-vela-workflow` fails?**

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

**Q: Can both methods be installed simultaneously?**

Yes. `.github/` and `.kiro/` \+ `.workflow/` don't conflict, allowing team members to choose based on their IDE.

### Usage Issues

**Q: Can generated code run directly?**

Yes. Generated projects include complete `package.json` and build config:

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

Use [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/en/tools/aiot-ide.html>) to open project and click debug button to launch simulator.

**Q: How to debug generated code?**

Run simulator in AIoT IDE and have AI automatically debug against Figma design

**Q: Can I customize AI coding rules?**

Yes. Edit configuration files after installation:

  * Method 1: Modify Markdown files in `.github/rules/`
  * Method 2: Modify Markdown files in `.kiro/steering/`

**Q: Why doesn't generated code exactly match design?**

  * Check if workspace has proper MCP configuration (e.g., mcp-figma)
  * Different models may generate slightly different code
  * Recommend adding check: "Please review project code against Figma design, ensuring correct dimensions, fonts, and complete consistency"
  * For missing graphics, enter: "Please import design images to project common and reference them"

**Q: What requirement input methods are supported?**

Input Method | Method 1 | Method 2
---|---|---
Text description | ✅ | ✅
Markdown file | ✅ | ✅
Feishu document link | — | ✅ (requires Feishu MCP)
Web page link | ✅ | ✅
Figma design | ✅ (requires Figma MCP) | ✅ (requires Figma Desktop)
Design screenshot | ✅ | ✅ 

* * *

## Related Resources

  * [Vela Quick App Development Docs (opens new window)](<https://iot.mi.com/vela/quickapp/>)
  * [AIoT IDE Download (opens new window)](<https://iot.mi.com/vela/quickapp/en/tools/aiot-ide.html>)
  * [Kiro IDE Download (opens new window)](<https://kiro.dev/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>)
  * npm package: `npx create-vela-workflow --help`
