<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/Props.html -->

# Props

## Prop Writing

Prop attribute names are written in camelCase. When passing data externally, convert them to kebab-case. For example, propObject is converted to prop-object.
```html
<!-- Child Component --> < template > < div class = " child-demo " > < text > {{ propObject.name }} </ text > </ div > </ template > < script > export default { props : [ 'propObject' ] } </ script >
```

```html
<!-- Parent Component --> < import name = " comp " src = " ./comp " > </ import > < template > < div class = " parent-demo " > < comp prop-object = " {{obj}} " > </ comp > </ div > </ template > < script > export default { private : { obj : { name : 'child-demo' } } } </ script >
```

## Attribute Default Values

When declaring props in a child component, you can set default values. If no data is passed when calling the child component, the default value will be automatically set.

To set default values, the `props` attribute must be written in Object form, not Array form.

**Example** :
```html
< script > // Child Component export default { props : { prop1 : { default : 'Hello' // Default value } , prop2Object : { } // No default value } , onInit () { console.info (` Data passed from parent: ` , this.prop1 , this.prop2Object) } } </ script >
```

## Data Unidirectionality

Data transfer between parent and child components is unidirectional. When the parent component's prop data updates, the child component's data refreshes to the latest value. However, if the child component's prop value changes, it does not affect the parent component's value.

However, **if the prop type is an array or object, changes in the child component will affect the parent component's value.** This means you should not modify the prop value inside a child component, as it is a dangerous operation.

## Three Common Methods for Handling Prop Values:

### 1\. Using the prop value as an initial value and receiving it with data
```html
< script > export default { props : [ 'say' , 'propObject' ] , data : { count : null , obj : null } , onInit () { console.info (` Data passed from parent: ` , this.say , this.propObject) this.count = this.propObject.count // Assign a simple type from prop to data this.obj = JSON.parse (JSON.stringify (this.propObject)) // Deep clone the prop } } </ script >
```

### 2\. Using $watch to monitor data changes

If monitoring a property in an object, use a dot-separated parameter, e.g., `$watch(xxx.xxx.xxx, methodName)`. For details, see [$watch](</vela/quickapp/en/guide/framework/script/global-data-method.html#this.$watch>).
```html
< script > export default { props : [ 'propObject' ] , data : { propSay : '' } , onInit () { // Monitor data changes this . $watch ('propObject.name' , 'watchPropsChange') } , /** * Monitor data changes, process the data, and set the value to data * @param newV * @param oldV */ watchPropsChange (newV , oldV) { console.info (` Data change monitored: ` , newV , oldV) this.propSay = newV && newV.toUpperCase () } } </ script >
```

### 3\. Using computed properties

For details, see [Computed Properties](</vela/quickapp/en/guide/framework/template/computed.html>).
```html
< script > export default { props : [ 'say' ] , computed : { sayText () { return this.say.toUpperCase () } } } </ script >
```

## Attribute Validation

When declaring props in a child component, you can specify data type validation.

The supported types for type checking include [`String`, `Number`, `Boolean`, `Function`, `Object`, `Array`].

To validate types, the `props` attribute must be written in Object form, not Array form.

**Example:**
```html
< script > // Child Component export default { props : { prop1 : { default : 'Hello' // Default value type : String // Type validation } , prop2Object : { } // No default value } , onInit () { console.info (` Data passed from parent: ` , this.prop1 , this.prop2Object) } } </ script >
```
