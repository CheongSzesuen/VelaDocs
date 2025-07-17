<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/qrcode.html -->

# # qrcode[2+](</vela/quickapp/zh/guide/version/APILevel2>)

## # 概述

生成并显示二维码。

## # 子组件

不支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
value | `string` | - | 是 | 用来生成二维码的内容  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
color | `<color>` | #000000 | 否 | 二维码颜色  
background-color | `<color>` | #ffffff | 否 | 二维码背景颜色  
  
## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div> <qrcode value="https://iot.mi.com" style="color: #008cff;"></qrcode> </div> </template> ```

![](../../data:image/png;base64,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)

← [ chart ](</vela/quickapp/zh/components/basic/chart.html>) [ barcode ](</vela/quickapp/zh/components/basic/barcode.html>) → 

快速导航

概述

子组件

属性

样式

事件

示例代码
