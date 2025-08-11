<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/barcode.html -->

# # barcode[2+](</vela/quickapp/zh/guide/version/APILevel2>)

## # 概述

条形码，将文本内容转换为条形码展示。

## # 子组件

不支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
value | `string` | - | 是 | 条形码内容，码制为Code128码，长度小于等于20字节  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
color | `<color>` | #000000 | 否 | 条形码颜色  
background-color | `<color>` | #ffffff | 否 | 条形码背景颜色  
  
注意

  * 当设置transform的rotate属性时，该组件只能旋转为垂直或者水平状态；
  * 当设置transform的scale属性时，该组件只能支持整数倍缩放。

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

``` <template> <div> <barcode value="barcodetest" style="color: #008cff;"></barcode> </div> </template> ```

![](../../data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASgAAABMCAIAAABRd722AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABOElEQVR4nO3VQQrCMBRAQev9PXNcKCJtlLrxoZ1ZlZB808LDZYxxAr7rXF8Ajkh4EBAeBIQHAeFBQHgQEB4EhAcB4UFAeBAQHgR+L7zlclou94fHymrDq/Xpwcf6mwm3PdsJr+Y8b5ieffOLq217XnN6t50TVsc/ev3phO3z9lNMr3covxce/AHhQUB4EBAeBIQHAeFBQHgQEB4EhAcB4UFAeBAQHgSEBwHhQUB4EBAeBIQHAeFBQHgQEB4EhAcB4UFAeBAQHgSEBwHhQUB4EBAeBIQHAeFBQHgQEB4EhAcB4UFAeBAQHgSEBwHhQUB4EBAeBIQHAeFBQHgQEB4EhAcB4UFAeBAQHgSWMUZ9Bzgc/3gQEB4EhAcB4UFAeBAQHgSEBwHhQUB4EBAeBIQHAeFBQHgQEB4Erhf9L51U2f+gAAAAAElFTkSuQmCC)
