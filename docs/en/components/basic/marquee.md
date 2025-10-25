<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/marquee.html -->

# marquee

## Overview

Marquee is used to insert a segment of scrolling text. By default, it is a single line.

## Child Components

Not supported

## Attributes

[Common attributes](</vela/quickapp/en/components/general/properties.html>) are supported.

Name | Type | Default Value | Mandatory | Description  
---|:---:|---|:---:|---  
scrollamount | `<number>` | 6 | No | Sets the length of each scroll, in px.  
loop | `<number>` | -1 | No | Sets the number of times that the marquee scrolls. If this parameter is not specified, the default value is −1, indicating that the marquee scrolls continuously.  
direction | `<string>` | left | No | Direction of text scrolling. The value can be **left** or **right**.  
text-offset | `<number>` |:---:| No | Sets the distance between the end of the previous text segment and the start of the next text segment when the marquee is looped. The attribute value is an integer greater than 0, in px.  
  
## Styles

[Common styles](</vela/quickapp/en/components/general/style.html>) are supported.

Name | Type | Default Value | Mandatory | Description  
---|:---:|---|:---:|---  
color | `<color>` | rgba(0, 0, 0, 0.54) | No | Text color.  
font-size | `<length>` | 30px | No | Text size.  
  
## Events

[Common events](</vela/quickapp/en/components/general/events.html>) are supported.

Name | Parameter | Description  
---|:---:|---  
bounce |:---:| Triggered when the marquee scrolls to the end.  
finish |:---:| Triggered when the marquee completes the number of times set by **loop**. This event is valid only when **loop** is greater than 0.  
start |:---:| Triggered when the marquee starts to scroll.  
  
## Methods

Name | Parameter | Description  
---|:---:|---  
start |:---:| Starts scrolling the marquee.  
stop |:---:| Stops scrolling the marquee.  
  
## Example Code
```html
< template > < div > < marquee id = " marquee " scrollamount = {{6}} loop = {{-1}} > scrollamount controls the scrolling speed. The default value is 6 (6 px/s). </ marquee > </ div > </ template > < script > export default { onReady () { this . $element ('marquee') . start () } } </ script >
```

![](../../images/marquee.gif)
