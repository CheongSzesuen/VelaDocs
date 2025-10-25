<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/Props.html -->

# Props

## Prop 写法

Prop 属性名称使用 camelCase(驼峰命名法)命名，在外部传递数据时请转化为以 kebab-case (短横线分隔命名) propObject 转换为 prop-object。
```html
<!-- 子组件 --> < template > < div class = " child-demo " > < text > {{ propObject.name }} </ text > </ div > </ template > < script > export default { props : [ 'propObject' ] } </ script >
```

```html
<!-- 父组件 --> < import name = " comp " src = " ./comp " > </ import > < template > < div class = " parent-demo " > < comp prop-object = " {{obj}} " > </ comp > </ div > </ template > < script > export default { private : { obj : { name : 'child-demo' } } } </ script >
```

## 属性默认值

子组件声明属性时，可以设置默认值。当调用子组件没有传入该数据时，将会自动设为默认值。

如果需要设置默认值，`props` 属性的写法必须要要写成 Object 形式，不能写成 Array 形式。

**示例如下：**
```html
< script > // 子组件 export default { props : { prop1 : { default : 'Hello' //默认值 } , prop2Object : { } //不设置默认值 } , onInit () { console.info (` 外部传递的数据： ` , this.prop1 , this.prop2Object) } } </ script >
```

## 数据单向性

父子间的数据传输是单向性的，父组件 prop 数据更新，子组件的数据会刷新为最新值；子组件的 prop 值发生改变，并不会改变父组件中值。

但是**prop 类型事数组或者对象，自组件变化会影响到父组件的值，** 这意味着你不应该在一个子组件内部改变 prop 的值，这是危险性操作。

## 常见的三种操作 prop 值的方法：

### 1\. prop 传入的值作为初始值，用 data 接收
```html
< script > export default { props : [ 'say' , 'propObject' ] , data { count : null , obj : null } , onInit () { console.info (` 外部传递的数据： ` , this.say , this.propObject) this.count = this.propObject.count // 将prop中一个简单类型赋值给data this.obj = JSON.parse (JSON.stringify (this.propObject)) // 将 prop 深度克隆 } } </ script >
```

### 2\. $watch 监控数据改变

如果是监听对象中的属性，参数请使用.分割，如：$watch(xxx.xxx.xxx, methodName)，详见[$watch](</vela/quickapp/zh/guide/framework/script/global-data-method.html#this.$watch>)。
```html
< script > export default { props : [ 'propObject' ] , data { propSay : '' } , onInit () { // 监听数据变化 this . $watch ('propObject.name' , 'watchPropsChange') } , /** * 监听数据变化，你可以对数据处理后，设置值到data上 * @param newV * @param oldV */ watchPropsChange (newV , oldV) { console.info (` 监听数据变化： ` , newV , oldV) this.propSay = newV && newV.toUpperCase () } } </ script >
```

### 3\. computed 属性

详见[计算属性](</vela/quickapp/zh/guide/framework/template/computed.html>)。
```html
< script > export default { props : [ 'say' ] , computed : { sayText () { return this.say.toUpperCase () } } } </ script >
```

## 属性校验

子组件声明属性时，可以指定数据类型校验。

类型检查支持的类型包括 [`String`、`Number`、`Boolean`、`Function`、`Object`、`Array`]

如果需要校验类型，`props` 属性的写法必须要要写成 Object 形式，不能写成 Array 形式。

**示例如下：**
```html
< script > // 子组件 export default { props : { prop1 : { default : 'Hello' //默认值 type : String // 校验类型 } , prop2Object : { } //不设置默认值 } , onInit () { console.info (` 外部传递的数据： ` , this.prop1 , this.prop2Object) } } </ script >
```
