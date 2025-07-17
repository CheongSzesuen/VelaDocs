<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/computed.html -->

# # 计算属性

## # 计算属性的基本使用

我们经常会在模版内使用表达式，合理使用表达式可以提升我们的开发效率。但是在模板中放入太多的逻辑会让模板过重且难以维护。例如：

``` <text> {{ message.split('').reverse().join('') }} </text> ```

在这个地方，模板不再是简单的声明式逻辑。如果我们在很多地方用上这样的表达式，有可能让模版的可读性降低，并且重复使用同一表达式逻辑会让代码变得冗余，不易维护。对此，我们可以使用计算属性：

``` <template> <div> <text>Original message: "{{ message }}"</text> <text>Comtextuted reversed message: "{{ reversedMessage }}"</text> </div> </template> <script> export default { data: { message: 'Hello' }, computed: { // 计算属性的 getter reversedMessage() { // `this` 指向 vm 实例 return this.message.split('').reverse().join('') } }, onReady() { console.log(this.reversedMessage) // olleH this.message = 'Goodbye' console.log(this.reversedMessage) // eybdooG } } </script> ```

这里我们声明了一个计算属性 `reversedMessage`。我们提供的函数将用作属性 `vm.reversedMessage` 的 getter 函数，这时 `vm.reversedMessage` 的值始终取决于 `vm.message` 的值。

你可以像绑定普通属性一样在模板中绑定计算属性。组件实例知道 `vm.reversedMessage` 依赖于 `vm.message`，因此当 `vm.message` 发生改变时，所有依赖 `vm.reversedMessage` 的绑定也会更新。

## # 设置计算属性的 `setter` 函数

计算属性默认只有 getter ，不过在需要时你也可以提供一个 setter ：

``` <script> export default { data: { firstName: 'Quick', lastName: 'App' }, computed: { fullName: { get() { return `${this.firstName} ${this.lastName}` }, set(value) { const names = value.split(' ') this.firstName = names[0] this.lastName = names[names.length - 1] } } }, onReady() { console.log(this.fullName) // Quick App this.fullName = 'John Doe' console.log(this.firstName) // John console.log(this.lastName) // Doe } } </script> ```

← [ 条件指令 ](</vela/quickapp/zh/guide/framework/template/if.html>) [ 组件 ](</vela/quickapp/zh/guide/framework/template/component.html>) → 

快速导航

计算属性的基本使用

设置计算属性的 `setter` 函数
