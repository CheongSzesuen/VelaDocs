<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/script/global-data-method.html -->

# Global Attributes and Methods

## Objects

### Common Objects

Attribute | Type | Description  
---|:---:|---  
$app | Object | Application object  
$page | Object | Page object  
$valid | Boolean | Whether the page object is valid  
  
#### Application Object

In a page, the global application object can be accessed via `$app`.

In the `app.ux` file, developers can define globally accessible data and methods, which can be accessed in the page via `this.$app.$def`, and directly via `this` in the `app.ux` file. For example, define the following in the `app.ux` file:
```html
< script > /** * Application-level configuration for all pages */ export default { data : { a : 1 } , func : function () { console.log (this.data.a) console.log (` function executed! `) } } </ script >
```

In other pages, you can call them like this:
```javascript
this . $app . $def.data this . $app . $def.func()
```

The following built-in methods can be accessed via `$app`:

Attribute | Type | Description  
---|:---:|---  
exit | Function | Exit the JS application and end the application lifecycle. Usage: `this.$app.exit()`  
  
#### Page Object

In a page, the current page object can be accessed via `this.$page`. The following attributes can be accessed on this object:

Attribute | Type | Description  
---|:---:|---  
name | String | Get the name of the current page route, consistent with the corresponding property name in `router.pages` in the manifest file  
path | String | Get the path of the current page route, consistent with the corresponding path in `router.pages` in the manifest file  
component | String | Get the component of the current page route, consistent with the corresponding component in `router.pages` in the manifest file  
  
## Methods

### this.$canIUse3+

In a page, you can use `this.$canIUse` to query available capabilities, including interfaces and components.

#### Parameters:

Type | Description  
---|---  
String | The capability to query, see the format below  
  
#### Return Value:

Type | Description  
---|---  
Boolean | Whether the queried capability is supported  
  
#### Parameter Format

##### Querying Interfaces
```javascript
// Query if a method under a feature is supported ` @ ${ featureName } . ${ method } ` // Query if a feature is supported ` @ ${ featureName } `
```

**Example**
```javascript
if(this . $canIUse('@system.router.push')) { // Can use the method @system.router.push } if(this . $canIUse('@system.router')) { // Can use the @system.router interface }
```

##### Querying Components

The `type` can be `'attr'`, `'style'`, or `'method'`, corresponding to the component's attributes, styles, and methods respectively.
```javascript
// Query if an attribute, style, or method under a component is supported ` ${ componentName } . ${ type } . ${ name } ` // Query if a component is supported ` ${ componentName } `
```

**Example**
```javascript
if(this . $canIUse('scroll')) { // Can use the scroll component } if(this . $canIUse('scroll.attr.scroll-x')) { // Can use the scroll-x attribute of the scroll component }
```

### this.$watch

Monitor data changes. Dynamically add properties/event bindings. The property must be defined in `data`, and the handler function must be defined in `<script>`. The event is triggered when the property value changes.  
If monitoring a property in an object, use dots to separate parameters, e.g., `$watch(xxx.xxx.xxx, methodName)`.

#### Parameters

Attribute | Type | Description  
---|:---:|---  
data | String | Property name, supports 'a.b.c' format, does not support array indices  
handler | String | Event handler function name. The first parameter is the new property value, the second is the old property value  
  
#### Code Example
```html
< script > export default { props : [ 'propObject' ] , data { say : '' , propSay : '' } , onInit () { // Monitor data changes this . $watch ('say' , 'watchDataChange') this . $watch ('propObject.name' , 'watchPropsChange') } , /** * Monitor data changes, you can process the data and set values to data * @param newV * @param oldV */ watchPropsChange (newV , oldV) { console.info (` Monitoring data changes: ` , newV , oldV) this.propSay = newV && newV.toUpperCase () } , watchDataChange (newV , oldV) { console.info (` Monitoring data changes: ` , newV , oldV) } } </ script >
```

### this.$element

Get the DOM object of a component with the specified ID. If no ID is specified, return the root component DOM object.

#### Parameters

Type | Description  
---|---  
String | `this.$element('idName')` to get the DOM node  
  
#### Code Example
```html
< template > < div > < div id = ' xxx ' > </ div > </ div > </ template > < script > export default { onReady () { const el = this . $element ('xxx') console.log (` Output xxx node information: ${ el } `) } } </ script >
```

`this.$element('xxx')` gets the div component instance object with ID xxx, and `this.$element()` gets the root component instance object in the template.

The `id` property assignment can be viewed in this [document](</vela/quickapp/en/components/general/properties.html>).

### this.$nextTick

Execute a delayed callback after the next DOM update cycle. Using this method immediately after modifying data allows you to get the updated DOM.

#### Parameters

Type | Description  
---|---  
Function | The callback function that performs operations on the DOM  
  
#### Code Example
```html
< template > < div class = " page " > < text @click = " onAddClick " > Add Item </ text > < div class = " list " id = " list " > < div class = " item " for = " {{list}} " > < text > {{ $item }} </ text > </ div > </ div > </ div > </ template > < script > export default { private : { list : [ "Item 1" , "Item 2" ] } , onAddClick () { this.list.push (Math.random ()) // After updating data, the DOM does not change immediately. this . $element ("list") . getBoundingClientRect ({ success : (rect) => { console.log ("getBoundingClientRect.height=" , rect.height) } }) this . $nextTick (() => { // After updating data, the DOM changes. this . $element ("list") . getBoundingClientRect ({ success : (rect) => { console.log ("$nextTick getBoundingClientRect.height=" , rect.height) } }) }) } } </ script > < style > .page { padding-top : 20px ; width : 100% ; height : 100% ; flex-direction : column ; justify-content : flex-start ; align-items : center ; } .list { width : 200px ; flex-direction : column ; align-items : center ; border : 2px solid red ; } </ style >
```

In addition to the above common methods, there are event methods such as `this.$on`, `this.$off`, `this.$dispatch`, `this.$broadcast`, and `this.$emit` for parent-child component communication. The method descriptions are as follows:

Method | Parameters | Description  
---|:---:|---  
this.$on | type: String Event name  
handler: Function Event handler function | Add an event handler. Usage: `this.$on('xxxx', this.fn)`, where `fn` is a function defined in `<script>`  
this.$off | type: String Event name  
handler: Function Event handler function | Remove an event handler. Usage: `this.$off('xxxx', this.fn)` or `this.$off('xxx')` to remove all handlers for the specified event  
this.$dispatch | type: String Event name | Send an event notification to the parent component. Usage: `this.$dispatch('xxx')`. Normally, the event will bubble up. To stop bubbling, call `evt.stop()` in the event handler function  
this.$broadcast | type: String Event name | Send an event notification to child components. Usage: `this.$broadcast('xxx')`. Normally, the event will propagate down. To stop propagation, call `evt.stop()` in the event handler function  
this.$emit | type: String Event name  
data: Object Event parameters | Trigger an event, and the corresponding handler function will be called. Usage: `this.$emit('xxx')` or `this.$emit('xxx', {a:1})`. The passed event parameters can be accessed in the event callback function via `evt.detail`, e.g., `evt.detail.a`  
  
For examples of using event methods, refer to the [documentation](</vela/quickapp/en/guide/framework/template/component.html#parent-child-component-communication>).
