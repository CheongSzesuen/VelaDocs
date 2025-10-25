<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/container/stack.html -->

# stack

## Overview

A basic container that stacks its direct child components in a layered manner, with each subsequent child component covering the previous one.

## Child Components

Supported

## Properties

Supports [general properties](</vela/quickapp/en/components/general/properties.html>)

## Styles

Supports [general styles](</vela/quickapp/en/components/general/style.html>)

## Events

Supports [general events](</vela/quickapp/en/components/general/events.html>)

## Example Code
```html
< template > < div class = " page " > < stack class = " stack " > < div class = " box box1 " > </ div > < div class = " box box2 " > </ div > < div class = " box box3 " > </ div > < div class = " box box4 " > </ div > </ stack > </ div > </ template > < style > .page { padding : 30px ; background-color : white ; } .box { border-radius : 8px ; width : 100px ; height : 100px ; } .box1 { width : 200px ; height : 200px ; background-color : #3f56ea ; } .box2 { left : 20px ; top : 20px ; background-color : #00bfc9 ; } .box3 { left : 50px ; top : 50px ; background-color : #47cc47 ; } .box4 { left : 80px ; top : 80px ; background-color : #FF6A00 ; } </ style >
```

![](../../images/stack.png)
