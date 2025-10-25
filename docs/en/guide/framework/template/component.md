<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/component.html -->

# Components

## Custom Components

When developing pages, developers must use Native components such as `text` and `div`, which are rendered by the Native layer of each platform. If a developer writes all UI parts in a single file's `<template>` for a complex page, the code's maintainability will be low, and modules may become unnecessarily coupled.

To better organize logic and code, a page can be split into multiple modules based on functionality, with each module responsible for one part of the functionality. The page then manages these modules, passing business and configuration data to achieve code separation. This is the significance of custom components.

A custom component is a component written by a developer that is used similarly to Native components and is rendered according to the component's `<template>`. At the same time, development is similar to that of a page, with a ViewModel managing data, events, and methods.

TIP

Since custom components have an independent ViewModel, there is a certain memory overhead. It is not recommended to use them on lightweight devices like watches and bracelets.

**Example** :
```html
< template > < div class = " tutorial-page " > < text class = " tutorial-title " > Custom Component: </ text > < text > {{ say }} </ text > < text > {{ obj.name }} </ text > </ div > </ template > < style lang = " less " > .tutorial-page { flex-direction : column ; padding-top : 20px ; .tutorial-title { font-weight : bold ; } } </ style > < script > // Child component export default { data : { say : 'hello' , obj : { name : 'quickApp' } } , onInit () { console.log ('I am a child component') } } </ script >
```

In custom components, the data model can only use the **data property** , and the data type is **Object**.

### Custom Component Lifecycle:

  * `onInit`: Indicates that the component's ViewModel data is ready and can start using the page's data.
  * `onReady`: Indicates that the component's ViewModel template has been compiled and DOM nodes can be accessed.
  * `onDestroy`: Called when the component is destroyed. Resources should be released, such as timers.

## Importing Components

In Vela, components are imported using the `<import>` tag, as shown in the following code:
```html
< import name = " XXX " src = " XXX " > </ import >
```

The `src` attribute in the `<import>` tag specifies the address of the custom component, and the `name` attribute specifies the **tag name** used to reference the component in the parent component.

**Example** :
```html
< import name = " comp-part1 " src = " ./part1 " > </ import > < template > < div class = " tutorial-page " > < text class = " tutorial-title " > Import Component: </ text > < comp-part1 > </ comp-part1 > </ div > </ template > < style lang = " less " > .tutorial-page { flex-direction : column ; padding : 20px 10px ; } .tutorial-title { font-weight : bold ; } </ style > < script > // Parent component export default { private : { } , onInit () { console.log ('Import component') } } </ script >
```

## Parent-Child Component Communication

### Parent Component Passes Data to Child Component via Props

The parent component passes data to the child component by declaring exposed property names in the child component's `props` attribute and then declaring the data to be passed on the component's reference tag. For details, see the [Props](</vela/quickapp/en/guide/framework/template/Props.html>) section.

**Example** :
```html
<!-- Child component --> < template > < div class = " child-demo " > < text class = " title " > Child Component: </ text > < text > {{ say }} </ text > < text > {{ propObject.name }} </ text > </ div > </ template > < script > export default { props : [ 'say' , 'propObject' ] , onInit () { console.info (` External data: ` , this.say , this.propObject) } } </ script >
```

```html
<!-- Parent component --> < import name = " comp " src = " ./comp " > </ import > < template > < div class = " parent-demo " > < comp say = " {{say}} " prop-object = " {{obj}} " > </ comp > </ div > </ template > < script > export default { private : { say : 'hello' , obj : { name : 'child-demo' } } } </ script >
```

### Child Component Communicates with Parent Component

  * The child component triggers a custom event bound to the node using `$emit()` to execute the parent component's method, as in the relationship between the parent component and Component 1.
  * The child component triggers a custom event using `$dispatch()`, and the parent component monitors the trigger using `$on()`, as in the relationship between the parent component and Component 2.

**Example** :
```html
<!-- Parent component --> < import name = " comp1 " src = " ./comp1.ux " > </ import > < import name = " comp2 " src = " ./comp2.ux " > </ import > < import name = " comp3 " src = " ./comp3.ux " > </ import > < template > < div class = " parent-demo " > < text > I am the parent component count: {{count}} </ text > < comp1 count = " {{count}} " onemit-evt = " emitEvt " > </ comp1 > < text > I am the parent component num: {{num}} </ text > < comp2 num = " {{num}} " > </ comp2 > < text > I am the parent component age: {{age}} </ text > < input type = " button " onclick = " evtTypeEmit " value = " Trigger $broadcast() " > </ input > < comp3 > </ comp3 > </ div > </ template > < script > export default { private : { count : 20 , num : 20 , age : 18 } , onInit () { this . $on ('dispatchEvt' , this.dispatchEvt) } , emitEvt (evt) { this.count = evt.detail.count } , dispatchEvt (evt) { this.num = evt.detail.num } , evtTypeEmit () { this . $broadcast ('broadevt' , { age : 19 }) } , } </ script >
```

```html
<!-- comp1 --> < template > < div class = " child-demo " > < text > I am child component one count: {{compCount}} </ text > < input type = " button " onclick = ' addHandler ' value = ' add ' > </ input > </ div > </ template > < script > export default { props : [ 'count' ] , data () { return { compCount : this.count } } , addHandler () { this.compCount ++ this . $emit ('emitEvt' , { count : this.compCount }) } , } </ script >
```

```html
<!-- comp2 --> < template > < div class = " child-demo " > < text > I am child component two num: {{compNum}} </ text > < input type = " button " onclick = ' delHandler ' value = ' del ' > </ input > </ div > </ template > < script > export default { props : [ 'num' ] , data () { return { compNum : this.num } } , delHandler () { this.compNum \-- this . $dispatch ('dispatchEvt' , { num : this.compNum }) } , } </ script >
```

```html
<!-- comp3 --> < template > < div class = " child-demo " > < text > I am child component three age: {{compAge}} </ text > </ div > </ template > < script > export default { props : [ ] , data () { return { compAge : null } } , onInit () { this . $on ('broadevt' , this.broadevt) } , broadevt (evt) { this.compAge = evt.detail.age } } </ script >
```

The framework provides developers with bidirectional event passing:

  * Downward passing: Triggered by the parent component and responded to by the child component. Use `parentVm.$broadcast()` for downward passing, such as `broadevt`.
  * Upward passing: Triggered by the child component and responded to by the parent component. Use `childVm.$dispatch()` for upward passing, such as `dispatchEvt`.

**Tips** :

  * When passing parameters during triggering, use `evt.detail` to retrieve the parameters.
  * After passing is complete, you can call `evt.stop()` to end the passing; otherwise, it will continue indefinitely.

