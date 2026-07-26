<!-- 源地址: https://iot.mi.com/vela/quickapp/en/tools/dev/official-site-tutorial.html -->
<!-- 最近更新日期: 2026-06-23 -->

# AI Automated Workflow Generation

> Install an AI development workflow with a single command, automating the entire process from requirement description to runnable code.

* * *

## Overview

The Vela Quick App AI Workflow is an AI-assisted development toolkit that incorporates the complete knowledge base of the Vela platform (components, APIs, layout specifications, best practices), enabling AI to write code like a seasoned Vela developer.

**All you need to provide** :

  * A requirement description (text, Feishu document, Markdown are all acceptable)
  * A design draft (Figma link or screenshot, optional)

**AI automatically completes** :

  * Generate Product Requirement Document (PRD)
  * Generate technical solution
  * Generate complete runnable project code
  * Automatically validate code quality

* * *

## Quick Installation

Ensure [Node.js (opens new window)](<https://nodejs.org/>) >= 16 is installed, then execute:

```bash
npx create-vela-workflow my-app
```

After installation, choose the appropriate method to start development based on your IDE.

* * *

## Two Usage Methods

Dimension | Method 1: Copilot Agent | Method 2: Kiro Workflow (Recommended)
---|---|---
IDE | AIoT IDE / VS Code | Kiro
AI Engine | GitHub Copilot (GPT-4o, etc.) | Kiro AI (Claude)
Installation Command | `npx create-vela-workflow . --mode copilot` | `npx create-vela-workflow . --mode kiro`
Startup Method | Select Agent in Copilot Chat | Reference workflow_starter.md in dialog box
Breakpoint Resumption | — | ✅ Session mechanism
Automatic Validation | Built-in checks in Agent | Hooks event-driven
Suitable For | Teams with existing Copilot subscriptions | Teams pursuing deep automation
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

After installation, the following `.github/` directory will be added to the project:

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
└── prompts/                     # Knowledge references (loaded on demand)
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

     * **Full process** : S1 PRD → S2 Technical solution → S3 Code (recommended for more standardized output)
     * **Quick mode** : Skip documentation and generate code directly (faster)
  6. After each stage completes, enter `y` to confirm, `e` to modify, or `n` to redo

### Figma Design Draft Integration (Optional, Recommended)

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

When Copilot completes, you should see Figma MCP in the Configure Tools dialog, indicating successful workspace configuration. Then simply paste the Figma link directly in the conversation for AI to read and generate the project. For example:

```
Generate a Vela quick app based on design draft: https://www.figma.com/design/dhoPQU6dFpV5TDI7BnUAjU/APP?XXXX
```

Due to rate limits on free Figma MCP access, we recommend getting Figma Desktop and generating with a Dev account. Configuration JSON:

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

Open Figma client in Dev mode and confirm MCP is connected, then for example you can directly enter:

```
@sym:Figma Desktop Help me generate the corresponding Vela quick app based on the content in the currently open design draft
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

After installation, the following `.kiro/` and `.workflow/` directories will be added to the project:

```
.kiro/
├── skills/vela-js-app/SKILL.md  # Complete Vela knowledge base
├── steering/                    # Workflow specifications (automatically loaded into each conversation)
├── hooks/                       # Automation hooks
│   ├── validate-ux-files        # Automatic syntax check when editing .ux files
│   ├── figma-design-check       # Automatic design draft comparison after code writing
│   └── post-coding-validation   # Automatic quality validation after task completion
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
  2. Enter in dialog box:

```
@.workflow/workflow_starter.md
```
  3. Enter requirement content as prompted (supports multiple sources):

     * Direct text description
     * Local Markdown file path
     * Feishu document link
     * Web page link
  4. Provide design draft (optional):

     * Figma link
     * Drag and drop design image
     * Enter "skip"
  5. Select workflow mode and AI will execute automatically

### Kiro Unique Features

**Session Breakpoint Resumption** : During development, enter `q` to save progress. Next time it will automatically detect and prompt for resumption.

**Automation Hooks** :

  * Every save of `.ux` file → automatic syntax error check
  * Code generation complete → automatic validation of route consistency and API declarations
  * With Figma design draft → automatic design reproduction comparison

**Steering Global Specifications** : Vela platform constraints (no third-party libraries, enforce Flexbox, round screen safe areas, etc.) are automatically injected into each conversation without manual reference.

### Figma Design Draft Integration (Same as Method 1)

* * *

## Workflow Demonstration

### Full Process Example

```
User: Develop an accounting app supporting addition of income/expense records and monthly statistics viewing

AI:   📝 Requirement received
      📐 Screen specification: 480×480 round screen (default)

      ❓ Please select workflow mode:
        [1] Full process  [2] Direct code generation

User: 1

AI:   🚀 S1 - PRD generation...
      ━━━━━━━━━━━━━━━━━━━━
      📄 Feature list:
        • Home: Income/expense overview + quick accounting button
        • Accounting page: Amount input + category selection
        • Statistics page: Monthly income/expense chart
      ❓ [y] Confirm  [e] Modify  [n] Redo

User: y

AI:   🚀 S2 - Technical solution...
      ━━━━━━━━━━━━━━━━━━━━
      📄 Page routes: 3 pages
      📄 Data storage: @system.storage
      📄 Chart: Built-in chart component
      ❓ [y] Confirm  [e] Modify  [n] Redo

User: y

AI:   🚀 S3 - Code generation...
      ━━━━━━━━━━━━━━━━━━━━
      📂 npx create-aiot ux --name accounting-app
      📄 Generate 3 pages + manifest configuration
      ✅ Quality validation passed

      🎉 Project creation completed!
```

### Quick Mode Example (with design draft)

```
User: Help me make a music player
      Design draft: https://www.figma.com/design/xxxxx

AI:   🎨 Parsing design draft...
      ✅ Detected 2 pages, 8 icons
      🖼️ Exporting PNG assets to src/common/images/

      📂 npx create-aiot ux --name music-player
      📄 Generate player home + playlist page
      🎨 Strict design reproduction (colors, font sizes, spacing)
      ✅ Code generation completed!
```

* * *

## Generated Code Specifications

AI-generated code automatically follows these specifications (no manual configuration required):

Specification | Description
---|---
Component Whitelist | Only use built-in Vela components (div, text, image, list, etc.)
API Whitelist | Only use @system.xxx system APIs
No Third-party Libraries | Do not import axios, lodash, echarts, etc.
Flexbox Layout | Default flex-direction: column
Round Screen Adaptation | Automatically add safe area padding (50px top/bottom, 36px left/right)
Asset Format | Images only in PNG format, no SVG allowed
Route Consistency | manifest.json routes automatically align with actual page files
API Declarations | Imported APIs automatically declared in features
Memory Optimization | Clean timers in onDestroy, mark static nodes as static

* * *

## Device Size Reference

Device | Pixel Dimensions | Screen Shape | designWidth
---|---|---|---
Xiaomi Watch S5 | 480×480 | Round | 480
Xiaomi Watch S3/S4/H1 | 466×466 | Round | 466
REDMI Watch 5 | 432×514 | Square | 432
Xiaomi Band 9 | 192×490 | Track | 192

The workflow can specify any target device screen specifications at startup, and AI will automatically adapt the layout and safe areas.

* * *

## Update Workflow

When a new version of the toolkit is released, update with a single command:

```bash
npx create-vela-workflow@latest . --mode all
```

* * *

## FAQ

### Installation Issues

**Q:`npx create-vela-workflow` execution fails?**

```bash
# Check Node.js version (needs >= 16)
node --version

# If npm registry has issues, switch to official registry
npm config set registry https://registry.npmjs.org/
```

**Q: Can both methods be installed simultaneously?**

Yes. `.github/` and `.kiro/` \+ `.workflow/` don't conflict, allowing team members to choose based on their IDE.

### Usage Issues

**Q: Can the generated code run directly?**

Yes. The generated project includes complete `package.json` and build configuration:

```bash
cd my-app
npm install
npm run build    # Build rpk package
```

You can open the project in [AIoT IDE (opens new window)](<https://iot.mi.com/vela/quickapp/en/tools/aiot-ide.html>) and click the debug button to launch the simulator.

**Q: What if the generated code needs debugging?**

You can have the AI automatically debug using the [velajs mcp service (opens new window)](<https://www.npmjs.com/package/velajs-mcp>).

**Q: Can I customize AI coding rules?**

Yes. Edit the configuration files after installation:

  * Method 1: Modify Markdown files under `.github/rules/`
  * Method 2: Modify Markdown files under `.kiro/steering/`

**Q: Why doesn't the generated project code exactly match the design draft?**

  * Check if the workspace has properly configured the corresponding MCP (e.g., mcp-figma)
  * Different models may generate slightly different code
  * Recommend adding checks like: `Please review the project code against the Figma design draft to ensure correct dimensions, fonts, and complete consistency`
  * For missing graphics, enter: `Please import the design draft image assets into the project's common folder and reference them`

**Q: What requirement input methods are supported?**

Input Method | Method 1 | Method 2
---|---|---
Text description | ✅ | ✅
Markdown file | ✅ | ✅
Feishu document link | — | ✅ (requires Feishu MCP)
Web page link | ✅ | ✅
Figma design draft | ✅ (requires Figma MCP) | ✅ (requires Figma Desktop)
Design screenshot | ✅ | ✅

* * *

## Related Resources

  * [Vela Quick App Development Documentation (opens new window)](<https://iot.mi.com/vela/quickapp/>)
  * [AIoT IDE Download (opens new window)](<https://iot.mi.com/vela/quickapp/en/tools/aiot-ide.html>)
  * [Kiro IDE Download (opens new window)](<https://kiro.dev/>)
  * [GitHub Copilot (opens new window)](<https://github.com/features/copilot>)
  * npm package: `npx create-vela-workflow --help`
