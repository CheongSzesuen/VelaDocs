<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/span.html -->

# span

## 概述

格式化的文本，只能作为[`<text>`](</vela/quickapp/zh/components/basic/text.html>)、[`<a>`](</vela/quickapp/zh/components/basic/a.html>)和`<span>`的子组件。

## 子组件

仅支持`<span>`

## 属性

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
id | `<string>` |:---:| 否 | 唯一标识  
style | `<string>` |:---:| 否 | 样式声明  
class | `<string>` |:---:| 否 | 引用样式表  
for | `<array>` |:---:| 否 | 根据数据列表，循环展开当前标签  
if | `<boolean>` |:---:| 否 | 根据数据 boolean 值，添加或移除当前标签  
  
## 样式

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
color | `<color>` | rgba(0, 0, 0, 0.54) | 否 | 文本颜色  
font-size | `<length>` | 30px | 否 | 文本尺寸  
font-style | normal | italic | normal | 否 | -  
font-weight | normal | bold | `<number>` | normal | 否 | 当前平台仅支持`normal`与`bold`两种效果，当值为数字时，低于`550`为前者，否则为后者  
text-decoration | underline | line-through | none | none | 否 | -  
  
## 事件

不支持

## 示例代码
```html
< template > < div > < text > < span > I am span, </ span > < span style = " color : #f76160 " > I am span, </ span > < span style = " color : #f76160 ; text-decoration : underline ; " > I am span, </ span > </ text > </ div > </ template >
```

![](../../data:image/png;base64,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)
