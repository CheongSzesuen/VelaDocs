<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/qrcode.html -->

# qrcode2+

## 概述

生成并显示二维码。

## 子组件

不支持

## 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
value | `string` |:---:| 是 | 用来生成二维码的内容  
  
## 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
color | `<color>` | #000000 | 否 | 二维码颜色  
background-color | `<color>` | #ffffff | 否 | 二维码背景颜色  
  
## 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## 示例代码
```html
< template > < div > < qrcode value = " https://iot.mi.com " style = " color : #008cff ; " > </ qrcode > </ div > </ template >
```

![](../../images/qrcode.png)
