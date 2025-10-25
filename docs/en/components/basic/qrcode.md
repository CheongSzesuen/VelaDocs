<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/qrcode.html -->

# qrcode2+

## Overview

Generates and displays a QR code.

## Child Components

Not supported

## Attributes

Supports [common attributes](</vela/quickapp/en/components/general/properties.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
value | `string` |:---:| Yes | The content used to generate the QR code  
  
## Styles

Supports [common styles](</vela/quickapp/en/components/general/style.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
color | `<color>` | #000000 | No | QR code color  
background-color | `<color>` | #ffffff | No | QR code background color  
  
## Events

Supports [common events](</vela/quickapp/en/components/general/events.html>)

## Example Code
```html
< template > < div > < qrcode value = " https://iot.mi.com " style = " color : #008cff ; " > </ qrcode > </ div > </ template >
```

![](../../images/qrcode.png)
