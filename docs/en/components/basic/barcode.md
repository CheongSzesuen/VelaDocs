<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/barcode.html -->

# barcode2+

## Overview

Barcode, which converts text content into a barcode for display.

## Subcomponents

Not supported

## Attributes

Supports [universal attributes](</vela/quickapp/en/components/general/properties.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
value | `string` |:---:| Yes | Barcode content, using Code128 encoding, with a length of up to 20 bytes  
  
## Styles

Supports [universal styles](</vela/quickapp/en/components/general/style.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
color | `<color>` | #000000 | No | Barcode color  
background-color | `<color>` | #ffffff | No | Barcode background color  
  
Note

  * When setting the rotate property of transform, this component can only be rotated to a vertical or horizontal state;
  * When setting the scale property of transform, this component only supports integer scaling.

## Events

Supports [universal events](</vela/quickapp/en/components/general/events.html>)

## Example Code
```html
< template > < div > < barcode value = " barcodetest " style = " color : #008cff ; " > </ barcode > </ div > </ template >
```

![](../../images/barcode.png)
