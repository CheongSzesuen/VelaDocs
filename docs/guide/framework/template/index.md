<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/ -->

# template 模板

类似`HTML`的标签语言，结合基础组件、事件，构建出页面的结构。

注意

模板中只能有 1 个根节点，如：div；请不要在`<template>`下存在多个根节点，也不要使用 block 作为根节点。

## 数据绑定
```html
< template > < text > {{message}} </ text > </ template > < script > export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private : { message : 'Hello' } } </ script >
```

## 事件绑定
```html
< template > < div > <!-- 正常格式 --> < text onclick = " press " > </ text > <!-- 缩写 --> < text @click = " press " > </ text > </ div > </ template > < script > export default { press (e) { this.title = 'Hello' } } </ script >
```

事件回调支持的写法（其中`{{}}`可以省略）：

**fn** ：`fn`为事件回调函数名（在`<script>`中有对应的函数实现）；

**fn(a,b)** ：函数参数例如`a`，`b`可以是常量，或者是在`<script>`中定义的页面的数据变量（前面不用写`this`）；

回调函数被调用时，会在参数列表末尾自动添加一个`evt`参数，通过`evt`参数访问回调事件相关上下文数据（数据内容具体参看组件回调事件说明），例如点击事件的点击位置`x`，`y`。

## 列表渲染
```html
< template > < div > < div for = " {{list}} " tid = " uniqueId " > < text > {{$idx}} </ text > < text > {{$item.uniqueId}} </ text > </ div > </ div > </ template > < script > export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private : { list : [ { uniqueId : 1 } , { uniqueId : 2 } ] } } </ script >
```

`for指令`根据源数据数组渲染列表，支持的写法如下（其中`{{}}`可以省略）：

  * `for="{{list}}"` `list`为源数据数组，默认的数组元素名为`$item`；
  * `for="{{value in list}}"` `value`为自定义的数组元素名，默认的数组元素索引名为`$idx`；
  * `for="{{(index, value) in list}}"` `index`为自定义的数组元素索引名，`value`为自定义的数组元素名。

`for指令`的`tid属性`用于指定数组元素的唯一 Id，若未指定，默认使用数组索引(`$idx`)作为唯一 Id。`tid属性`的作用在于元素节点重用，优化 for 循环的重绘效率。

示例代码中，`tid="uniqueId"`表示使用数组`list`的数组元素`$item.uniqueId`作为数组元素的唯一 Id，且必须保证 uniqueId 这个属性值在每个数组元素都不一样。

使用`tid属性`时应注意：

  * `tid属性`指定的数据属性必须存在，否则可能导致运行异常；
  * `tid属性`指定的数据属性要保证唯一，否则可能导致性能问题；
  * `tid属性`目前不支持表达式。

## 条件渲染

分为2种：`if/elif/else` 和`show`。它们的区别在于：`if`为`false`时，组件会从VDOM中移除，而`show`仅仅是渲染时不可见，组件依然存在于 VDOM 中；

`if/elif/else`节点必须是相邻的兄弟节点，否则无法通过编译。
```html
< template > < div > < text if = " {{display}} " > Hello-1 </ text > < text elif = " {{display}} " > Hello-2 </ text > < text else > Hello-3 </ text > </ div > </ template > < script > export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private : { display : false } } </ script >
```

`show`等同于`visible=none`，主要用于在原生组件上声明；
```html
< template > < text show = " {{visible}} " > Hello </ text > </ template > < script > export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private : { visible : false } } </ script >
```

## 逻辑控制块

可以使用`<block>`实现更为灵活的循环/条件渲染；注意`<block>`目前只支持`for`和`if/elif/else`属性，如果没有指定任何属性，`<block>`则在构建时被当作`透明`节点对待，其子节点被添加到`<block>`的父节点上。
```html
< template > < list > < block for = " cities " > < list-item type = " city " > < text > {{$item.name}} </ text > </ list-item > < list-item type = " spot " for = " $item.spots " > < text > {{$item.address}} </ text > </ list-item > </ block > </ list > </ template > < script > export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private : { cities : [ { name : 'beijing' , spots : [ { address : 'XXX' } ] } , { name : 'shanghai' , spots : [ { address : 'XXX' } , { address : 'XXX' } ] } ] } } </ script >
```
