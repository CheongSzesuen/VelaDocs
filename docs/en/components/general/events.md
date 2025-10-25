<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/general/events.html -->

# Common Events

Common events are the event callbacks supported by all components.

Developers can register callback events on component tags using `on{eventName}` (e.g., `onclick`) or `@{eventName}` (e.g., `@click`).

For more detailed explanations, refer to the [Event Binding](</vela/quickapp/en/guide/framework/template/event.html>) documentation.

## Example Code
```html
< template > < div > < text onclick = " clickFunction1 " > line 1 </ text > < text @click = " clickFunction2 " > line 2 </ text > </ div > </ template >
```

## List of Common Events

Name | Parameters | Description | Bubbling  
---|:---:|---|---  
touchstart | TouchEvent | Triggered when a finger first touches the component | Supported  
touchmove | TouchEvent | Triggered when a finger moves after touching the component | Supported  
touchend | TouchEvent | Triggered when a finger ends the touch action | Supported  
click | MouseEvent | Triggered when the component is clicked | Supported  
longpress | MouseEvent | Triggered when the component is long-pressed | Supported  
swipe | { direction: <`"left"` | `"right"` | `"up"` | `"down"`> } | Triggered after a quick swipe on the component (not triggered when there is a scrollbar in the swipe direction)  
Parameter description:  
left: swipe left;  
right: swipe right;  
up: swipe up;  
down: swipe down; | Not Supported  
  
## Event Objects

### 1\. TouchEvent Type Description:

Property | Type | Description  
---|:---:|---  
touches | TouchList | Touch event, an array of touch point information currently on the screen  
changedTouches | TouchList | Touch event, an array of changed touch point information. The data format of changedTouches is the same as touches, representing the changed touch points, such as from none to present (touchstart), position change (touchmove), from present to none (touchend),  
For example, when the user's finger leaves the screen, there is no data in the touches array, while changedtouches will save the data before leaving  
  
**Where, TouchList is a collection of Touch objects.**

### 2\. Touch Type Description

Property | Type | Description  
---|:---:|---  
identifier | number | The identifier of the touch point. For multi-point simultaneous touch, it is [0,1,2,3,...], representing the first finger, second finger...  
During a touch action (from finger press to finger release), this identifier remains unchanged and can be used to determine if it is the same touch process  
clientX | number | The X-axis coordinate from the left edge of the visible area, excluding any scroll offset  
clientY | number | The Y-axis coordinate from the top edge of the visible area, excluding any scroll offset and the height of the status bar and titlebar  
pageX | number | The X-axis coordinate from the left edge of the visible area, including any scroll offset  
pageY | number | The Y-axis coordinate from the top edge of the visible area, including any scroll offset. (Excluding the height of the status bar and titlebar)  
offsetX | number | The distance from the left edge of the event trigger object along the X-axis  
offsetY | number | The distance from the top edge of the event trigger object along the Y-axis  
  
### 3\. MouseEvent Type Description

Property | Type | Description  
---|:---:|---  
clientX | number | The X-axis coordinate from the left edge of the visible area, excluding any scroll offset  
clientY | number | The Y-axis coordinate from the top edge of the visible area, excluding any scroll offset and the height of the status bar and titlebar  
pageX | number | The X-axis coordinate from the left edge of the visible area, including any scroll offset  
pageY | number | The Y-axis coordinate from the top edge of the visible area, including any scroll offset. (Excluding the height of the status bar and titlebar)  
offsetX | number | The distance from the left edge of the event trigger object along the X-axis  
offsetY | number | The distance from the top edge of the event trigger object along the Y-axis  
  
## Example

Below, click and touchmove events are bound to a div, and the events are printed when triggered.
```html
< template > < div class = " root-page " > < div class = " touch-region " onclick = " click " ontouchmove = " move " > </ div > </ div > </ template > < style > .root-page { flex-direction : column ; align-items : center ; } .touch-region { width : 80% ; height : 20% ; background-color : #444444 ; } </ style > < script > export default { private : { } , click (event) { console.log ("click event fired") } , move (event) { console.log ("move event touches:" \+ JSON.stringify (event.touches)) console.log ("move event changedTouches:" \+ JSON.stringify (event.changedTouches)) } } </ script >
```

**The printed results are as follows, for the click event** :
```js
move event touches : [ { "offsetX" : 296 , "identifier" : 0 , "offsetY" : 113.48148345947266 , "clientY" : 113.48148345947266 , "clientX" : 360 , "pageY" : 113.48148345947266 , "pageX" : 360 } ]
```

```js
move event changedTouches : [ { "offsetX" : 296 , "identifier" : 0 , "offsetY" : 113.48148345947266 , "clientY" : 113.48148345947266 , "clientX" : 360 , "pageY" : 113.48148345947266 , "pageX" : 360 } ]
```

``` click event fired
```
