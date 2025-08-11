<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/ -->

# # 框架简介

本应用框架是一套以前端开发技术栈为主进行应用开发的框架，采用流行的前端开发模式，贴合主流前端开发者的思维习惯，同时大幅提升应用的性能，提供大量前端环境无法使用的系统能力，以及很多第三方服务的对接能力。

## # 文件结构

应用由一个 manifest.json 和多个页面 ux 文件组成。manifest.json 文件中定义应用描述、功能权限声明、系统配置和页面路由等信息；页面 ux 文件中完成单个页面的具体实现，包括 UI 模板、样式单、数据定义和回调事件处理等。具体使用参看[项目结构](</vela/quickapp/zh/guide/framework/project-structure.html>)。

## # 应用框架

### # 路由管理

框架负责管理整个应用的页面路由，实现页面间的无缝切换，管理每个页面的完整生命周期。开发者需要将页面在 manifest.json 中进行注册，在代码中通过框架提供的接口方法实现页面的切换。具体使用参看[项目配置](</vela/quickapp/zh/guide/framework/manifest.html>)、[页面切换](</vela/quickapp/zh/guide/framework/page-switch.html>)。

### # 数据绑定

数据绑定可以让数据与视图非常简单地保持同步。当做数据修改的时候，只需要在逻辑层修改数据，视图层就会做相应的更新。数据绑定的具体使用参看[模板语法](</vela/quickapp/zh/guide/framework/template/>)。

### # 界面组件

框架提供了一套基础的界面组件，界面组件标签除了支持常用的 HTML5 标签，例如`<div>，<input>`等之外，还提供与原生 UI 相关的组件标签，例如`<switch>，<slider>，<list>`等。具体使用参看[组件](</vela/quickapp/zh/components/>)。

### # 原生接口

框架还提供丰富的原生接口，既有通用的系统功能，也有第三方服务的对接，如网络请求、本地存储等等。这些 API 可以大大节省开发者工作量，快速开发出应用。具体使用参看[接口](</vela/quickapp/zh/features/>)。
