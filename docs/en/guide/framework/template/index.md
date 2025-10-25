<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/ -->

# Template

A tag language similar to `HTML` that combines basic components and events to build the structure of a page.

Note

There can only be one root node in the template, such as `div`. Please do not have multiple root nodes under `<template>`, and do not use `block` as the root node.

## Data Binding
```html
< template > < text > {{message}} </ text > </ template > < script > export default { // The data model of the page-level component affects the override mechanism of the incoming data: properties defined within `private` are not allowed to be overridden. private : { message : 'Hello' } } </ script >
```

## Event Binding
```html
< template > < div > <!-- Normal format --> < text onclick = " press " > </ text > <!-- Shorthand --> < text @click = " press " > </ text > </ div > </ template > < script > export default { press (e) { this.title = 'Hello' } } </ script >
```

Supported syntax for event callbacks (where `{{}}` can be omitted):

**fn** : `fn` is the name of the event callback function (with corresponding function implementation in `<script>`);

**fn(a,b)** : Function parameters such as `a`, `b` can be constants or data variables defined in `<script>` (no need to write `this` before them);

When the callback function is called, an `evt` parameter will be automatically added at the end of the parameter list. You can access the context data related to the callback event through the `evt` parameter (refer to the component callback event description for specific data content), such as the click position `x`, `y` of a click event.

## List Rendering
```html
< template > < div > < div for = " {{list}} " tid = " uniqueId " > < text > {{$idx}} </ text > < text > {{$item.uniqueId}} </ text > </ div > </ div > </ template > < script > export default { // The data model of the page-level component affects the override mechanism of the incoming data: properties defined within `private` are not allowed to be overridden. private : { list : [ { uniqueId : 1 } , { uniqueId : 2 } ] } } </ script >
```

The `for directive` renders a list based on the source data array. The supported syntax is as follows (where `{{}}` can be omitted):

  * `for="{{list}}"` `list` is the source data array, and the default array element name is `$item`;
  * `for="{{value in list}}"` `value` is a custom array element name, and the default array element index name is `$idx`;
  * `for="{{(index, value) in list}}"` `index` is a custom array element index name, and `value` is a custom array element name.

The `tid attribute` of the `for directive` is used to specify the unique ID of the array element. If not specified, the array index (`$idx`) is used as the unique ID by default. The purpose of the `tid attribute` is to reuse element nodes and optimize the redraw efficiency of the for loop.

In the example code, `tid="uniqueId"` means that the array element `$item.uniqueId` of the array `list` is used as the unique ID of the array element, and it must be ensured that the value of the `uniqueId` property is different for each array element.

When using the `tid attribute`, pay attention to the following:

  * The data attribute specified by the `tid attribute` must exist, otherwise it may cause runtime exceptions;
  * The data attribute specified by the `tid attribute` must be unique, otherwise it may cause performance issues;
  * The `tid attribute` currently does not support expressions.

## Conditional Rendering

There are two types: `if/elif/else` and `show`. The difference is that when `if` is `false`, the component will be removed from the VDOM, while `show` is just invisible during rendering, and the component still exists in the VDOM;

`if/elif/else` nodes must be adjacent sibling nodes, otherwise they cannot pass compilation.
```html
< template > < div > < text if = " {{display}} " > Hello-1 </ text > < text elif = " {{display}} " > Hello-2 </ text > < text else > Hello-3 </ text > </ div > </ template > < script > export default { // The data model of the page-level component affects the override mechanism of the incoming data: properties defined within `private` are not allowed to be overridden. private : { display : false } } </ script >
```

`show` is equivalent to `visible=none`, mainly used for declaration on native components;
```html
< template > < text show = " {{visible}} " > Hello </ text > </ template > < script > export default { // The data model of the page-level component affects the override mechanism of the incoming data: properties defined within `private` are not allowed to be overridden. private : { visible : false } } </ script >
```

## Logical Control Block

You can use `<block>` to achieve more flexible loop/conditional rendering. Note that `<block>` currently only supports the `for` and `if/elif/else` attributes. If no attributes are specified, `<block>` will be treated as a `transparent` node during construction, and its child nodes will be added to the parent node of `<block>`.
```html
< template > < list > < block for = " cities " > < list-item type = " city " > < text > {{$item.name}} </ text > </ list-item > < list-item type = " spot " for = " $item.spots " > < text > {{$item.address}} </ text > </ list-item > </ block > </ list > </ template > < script > export default { // The data model of the page-level component affects the override mechanism of the incoming data: properties defined within `private` are not allowed to be overridden. private : { cities : [ { name : 'beijing' , spots : [ { address : 'XXX' } ] } , { name : 'shanghai' , spots : [ { address : 'XXX' } , { address : 'XXX' } ] } ] } } </ script >
```
