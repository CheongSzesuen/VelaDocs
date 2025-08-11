<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/template/component.html -->

# # 组件

## # 组件自定义

开发页面时开发者必须用到 Native 组件，如：`text`、`div`，这些组件是由各平台 Native 底层渲染出来的；如果开发一个复杂的页面，开发者把所有的 UI 部分写在一个文件的`<template>`，那代码的可维护性将会很低，并且模块之间容易产生不必要的耦合关系。

为了更好的组织逻辑与代码，可以把页面按照功能拆成多个模块，每个模块负责其中的一个功能部分，最后页面将这些模块引入管理起来，传递业务与配置数据完成代码分离，那么这就是自定义组件的意义。

自定义组件是一个开发者编写的组件，使用起来和 Native 一样，最终按照组件的`<template>`来渲染；同时开发起来又和页面一样，拥有 ViewModel 实现对数据、事件、方法的管理。

提示

由于自定义组件拥有独立的ViewModel，因此存在一定内存开销，在手表手环等轻量级设备上不建议使用。

**示例如下：**

``` <template> <div class="tutorial-page"> <text class="tutorial-title">自定义组件:</text> <text>{{ say }}</text> <text>{{ obj.name }}</text> </div> </template> <style lang="less"> .tutorial-page { flex-direction: column; padding-top: 20px; .tutorial-title { font-weight: bold; } } </style> <script> // 子组件 export default { data: { say: 'hello', obj: { name: 'quickApp' } }, onInit() { console.log('我是子组件') } } </script> ```

自定义组件中数据模型只能使用**data 属性** ，data 类型是 **Object** 。

### # 自定义组件生命周期：

`onInit` ：表示组件ViewModel的数据已经准备好，可以开始使用页面中的数据。

`onReady` ：表示组件ViewModel的模板已经编译完成，可以开始获取 DOM 节点。

`onDestroy` ：组件被销毁时调用，组件销毁时应该做一些释放资源的操作，例如释放定时器等。

## # 组件引入

vela中是通过`<import>`标签引入组件，如下面代码所示：

``` <import name="XXX" src="XXX"></import> ```

`<import>`标签中的`src`属性指定自定义组件的地址，`name`属性指定在父组件中引用该组件时使用的 **标签名称** 。

**示例如下：**

``` <import name="comp-part1" src="./part1"></import> <template> <div class="tutorial-page"> <text class="tutorial-title">引入组件：</text> <comp-part1></comp-part1> </div> </template> <style lang="less"> .tutorial-page { flex-direction: column; padding: 20px 10px; } .tutorial-title { font-weight: bold; } </style> <script> // 父组件 export default { private: {}, onInit() { console.log('引入组件') } } </script> ```

## # 父子组件通信

### # 父组件通过 Prop 向子组件传递数据

父组件向子组件传递数据，通过在子组件的`props`属性中声明对外暴露的属性名称，然后在组件引用标签上声明传递的父组件数据，详见[Props](</vela/quickapp/zh/guide/framework/template/Props.html>)部分。

**示例如下：**

``` <!-- 子组件 --> <template> <div class="child-demo"> <text class="title">子组件:</text> <text>{{ say }}</text> <text>{{ propObject.name }}</text> </div> </template> <script> export default { props: ['say', 'propObject'], onInit() { console.info(`外部传递的数据：`, this.say, this.propObject) } } </script> ```

``` <!-- 父组件 --> <import name="comp" src="./comp"></import> <template> <div class="parent-demo"> <comp say="{{say}}" prop-object="{{obj}}"></comp> </div> </template> <script> export default { private: { say:'hello' obj:{ name:'child-demo' } } } </script> ```

### # 子组件对父组件通信

  * 子组件通过`$emit()`触发在节点上绑定的自定义事件来执行父组件的方法，如父组件与组件一；
  * 子组件通过`$dispatch()`触发自定义事件，父组件通过`$on()`监控自定义事件的触发，如父组件与组件二；

**示例如下：**

``` <!-- 父组件 --> <import name="comp1" src="./comp1.ux"></import> <import name="comp2" src="./comp2.ux"></import> <import name="comp3" src="./comp3.ux"></import> <template> <div class="parent-demo"> <text>我是父组件count:{{count}}</text> <comp1 count="{{count}}" onemit-evt="emitEvt"></comp1> <text>我是父组件num:{{num}}</text> <comp2 num="{{num}}"></comp2> <text>我是父组件age:{{age}}</text> <input type="button" onclick="evtTypeEmit" value="触发$broadcast()"></input> <comp3></comp3> </div> </template> <script> export default { private:{ count:20, num:20, age:18 }, onInit(){ this.$on('dispatchEvt',this.dispatchEvt) }, emitEvt(evt){ this.count = evt.detail.count }, dispatchEvt(evt){ this.num = evt.detail.num }, evtTypeEmit(){ this.$broadcast('broadevt',{ age:19 }) }, } </script> ```

``` <!-- comp1 --> <template> <div class="child-demo"> <text>我是子组件一count:{{compCount}}</text> <input type="button" onclick='addHandler' value='add'></input> </div> </template> <script> export default { props: ['count'], data(){ return{ compCount:this.count } }, addHandler(){ this.compCount ++ this.$emit('emitEvt',{ count:this.compCount }) }, } </script> ```

``` <!-- comp2 --> <template> <div class="child-demo"> <text>我是子组件二num:{{compNum}}</text> <input type="button" onclick='delHandler' value='del'></input> </div> </template> <script> export default { props: ['num'], data(){ return{ compNum:this.num } }, delHandler(){ this.compNum -- this.$dispatch('dispatchEvt',{ num:this.compNum }) }, } </script> ```

``` <!-- comp3 --> <template> <div class="child-demo"> <text>我是子组件三age:{{compAge}}</text> </div> </template> <script> export default { props:[], data(){ return{ compAge:null } }, onInit(){ this.$on('broadevt',this.broadevt) }, broadevt(evt){ this.compAge = evt.detail.age } } </script> ```

框架向开发者提供了双向的事件传递

  * 向下传递：父组件触发，子组件响应；调用`parentVm.$broadcast()`完成向下传递，如：broadevt
  * 向上传递：子组件触发，父组件响应；调用`childVm.$dispatch()`完成向上传递，如：dispatchEvt

**提示：**

  * 触发时传递参数，再接收时使用`evt.detail`来获取参数
  * 当传递结束后，可以调用`evt.stop()`来结束传递,否则会一直传递下去

