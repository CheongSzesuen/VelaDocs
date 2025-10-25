<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/template/computed.html -->

# Computed Properties

## Basic Usage of Computed Properties

We often use expressions in templates, and using expressions properly can improve our development efficiency. However, putting too much logic in the template makes it heavy and difficult to maintain. For example:
```html
< text > {{ message.split('').reverse().join('') }} </ text >
```

In this case, the template is no longer simple declarative logic. If we use such expressions in many places, it might reduce the readability of the template, and reusing the same expression logic redundantly makes the code hard to maintain. To address this, we can use computed properties:
```html
< template > < div > < text > Original message: "{{ message }}" </ text > < text > Computed reversed message: "{{ reversedMessage }}" </ text > </ div > </ template > < script > export default { data : { message : 'Hello' } , computed : { // Getter function for the computed property reversedMessage () { // `this` points to the vm instance return this.message.split ('') . reverse () . join ('') } } , onReady () { console.log (this.reversedMessage) // olleH this.message = 'Goodbye' console.log (this.reversedMessage) // eybdooG } } </ script >
```

Here, we declared a computed property `reversedMessage`. The function we provided will be used as the getter function for the property `vm.reversedMessage`, and the value of `vm.reversedMessage` always depends on the value of `vm.message`.

You can bind computed properties in the template just like binding regular properties. The component instance knows that `vm.reversedMessage` depends on `vm.message`, so when `vm.message` changes, all bindings that depend on `vm.reversedMessage` will also update.

## Setting the setter Function for Computed Properties

Computed properties have only a getter by default, but you can also provide a setter when needed:
```html
< script > export default { data : { firstName : 'Quick' , lastName : 'App' } , computed : { fullName : { get () { return ` ${ this.firstName } ${ this.lastName } ` } , set (value) { const names = value.split (' ') this.firstName = names [ 0 ] this.lastName = names [ names.length \- 1 ] } } } , onReady () { console.log (this.fullName) // Quick App this.fullName = 'John Doe' console.log (this.firstName) // John console.log (this.lastName) // Doe } } </ script >
```
