<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/general/animation-style.html -->

# # 动画样式

Vela JS 应用支持开发者制作动画，提供了`transform`类、`transform-origin`类、`animation`类与`transition`类的动画样式属性，且参数格式与 CSS 对齐，更方便开发者上手适配动画。

`transform`可参考此[文档 (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform>)。

`transform-origin`可参考此[文档 (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform-origin>)。

`animation`可参考此[文档 (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation>)。

`transition` 可参考此[文档 (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition>)。

## # 动画样式列表

名称 | 类型 | 默认值 | 描述  
---|---|---|---  
transform | `<string>` | - | 见下面 transform 操作  
transform-origin | `<string>` | - | 见下面 transform-origin 操作  
animation-name | `<string>` | - | 与@keyframes 的 name 相呼应，见下面@keyframes 属性  
animation-delay | `<time>` | 0 | 目前支持的单位为[ s(秒) | ms(毫秒) ]  
animation-duration | `<time>` | 0 | 目前支持的单位为[ s(秒) | ms(毫秒) ]  
animation-iteration-count | `<integer>` | `infinite` | 1 | 定义动画播放的次数，可设置为`infinite`无限次播放  
animation-timing-function | linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?) | ease | -  
transition-property | `<string>` | all | 指定执行 transition 效果的通用样式属性名称，参见详情  
transition-duration | `<time>` | 0s | 指定 transition 执行时间  
transition-timing-function | linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?) | ease | 指定 transition 执行时的时间函数。该参数释义与 animation 相同  
transition-delay | `<time>` | 0s | 指定 transition 开始执行的时间，即当改变元素属性值后多长时间开始执行 transition 效果  
  
**注** ：

  * animation-timing-function 类型

cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number_of_steps[, step-direction]?)其中：

steps(number_of_steps，step-direction)

名称 | 类型 | 默认值  | 必填  | 描述  
---|---|---|---|---  
number_of_steps | `<integer>` | - | 是 | 表示等间隔步数的正整数  
step-direction | jump-start | jump-end | jump-none | jump-both | start | end | end | 否 | 指示函数左连续或右连续的关键字  
  
  * cubic-bezier(x1, y1, x2, y2)

参数 x1, y1, x2, y2 是 `<number>` 类型的值，代表当前定义的立方贝塞尔曲线中的 P1 和 P2 点的横坐标和纵坐标，x1 和 x2 必须在 [0，1] 范围内，否则当前值无效。

## # transform 操作

向元素应用 2D 转换。该属性允许我们对元素进行旋转、缩放、移动。 支持的样式属性列表如下：

名称 | 类型  
---|---  
translate | `<length>` | `<percent>`  
translateX | `<length>` | `<percent>`  
translateY | `<length>` | `<percent>`  
scale | `<number>`  
scaleX | `<number>`  
scaleY | `<number>`  
rotate | `<deg>`  
  
## # transform-origin 操作

更改一个元素变形的原点，目前支持改变元素的 X 和 Y 轴。

**注意：**

  * 使用此属性必须先使用 transform 属性。

示例代码：

``` /* 使用 % 值 */ div { transform: rotate(30deg); transform-origin: 20% 40%; } /* 使用 px 值 */ div { transform: rotate(30deg); transform-origin: 100px 100px; } ```

## # animation-name 属性

指定所采用的一系列动画，属性值的每个名称代表一个由 @keyframes 属性定义的关键帧序列。该属性支持在组件中应用单个动画或多个动画 `1070+` ，应用多个动画时动画同时开始执行。

示例代码：

``` /* 单个动画 */ animation-name: Color; animation-name: translate; animation-name: rotate; /* 多个动画 1070+ */ animation-name: Color, Opacity; animation-name: Width, translate, rotate; ```

## # @keyframes 属性

名称 | 类型 | 默认值 | 描述  
---|---|---|---  
background-color | `<color>` | - | -  
background-position | `<length>` |`<percentage>`| left | right | top | bottom | center | 0px 0px | 描述了背景图片在容器中绘制的位置，支持 1-4 个参数，详情见[背景图样式](</vela/quickapp/zh/components/general/background-img-styles.html>)  
opacity | `<number>` | - | -  
width/height | `<length>` | - | 暂不支持百分比  
transform | `<string>` | - | 可以对元素进行旋转、缩放、移动  
  
**注** ：

暂时不支持起始值(0%)或终止值(100%)缺省的情况，都需显式指定。

## # transition 过渡动画

transition 过渡动画是实现动画的另一种方式。过渡动画可以为元素定义在不同状态之间切换时的过渡效果，比如通过 JavaScript 实现的状态变化。

### # transition 使用示例

共 4 个样式属性：transition-property、transition-duration、transition-timing-function、transition-delay，直接写在样式当中，使用示例如下：

``` <template> <div class="page"> <div class="div {{otherClass}}"></div> </div> </template> <script> export default { data: { otherClass: "" }, onShow() { const that = this setTimeout(() => { that.otherClass = "new-width" }, 1000); } }; </script> <style> .page { padding: 60px; align-items: center; } .div { width: 100px; height: 200px; background-color: red; transition-property: width; transition-duration: 2000ms; transition-timing-function: ease-in; transition-delay: 500ms; } .new-width { width: 300px; } </style> ```

上述 4 个样式属性可简写到一个中，表示当触发 div 的 width 变化后 0.5s，以加速的方式变化至新的 width 值，过渡动画持续 2s：

``` .div { transition: width 2000ms ease-in 500ms; } ```

### # transition-property 支持的通用样式属性

JS 应用中 transition-property 支持的通用样式属性列表如下：

样式名称 | 备注  
---|---  
width | √  
height | √  
opacity | √  
visibility | √  
color | 暂不支持  
transform-origin | 暂不支持  
transform | 暂不支持  
padding | 暂不支持  
padding-[left|top|right|bottom] | 暂不支持  
margin | 暂不支持  
margin-[left|top|right|bottom] | 暂不支持  
border | 暂不支持  
border-[left|top|right|bottom] | 暂不支持  
border-width | √  
border-[left|top|right|bottom]-width | 暂不支持  
border-color | √  
border-[left|top|right|bottom]-color | 暂不支持  
border-radius | 暂不支持  
border-[top|bottom]-[left|right]-radius | 暂不支持  
background | 暂不支持  
background-color | √  
background-size | 暂不支持  
background-position | √  
flex | 暂不支持  
flex-grow | 暂不支持  
flex-shrink | 暂不支持  
flex-basis | 暂不支持  
[left|top|right|bottom] | 暂不支持
