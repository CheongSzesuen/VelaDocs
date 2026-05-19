<!-- 源地址: https://iot.mi.com/vela/quickapp/en/tools/dev/official-site-tutorial.html -->

# AI Automated Generation

> Install the AI development workflow with a single command, automating the entire process from requirement description to runnable code.

* * *

## Overview

The Vela Quick App AI Workflow is an AI-assisted development toolkit that incorporates the complete knowledge base of the Vela platform (components, APIs, layout specifications, best practices), enabling AI to write code like a seasoned Vela developer.

**All you need to provide** :

  * A requirement description (text, Feishu document, or Markdown)
  * A design draft (Figma link or screenshot, optional)

**AI automatically completes** :

  * Generate Product Requirement Document (PRD)
  * Generate technical solution
  * Generate complete, runnable project code
  * Automatically validate code quality

* * *

## Quick Installation

Ensure [Node.js (opens new window)](<https://nodejs.org/>) >= 16 is installed, then execute:

```bash
npx create-vela-workflow my-app
```

After installation, choose the corresponding development method based on your IDE.

* * *

## Two Usage Methods

Dimension | Method 1: Copilot Agent | Method 2: Kiro Workflow (Recommended)
---|---|---
IDE | AIoT IDE / VS Code | Kiro
AI Engine | GitHub Copilot (GPT-4o, etc.) | Kiro AI (Claude)
Installation Command | `npx create-vela-workflow . --mode copilot` | `npx create-vela-workflow . --mode kiro`
Startup Method | Select Agent in Copilot Chat | Reference workflow_starter.md in dialog
Breakpoint Recovery | — | ✅ Session mechanism
Automatic Validation | Built-in checks in Agent | Hooks event-driven
Suitable For | Teams with existing Copilot subscriptions | Teams pursuing deep automation
Debugging Method | Built-in plugins, supports [velajs-mcp (opens new window)](https://www.npmjs.com/package/velajs-mcp) | Supports [velajs-mcp (opens new window)](https://www.npmjs.com/package/velajs-mcp) 

* * *

## Method 1: AIoT IDE / VS Code + GitHub Copilot

### Prerequisites

  * [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>) or [VS Code (opens new window)](<https://code.visualstudio.com/>)
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

After installation, the `.github/` directory will be added to the project:

```
.github/
├── agents/                      # Custom Agents (optional in Copilot Chat)
│   ├── vela-workflow.agent.md   # 🎯 Workflow entry
│   ├── vela-s1-prd.agent.md    # S1: PRD generation
│   ├── vela-s2-tech.agent.md   # S2: Technical solution
│   ├── vela-s3-coding.agent.md # S3: Code generation
│   └── vela-knowledge.agent.md # Knowledge base query
├── rules/                       # Coding rules (automatically injected, enforced by AI)
│   ├── vela-platform.md        # Component + API whitelist
│   ├── vela-layout.md          # Flexbox + round screen adaptation
│   └── ...
└── prompts/                     # Knowledge references (loaded as needed)
    ├── vela-components.prompt.md
    ├── vela-apis.prompt.md
    └── ...
```

### Usage

  1. Open the project in IDE
  2. Open **Copilot Chat** panel
  3. Select **"Vela Quick App Workflow"** from Agent dropdown menu
  4. Enter requirements:

```
Create a weather app showing current temperature and 3-day forecast for Xiaomi Watch S5
```
  5. AI will guide you to choose mode:

     * **Full process** : S1 PRD → S2 Technical solution → S3 Code (recommended for standardized output)
     * **Quick mode** : Skip documentation, generate code directly (faster)
  6. After each stage completes, enter `y` to confirm, `e` to modify, or `n` to redo

### Figma Design Integration (Optional, Recommended)

For Figma design drafts, additional Figma MCP configuration is required:

Add to `~/Library/Application Support/Code/User/mcp.json` in VS Code:

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

After Copilot completes, you should see Figma MCP in the Configure Tools dialog, indicating successful workspace configuration. Then simply paste the Figma link in the dialog to let AI read its content and generate the project. For example:

```
Generate a Vela quick app based on design draft: https://www.figma.com/design/dhoPQU6dFpV5TDI7BnUAjU/APP?XXXX
```

Since free Figma MCP access has rate limits, we recommend getting Figma Desktop and generating with a Dev account. Configure as follows:

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

Open Figma client in Dev mode and confirm MCP is connected, then you can directly input:

```
@sym:Figma Desktop Generate the corresponding Vela quick app based on the content of the currently opened design draft
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

After installation, `.kiro/` and `.workflow/` directories will be added to the project:

```
.kiro/
├── skills/vela-js-app/SKILL.md  # Complete Vela knowledge base
├── steering/                    # Workflow specifications (automatically loaded into each dialog)
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
  4. Provide design draft (optional):

     * Figma link
     * Drag in design image
     * Enter "skip"
  5. Select workflow mode and AI executes automatically

### Kiro Unique Features

**Session Breakpoint Recovery** : During development, enter `q` to save progress. Next time it will automatically detect and prompt to resume.

**Automation Hooks** :

  * Every save of `.ux` file → Auto syntax error check
  * Code generation complete → Auto validate routing consistency and API declarations
  * With Figma design → Auto compare design reproduction accuracy

**Steering Global Specifications** : Vela platform constraints (no third-party libraries, enforce Flexbox, round screen safe areas, etc.) are automatically injected into each dialog without manual reference.

### Figma Design Integration (Same as Method 1)

* * *

## Workflow Demonstration

### Complete Process Example

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

### Quick Mode Example (with design draft)

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
Component Whitelist | Only use Vela built-in components (div, text, image, list, etc.)
API Whitelist | Only use @system.xxx system APIs
No Third-Party Libraries | No axios, lodash, echarts, etc.
Flexbox Layout | Default flex-direction: column
Round Screen Adaptation | Auto add safe area padding (50px top/bottom, 36px left/right)
Asset Format | Only PNG images, no SVG
Routing Consistency | manifest.json routing automatically aligns with actual page files
API Declarations | Imported APIs automatically declared in features
Memory Optimization | onDestroy cleans timers, static marks static nodes 

* * *

## Supported Devices

Device | Pixel Dimensions | Screen Shape | designWidth
---|---|---|---
Xiaomi Watch S5 | 480×480 | Round | 480
Xiaomi Watch S3/S4/H1 | 466×466 | Round | 466
REDMI Watch 5 | 432×514 | Square | 432
Xiaomi Band 9 | 192×490 | Track | 192 

Specify target device screen specs when starting workflow, AI will automatically adapt layout and safe areas.

* * *

## Update Workflow

When a new toolkit version is released, update with one command:

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

**Q:`npx create-vela-workflow` fails to execute?**

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

**Q: Can both methods be installed simultaneously?**

Yes. `.github/` and `.kiro/` \+ `.workflow/` don't conflict. Team members can choose based on their IDE.

### Usage Issues

**Q: Can generated code run directly?**

Yes. Generated project includes complete `package.json` and build config:

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

Use [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>) to open project and click debug button to launch simulator.

**Q: How to debug generated code?**

Use AIoT IDE for debugging or install [velajs-mcp (opens new window)](<https://www.npmjs.com/package/velajs-mcp>) to let AI automatically debug against Figma design:

```bash
# Create new project and install
npx create-vela-workflow my-app --mode copilot

# Or install in existing project
cd your-project
npx create-vela-workflow . --mode copilot
```

**Q: Can I customize AI coding rules?**

Yes. Edit configuration files after installation:

  * Method 1: Modify Markdown files under `.github/rules/`
  * Method 2: Modify Markdown files under `.kiro/steering/`

**Q: Why doesn't generated code exactly match design draft?**

  * Check if workspace has correct MCP configured (e.g., mcp-figma)
  * Different models may generate slightly different code
  * Recommend adding check: "Please review project code against Figma design, ensure correct dimensions, fonts, and complete reproduction"
  * For missing graphics, enter: "Please import design draft image assets to project common and reference them"

**Q: What requirement input methods are supported?**

Input Method | Method 1 | Method 2
---|---|---
Text description | ✅ | ✅
Markdown file | ✅ | ✅
Feishu document link | — | ✅ (needs Feishu MCP)
Web page link | ✅ | ✅
Figma design | ✅ (needs Figma MCP) | ✅ (needs Figma Desktop)
Design screenshot | ✅ | ✅ 

* * *

## Related Resources

  * [Vela Quick App Development Docs (opens new window)](<https://iot.mi.com/vela/quickapp/>)
  * [AIoT IDE Download (opens new window)](<https://iot.mi.com/vela/quickapp/zh/tools/aiot-ide.html>)
  * [Kiro IDE Download (opens new window)](<https://kiro.dev/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>)
  * [velajs-mcp Debugging Tool (opens new window)](<https://www.npmjs.com/package/velajs-mcp>)
  * npm package: `npx create-vela-workflow --help`
