<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/ -->

# # 概述

Xiaomi Vela JS 应用是小米公司开发的一种应用类型，它是基于小米的物联网嵌入式软件平台 Xiaomi Vela OS 开发的。本文将介绍 Xiaomi Vela JS 应用的特点、应用场景以及开发支持，帮助开发者更好地了解和使用这一应用类型。

如果您想快速了解如何开发 Xiaomi Vela JS 应用，并且希望快速上手，请直接访问 [快速入门](</vela/quickapp/zh/guide/start.html>) 章节。

## # 应用特点

Xiaomi Vela JS 应用是一种基于 Xiaomi Vela OS 操作系统的轻量级应用模式，旨在为智能穿戴设备提供更加流畅和便捷的用户体验。它具备以下显著特点：

  * **轻量化：** Xiaomi Vela JS 应用采用了轻量级的架构设计，与传统的应用程序相比，Xiaomi Vela JS 应用具有更小的体积，这使得它们能够快速加载和运行，尤其适合内存和处理能力有限的穿戴设备。
  * **跨平台兼容性：** Xiaomi Vela JS 应用支持跨端运行，开发者可以一次开发，实现在多种设备上的运行，这大大提高了开发效率和应用的普及率。
  * **高性能渲染：** 系统优化了渲染能力，使得应用的动画和交互更为流畅，提升了用户的使用体验。
  * **安全性能：** Xiaomi Vela OS 通过三重隔离机制确保了应用的安全性，保护了用户数据和设备的安全。
  * **开发支持：** 小米提供了全面的开发支持 Xiaomi Vela JS 应用的开发工具和文档齐全，开发者可以轻松上手，快速构建高质量的应用。小米提供了包括AIoT-IDE在内的一系列开发工具，支持开发者在Ubuntu、Windows、MacOS等操作系统上进行Xiaomi Vela JS 应用的开发和调试。

## # 应用场景

Xiaomi Vela JS 应用的应用场景广泛，已落地多款产品，覆盖了智能穿戴设备上的多种使用情形：

  * **健康监测：** 应用可以实时监测用户的心率、睡眠质量等健康数据，为用户提供健康建议和预警。
  * **运动辅助：** 在用户进行运动时，应用能够记录运动数据，提供运动指导和健康管理。
  * **消息提醒：** 应用能够显示手机等设备的消息提醒，方便用户在不拿出手机的情况下查看重要信息。
  * **移动支付：** 应用可以集成支付功能，用户可以直接在穿戴设备上完成支付操作，提高支付的便捷性。
  * **智能控制：** 作为智能家居的控制中心，应用可以远程操控家中的智能设备，如灯光、空调等。
  * **日常工具：** 提供天气预报、闹钟、计时器等日常工具功能，满足用户的多样化需求。

## # 技术优势

相较于传统的应用框架，Xiaomi Vela JS 应用具有以下技术优势：

### # 前端开发范式

Xiaomi Vela JS 应用采用JavaScript语言开发，并且支持前端MVVM高效的开发范式，响应式UI框架，易学易用。使得开发者可以降低上手难度，缩短开发周期。这种模式贴合主流前端开发者的思维习惯，使得开发者能够快速构建出功能丰富、交互友好的应用，同时降低了学习成本。参考[开发语法](</vela/quickapp/zh/guide/framework/>)。

### # 统一的API和组件

Xiaomi Vela JS 应用提供了统一的[JS接口](</vela/quickapp/zh/features/>)和[UI组件](</vela/quickapp/zh/components/>)，使得开发者无需关心底层硬件和操作系统的差异，简化了开发流程，同时保证了应用的质量和用户体验。

### # 高性能渲染

  * 通过架构优化，让复杂计算下沉到原生层，解决 JS 语言的性能瓶颈，从而拥有媲美原生的运行效率和流畅体验。
  * 提供丰富的动效能力，包括30+插值和物理动效，可用于过渡、转场等动画效果，使用户界面更加生动、有趣和富有表现力。
  * 充分挖掘硬件性能，最大限度利用 GPU 和 CPU 的硬件加速能力，让复杂UI 界面和动画更加流畅，达到 60 fps 满帧效果。

### # 多屏适配

[多屏适配](</vela/quickapp/zh/guide/multi-screens/>)是Xiaomi Vela JS 应用框架的另一大特色，具体表现在：

  * **[适配规范](</vela/quickapp/zh/guide/multi-screens/specs.html>)：** 框架支持不同形状、尺寸和分辨率的屏幕自适应，确保应用在各种设备上都能提供良好的视觉体验。
  * **[设计规范](</vela/quickapp/zh/guide/design/multi-screens.html>)：** Vela提供了一套多屏设计的技术规范，帮助开发者按照设计稿完成应用的多屏适配。
  * **[多屏UI模拟器](</vela/quickapp/zh/guide/multi-screens/simulator.html>)：** AIoT-IDE提供了多屏UI模拟器，使开发者能够快速预览应用在不同屏幕上的效果，进行必要的调整。
  * **[适配案例](</vela/quickapp/zh/guide/multi-screens/samples.html>)：** 提供了对常见页面元素进行多屏适配的代码示例以及整站案例，供开发者参考和学习。

## # 应用开发流程

### # 环境搭建

小米提供了包括AIoT-IDE在内的一系列开发工具，支持开发者在Ubuntu、Windows、MacOS等操作系统上进行Xiaomi Vela JS 应用的开发和调试。 AIoT-IDE是Xiaomi Vela JS 应用的集成开发环境，提供了项目初始化、编码、调试等一系列功能。请参考[安装环境](</vela/quickapp/zh/guide/start/use-ide.html>)初始化项目。

### # 应用开发

初始化项目后请参考[项目结构](</vela/quickapp/zh/guide/start/project-overview.html>)了解项目中各文件和目录的作用。项目由配置文件（manifest.json）、模板代码（ux文件）、 样式代码（css文件）、逻辑代码（js文件）以及资源文件（图片、音频等）组成。请参考[项目配置](</vela/quickapp/zh/guide/framework/manifest.html>)对项目相关信息进行配置。

应用开发范式遵循声明式UI，和传统Web开发范式类似。项目中的页面以及组件均由`ux`后缀文件编写，文件由[template 模板](</vela/quickapp/zh/guide/framework/template/>)、[style 样式](</vela/quickapp/zh/guide/framework/style/>)和[script 脚本](</vela/quickapp/zh/guide/framework/script/>)3 个部分组成。开发者可以通过编写`ux`文件使用[UI组件](</vela/quickapp/zh/components/>)、[自定义组件](</vela/quickapp/zh/guide/framework/template/component.html>)和样式描述页面结构和呈现效果，使用js脚本定义页面数据、实现生命周期接口、通用方法、事件处理等。 请参考[编写页面UI](</vela/quickapp/zh/guide/start/user-interface.html>)进一步了解页面开发。

### # 运行调试

AIoT-IDE提供内置的模拟器，支持开发者启动模拟器在IDE中直接运行和调试应用，实时查看运行效果。请参考[运行调试](</vela/quickapp/zh/guide/start/use-ide.html#_5-运行项目.html>)了解如何运行和调试应用。

### # 打包发布

应用开发完成后，开发者可以使用AIoT-IDE提供的打包功能将应用打包成安装包，请参考[打包项目](</vela/quickapp/zh/guide/start/use-ide.html#_7-打包项目.html>)了解如何打包应用。项目打包成功后请参考[发布](</vela/quickapp/zh/guide/publish/>)进行应用发布。
