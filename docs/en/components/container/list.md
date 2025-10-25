<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/container/list.html -->

# list

## Overview

A list view container that contains a series of list items with the same structure and presents similar data in a continuous, multiline format.

## Child Components

Only supports [`<list-item>`](</vela/quickapp/en/components/container/list-item.html>)

## Attributes

Supports [universal attributes](</vela/quickapp/en/components/general/properties.html>)

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
bounces | `<boolean>` | false | No | Whether to bounce at the boundary  
  
## Styles

Supports [universal styles](</vela/quickapp/en/components/general/style.html>)

You need to explicitly set the height when using it.

## Events

Supports [universal events](</vela/quickapp/en/components/general/events.html>)

Name | Parameters | Description  
---|:---:|---  
scroll | {scrollX: `<number>`, scrollY: `<number>`, scrollState: `<stateValue>`} | List scrolling;   
Description of stateValue values:   
0: List stops scrolling   
1: List is scrolling via user gesture   
2: List is scrolling, user has released hand  
scrollbottom |:---:| List scrolls to the bottom  
scrolltop |:---:| List scrolls to the top  
scrollend |:---:| List scrolling ends  
scrolltouchup |:---:| Finger lifts during list scrolling  
  
## Example Code
```html
< template > < div class = " page " > < list class = " list " bounces = " true " onscroll = " onScroll " onscrolltop = " onScrollTop " onscrollbottom = " onScrollBottom " onscrolltouchup = " onScrollTouchup " > < list-item for = " {{productList}} " class = " item " type = " item " > < text > {{$item.name}}: {{$item.price}} </ text > </ list-item > </ list > </ div > </ template > < script > export default { private : { productList : [ { name : 'Clothes' , price : '100' } , { name : 'Pants' , price : '200' } , { name : 'Shoes' , price : '300' } , { name : 'Hat' , price : '60' } , { name : 'Umbrella' , price : '300' } , { name : 'Backpack' , price : '60' } , { name : 'Book' , price : '30' } ] , } , onScroll (e) { console.log ('### list onScroll evt: ' , e) } , onScrollTop (e) { console.log ('### list onScrollTop evt: ' , e) } , onScrollBottom (e) { console.log ('### list onScrollBottom evt: ' , e) } , onScrollTouchup (e) { console.log ('### list onScrollTouchup evt: ' , e) } } </ script > < style > .page { justify-content : center ; align-items : center ; background-color : #000 ; } .list { width : 300px ; height : 200px ; border : 1px solid #fff ; } text { color : #fff ; } .item { height : 40px ; width : 100% ; align-items : center ; justify-content : center ; border : 1px solid #fff ; } </ style >
```

### Effect Display

![](../../images/list-methods.jpeg)

## Methods

Name | Parameters | Description  
---|:---:|---  
scrollTo | Object | Scrolls the list to the specified item position  
scrollBy | Object | Scrolls the list content by a certain distance  
  
**Parameter description for scrollTo** :

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
index | number | 0 | No | Target item position for list scrolling  
behavior | smooth / instant / auto | auto | No | Whether to scroll smoothly. Supported parameters: smooth (smooth scrolling), instant (instant scrolling). The default value is auto, which has the same effect as instant  
  
**Parameter description for scrollBy** :

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
left | number | 0 | No | Horizontal scrolling distance from the current position, in px. A positive value scrolls left, and a negative value scrolls right. Does not take effect when flex-direction is column or column-reverse  
top | number | 0 | No | Vertical scrolling distance from the current position, in px. A positive value scrolls up, and a negative value scrolls down. Does not take effect when flex-direction is row or row-reverse  
behavior | smooth / instant / auto | auto | No | Whether to scroll smoothly. Supported parameters: smooth (smooth scrolling), instant (instant scrolling). The default value is auto, which has the same effect as instant
