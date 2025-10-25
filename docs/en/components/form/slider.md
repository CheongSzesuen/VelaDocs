<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/form/slider.html -->

# slider

## Overview

Slider selector.

## Child Components

Not supported.

## Attributes

Supports [general attributes](</vela/quickapp/en/components/general/properties.html>).

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
min | `<number>` | 0 | No | -  
max | `<number>` | 100 | No | -  
step | `<number>` | 1 | No | -  
value | `<number>` | 0 | No | -  
  
## Styles

Supports [general styles](</vela/quickapp/en/components/general/style.html>).

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
color | `<color>` | #f0f0f0 or rgb(240, 240, 240) | No | Background bar color  
selected-color | `<color>` | #009688 or rgb(0, 150, 136) | No | Selected color  
block-color | `<color>` |:---:| No | Slider block color  
padding-[left|right] | `<length>` | 32px | No | Left and right padding  
  
## Events

Supports [general events](</vela/quickapp/en/components/general/events.html>).

Name | Parameters | Description  
---|:---:|---  
change | {progress:progressValue, isFromUser:isFromUserValue} | Triggered after a drag is completed   
isFromUser description:   
Indicates whether the event was triggered by user dragging  
  
## Example Code
```html
< template > < div class = " page " > < text class = " title " > Slider Component </ text > < slider class = " slider " min = " 0 " max = " 100 " step = " 10 " value = " {{ initialSliderValue }} " onchange = " onSliderChange " > </ slider > < text > Slider value: {{ sliderValue }} </ text > </ div > </ template > < script > export default { private : { initialSliderValue : 10 , sliderValue : null } , onSliderChange (e) { this.sliderValue = e.progress } } </ script > < style > .page { flex-direction : column ; padding : 30px ; background-color : #ffffff ; } .title { font-weight : bold ; } .slider { margin-top : 20px ; margin-bottom : 20px ; padding-left : 0 ; padding-right : 0 ; } </ style >
```

![](../../images/slider.gif)
