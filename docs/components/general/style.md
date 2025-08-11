<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/general/style.html -->

# 通用样式

通用样式，即所有组件都可以支持的样式。

它们均与 css 的属性样式用法保持一致，开发者可写在`内联样式`或`<style>`标签里，实现组件样式的定制化。

关于组件样式的设置，可以参考此[文档](</vela/quickapp/zh/guide/framework/style/page-style-and-layout.html>)。

## 示例代码
```html
< template > < div class = " page " > < div class = " box-normal " style = " background-color : #f76160 " > </ div > < div class = " box-normal " > </ div > </ div > </ template > < style > .page { padding : 30px ; background-color : white ; } .box-normal { background-color : #09ba07 ; width : 100px ; height : 100px ; border-radius : 8px ; margin-right : 10px ; } </ style >
```

![](../../data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANYAAABsCAIAAACZ0NtqAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADQElEQVR4nO3YMU8acRjHcY5ra0xYNKyoocPRgc1R2bwRfCE6thJoJ2yj7agvhHY8N2R0Yyg3aFRWoosJsQaug9erWsLRRu/nP/1+Jg6O5MmTb47jrCAIUoBOWj0A/nckCDEShNiLP98a9ftDzxv53aDXS36gZ8XK5dJOwXbddDb7D18/G5zun++1Llqdq86jz2aWYqZYmi9tLGwuzi49+Mh68Hfkptkcfvua3GiGsMuVl+vrf/WV7ePGp5OPTzSPuWr5+vvXH+6+cy/B692dwPcTn8oMluPMbFWnPNk9WmtfHj7pPOZamVv1lg+iw9/3gjfNJv1NEPj+TbM5zZnbxw36m6B9ebh93IgOw6vgqN/8e6tbipjvPr8ZfJ94dng9E27kNg85vq+0r29LwyvgkPPU45jjthF7Z/vJTOJ6aJFhQmO/K5uGJPELqp10UpmEtNFiwoT5PnLlGIXxfOXKUWL4tE0xEgQYiQIMRKEGAlCjAQhRoIQI0GIkSDESBBiJAgxEoQYCUKMBCFGghAjQYiRIMRIEGIkCDEShBgJQowEIUaCECNBiJEgxEgQYiQIMRKEGAlCjAQhRoIQI0GIkSDESBBiJAgxEoQYCUKMBCFGghAjQYiRIMRIEGIkCDEShBgJQowEIUaCECNBiJEgxEgQYiQIMRKEGAlCjAQhRoIQI0GIkSDESBBiJAgxEoQYCUKMBCFGghAjQYiRIMRIEGIkCDEShBgJQowEIUaCECNBiJEgxEgQYiQIMRKEGAlCjAQhRoIQI0GIkSDESBBiJAgxEoQYCUIsTNDK5bRzmCJ2UcVMMZlJTBctKkww7RR0w5gkdlGl+VIyk5guWlSYoO26umFMEruojYXNZCYxXbSoX1fBbNYuV3TzmMEuV9LZ7ORzFmeXavl6MvOYq5avL84u3b62giCIPrje3Ql8XzPUs2c5zsxWdcqT3aO19uXhk85jrpW5VW/5IDq89494ZqvKtXAsu1yZvr9UKuUtH3AtHKuWr9/tL/XgKnhr1O8PPW/kd4NeL8HZniMrl0s7Bdt1Y39/xzobnO6f77UuWp2rzqPPZpZipliaL20sbEa/v5ExCQJJ4tE0xEgQYiQIsZ83RLmJu++FMQAAAABJRU5ErkJggg==)

## 属性列表

**注** ：通用样式均为非必填项。

名称 | 类型 | 默认值 | 描述  
---|:---:|---|---  
width | `<length>` | `<percentage>` |:---:| 未设置时使用组件自身内容需要的宽度  
height | `<length>` | `<percentage>` |:---:| 未设置时使用组件自身内容需要的高度  
min-width | auto | `<length>` | `<percentage>` | auto | 指定元素的最小宽度。该属性不能为负值，默认值 `auto` 为弹性元素的默认最小宽度，下同  
min-height | auto | `<length>` | `<percentage>` | auto | 指定元素的最小高度  
max-width | none | `<length>` | `<percentage>` | none | 指定元素的最大宽度。该属性不能为负值，默认值 `none` 表示不做限制，下同  
max-height | none | `<length>` | `<percentage>` | none | 指定元素的最大高度  
padding | `<length>` | 0 | 简写属性，在一个声明中设置所有的内边距属性，该属性可以有 1 到 4 个值，具体请参考[MDN (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding>)文档  
padding-[left|top|right|bottom] | `<length>` | 0 | 设置一个元素的某个方向的内边距，padding 区域指一个元素的内容和其边界之间的空间，该属性不能为负值  
margin | `<length>` | 0 | 简写属性，在一个声明中设置所有的外边距属性，该属性可以有 1 到 4 个值，具体请参考[MDN (opens new window)](<https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin>)文档  
margin-[left|top|right|bottom] | `<length>` | 0 | 设置一个元素的某个方向的外边距，该属性不能为负值  
border |:---:| 0 | 简写属性，在一个声明中设置所有的边框属性，可以按顺序设置属性 width style color，不设置的值为默认值  
border-style | solid | solid | 暂时仅支持 1 个值，为元素的所有边框设置样式  
border-width | `<length>` | 0 | 设置元素的所有边框宽度  
border-color | `<color>` | black | 设置元素的所有边框颜色，颜色值的填入请参考 [颜色配置](</vela/quickapp/zh/components/general/color.html>)  
border-radius | `<length>` | `<percentage>` | 0 | border-radius 属性允许你设置元素的外边框圆角。设置时需要同时设置 border-width、border-color。radius 的幅度不会超过矩形较短边的一半  
background-color | `<color>` |:---:| 颜色值的填入请参考 [颜色配置](</vela/quickapp/zh/components/general/color.html>)  
color | `<color>` |:---:| 颜色值的填入请参考 [颜色配置](</vela/quickapp/zh/components/general/color.html>)  
background-image | `<uri>` |:---:| 支持本地图片资源与网络图片资源；使用`internal://`协议图片需将aiot-toolkit升级到1.1.2以上版本  
background-size | contain | cover | auto | `<length>` | `<percentage>` | auto auto | 设置背景图片大小，详情见[背景图样式](</vela/quickapp/zh/components/general/background-img-styles.html>)  
background-repeat | repeat | repeat-x | repeat-y | no-repeat | repeat | [暂不支持] 设置是否及如何重复绘制背景图像，详情见[背景图样式](</vela/quickapp/zh/components/general/background-img-styles.html>)  
background-position | `<length>` |`<percentage>`| left | right | top | bottom | center | 0px 0px | 设置背景图片在容器中绘制的位置，支持 1-4 个参数，详情见[背景图样式](</vela/quickapp/zh/components/general/background-img-styles.html>)  
box-shadow [3+](</vela/quickapp/zh/guide/version/APILevel3>) | `<length>` `<length>` `<color>` |  
`<length>` `<length>` `<length>` `<color>` |  
`<length>` `<length>` `<length>` `<length>` `<color>`  
|:---:| 设置元素的阴影效果，该属性可设置的值包括阴影的 X 轴偏移量、Y 轴偏移量、模糊半径、扩散半径和[颜色](</vela/quickapp/zh/components/general/color.html>)。  
写法举例：  
box-shadow: 60px -16px teal，值分别对应：x轴偏移量、y轴偏移量、[阴影颜色](</vela/quickapp/zh/components/general/color.html>)；  
box-shadow: 10px 5px 5px black，值分别对应：x轴偏移量、y轴偏移量、阴影模糊半径、[阴影颜色](</vela/quickapp/zh/components/general/color.html>)；  
box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2)，值分别对应：x轴偏移量、y轴偏移量、阴影模糊半径、阴影扩散半径、[阴影颜色](</vela/quickapp/zh/components/general/color.html>)  
opacity | `<number>` | 1 | opacity 属性指定了一个元素的透明度  
display | flex | none | flex | JS 应用只支持 flex 布局；将当前元素的 display 设置为 none JS 应用页面将不渲染此元素  
visibility | visible | hidden | visible | visibility 属性控制显示或隐藏元素而不更改文档的布局  
flex | `<number>` |:---:| 父容器为`<div>、<list-item>`时生效  
flex-grow | `<number>` | 0 | 父容器为`<div>、<list-item>`时生效  
flex-shrink | `<number>` | 1 | 父容器为`<div>、<list-item>`时生效  
flex-basis | `<number>` | -1 | 父容器为`<div>、<list-item>`时生效  
flex-direction | `<string>` | row | 默认为横向`row`，父容器为`<div>、<list-item>`时生效  
align-items | `<string>` | flex-start | align-items 定义了伸缩项目可以在伸缩容器的当前行的侧轴上对齐方式。flex-start(默认值)：伸缩项目在侧轴起点边的外边距紧靠住该行在侧轴起始的边。flex-end：伸缩项目在侧轴终点边的外边距靠住该行在侧轴终点的边 。center：伸缩项目的外边距盒在该行的侧轴上居中放置。baseline：伸缩项目根据他们的基线对齐。stretch：伸缩项目拉伸填充整个伸缩容器。此值会使项目的外边距盒的尺寸在遵照「min/max-width/height」属性的限制下尽可能接近所在行的尺寸  
justify-content | `<string>` | flex-start | justify-content 定义了伸缩项目沿着主轴线的对齐方式。flex-start(默认值)：伸缩项目向一行的起始位置靠齐。flex-end：伸缩项目向一行的结束位置靠齐。center：伸缩项目向一行的中间位置靠齐。space-between：伸缩项目会平均地分布在行里。第一个伸缩项目一行中的最开始位置，最后一个伸缩项目在一行中最终点位置。space-around：伸缩项目会平均地分布在行里，两端保留一半的空间  
position | absolute | relative | relative | 支持 relative 和 absolute 属性值，且默认值为 relative；父容器为`<list>、<swiper>`时不生效  
[left|top|right|bottom] | `<length>` |:---:| 一般配合`absolute`布局使用，支持单位px，暂不支持百分比
