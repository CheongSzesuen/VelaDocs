<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/style/ -->

# # style 样式

用于描述 template 模板的组件样式，决定组件应该如何显示。

样式布局采用 CSS Flexbox（弹性盒）样式，针对部分原生组件，对 CSS 进行了少量的扩充以及修改。

为了解决屏幕适配问题，所有与大小相关的样式（例如 width、font-size）均以基准宽度（默认 480px）为基础，根据实际屏幕宽度进行缩放，例如 width:100px，在 960px 宽度屏幕上，width 实际上为 200px。

## # 文件导入

支持 2 种导入外部文件的方式：

``` <!-- 导入外部文件, 代替style内部样式 --> <style src="./style.css"></style> <!-- 合并外部文件 --> <style> @import './style.css'; .a { } </style> ```

## # 模板内部样式

支持使用 style、class 属性来控制组件的样式：

``` <!-- 内联inline --> <div style="color:red; margin: 10px;"/> <!-- class声明 --> <div class="normal append"/> ```

## # 选择器

支持的选择器有：

选择器 | 样例 | 样例描述  
---|---|---  
.class | .intro | 选择所有拥有 class="intro" 的组件  
#id | #firstname | 选择拥有 id="firstname" 的组件  
tag | div | 选择所有 div 组件  
, | .a, .b | 选择所有 class="a"以及 class="b"的组件  
  
``` <style> /* 单个选择器 */ text { } .class-abc { } #idAbc { } /* 同一样式适应多个选择器 */ .font-text, .font-comma { } </style> ```

## # 选择器优先级

当前样式的选择器的优先级计算保持与浏览器一致，是浏览器 CSS 渲染的一个子集（仅支持：inline, id, class, tag）。

多条 CSS 声明可以匹配到同一个元素 如 div，应用在该元素上的 CSS 声明总体优先级是：inline > #id > .class > tag，这四大类匹配到该元素的多个 CSS 声明，如：`<div id="sample" style="width: 200px;" class="class-div"></div>`，其优先级按照各选择器的权值高低之和来比较。选择器的优先级权值如下：

  * `ID选择器`（例如: #hello）的权值为 10000

  * `类选择器`（例如: .example）的权值为 100

  * `类型选择器`（例如: h1）的权值为 1

css 的优先级计算文档也可以查看[MDN 文档 (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/Specificity>)入门

## # 样式预编译

目前 JS 应用支持`less`与`sass`的预编译，具体教程也可以参考[这里](</vela/quickapp/zh/guide/framework/style/page-style-and-layout.html#引入-less-scss-预编译>)。

``` <!--导入外部文件, 代替style内部样式--> <style lang="less" src="./lessFile.less"></style> <!--合并外部文件--> <style lang="less"> @import './lessFile.less'; .less-font-text, .less-font-comma { font-size: 60px; } </style> ```

快速导航

文件导入

模板内部样式

选择器

选择器优先级

样式预编译
