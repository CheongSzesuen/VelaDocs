<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/script/global-data-method.html -->

# 全局属性和方法

## 对象

### 公共对象

属性 | 类型 | 描述  
---|:---:|---  
$app | Object | 应用对象  
$page | Object | 页面对象  
$valid | Boolean | 页面对象是否有效  
  
#### 应用对象

在页面中可通过 $app 访问到全局应用对象。

在`app.ux`文件中，开发者可以定义全局可访问的数据和方法，在页面中通过`this.$app.$def`访问，在`app.ux`文件中，直接通过`this`访问。例如在`app.ux`文件中定义如下：
```html
< script > /** * 应用级别的配置，供所有页面公用 */ export default { data : { a : 1 } , func : function () { console.log (this.data.a) console.log (` function executed! `) } } </ script >
```

在其他页面可以这样调用：
```javascript
this . $app . $def.data this . $app . $def.func()
```

可通过 $app 访问如下内置方法：

属性 | 类型 | 描述  
---|:---:|---  
exit | Function | 退出 JS 应用，结束应用生命周期。调用方法：this.$app.exit()  
  
#### 页面对象

在页面中可通过this.$page访问到当前页面对象，该对象上可访问到如下属性：

属性 | 类型 | 描述  
---|:---:|---  
name | String | 获取当前页面路由的名称，与manifest 文件中router.pages 中对应的属性名一致  
path | String | 获取当前页面路由的 path，与manifest 文件中router.pages 中对应的 path 一致  
component | String | 获取当前页面路由的 component，与manifest 文件中router.pages 中对应的 component 一致  
  
## 方法

### this.$canIUse3+

在页面中可通过 this.$canIUse 进行可使用的能力查询，包括接口和组件。

#### 参数:

类型 | 描述  
---|---  
String | 要查询的能力，格式见下方  
  
#### 返回值：

类型 | 描述  
---|---  
Boolean | 查询的能力是否支持  
  
#### 入参格式

##### 查询接口
```javascript
// 查询feature下的方法是否支持 ` @ ${ featureName } . ${ method } ` // 查询某个feature是否支持 ` @ ${ featureName } `
```

**示例**
```javascript
if(this . $canIUse('@system.router.push')) { // 可以使用方法@system.router.push } if(this . $canIUse('@system.router')) { // 可以使用@system.router接口 }
```

##### 查询组件

type取值可以是`'attr'`、`'style'`、`'method'`，分别对应组件的属性、样式、方法。
```javascript
// 查询组件下的属性、样式、方法是否支持 ` ${ componentName } . ${ type } . ${ name } ` // 查询组件是否支持 ` ${ componentName } `
```

**示例**
```javascript
if(this . $canIUse('scroll')) { // 可以使用scroll组件 } if(this . $canIUse('scroll.attr.scroll-x')) { // 可以使用scroll组件的scroll-x属性 }
```

### this.$watch

监控数据改变。动态添加属性/事件绑定，属性必须在 data 中定义，handler 函数必须在`<script>`定义，当属性值发生变化时事件被触发。  
如果是监听对象中的属性，参数请使用.分割，如：$watch(xxx.xxx.xxx, methodName)。

#### 参数

属性 | 类型 | 描述  
---|:---:|---  
data | String | 属性名，支持'a.b.c'格式，不支持数组索引  
handler | String | 事件句柄函数名，函数的第一个参数为新属性值，第二个参数为旧的属性值  
  
#### 代码示例
```html
< script > export default { props : [ 'propObject' ] , data { say : '' , propSay : '' } , onInit () { // 监听数据变化 this . $watch ('say' , 'watchDataChange') this . $watch ('propObject.name' , 'watchPropsChange') } , /** * 监听数据变化，你可以对数据处理后，设置值到data上 * @param newV * @param oldV */ watchPropsChange (newV , oldV) { console.info (` 监听数据变化： ` , newV , oldV) this.propSay = newV && newV.toUpperCase () } , watchDataChange (newV , oldV) { console.info (` 监听数据变化： ` , newV , oldV) } } </ script >
```

### this.$element

获取指定 id 的组件 dom 对象，如果没有指定 id，则返回根组件 dom 对象。

#### 参数

类型 | 描述  
---|---  
String | this.$element('idName')获取 dom 节点  
  
#### 代码示例
```html
< template > < div > < div id = ' xxx ' > </ div > </ div > </ template > < script > export default { onReady () { const el = this . $element ('xxx') console.log (` 输出xxx节点信息： ${ el } `) } } </ script >
```

this.$element('xxx') 获取 id 为 xxx 的 div 组件实例对象， this.$element() 获取模板中的根组件实例对象。

`id`属性赋值可以查看此[文档](</vela/quickapp/zh/components/general/properties.html>)。

### this.$nextTick

在下次 DOM 更新循环结束之后执行延迟回调。在修改数据之后立即使用这个方法，可以获取更新后DOM。

#### 参数

类型 | 描述  
---|---  
Function | 回调函数中执行的是会对DOM进行操作的处理  
  
#### 代码示例
```html
< template > < div class = " page " > < text @click = " onAddClick " > 添加项目 </ text > < div class = " list " id = " list " > < div class = " item " for = " {{list}} " > < text > {{ $item }} </ text > </ div > </ div > </ div > </ template > < script > export default { private : { list : [ "项目1" , "项目2" ] } , onAddClick () { this.list.push (Math.random ()) // 更新数据后,DOM没有立即发生变化。 this . $element ("list") . getBoundingClientRect ({ success : (rect) => { console.log ("getBoundingClientRect.height=" , rect.height) } }) this . $nextTick (() => { // 更新数据后,DOM发生变化。 this . $element ("list") . getBoundingClientRect ({ success : (rect) => { console.log ("$nextTick getBoundingClientRect.height=" , rect.height) } }) }) } } </ script > < style > .page { padding-top : 20px ; width : 100% ; height : 100% ; flex-direction : column ; justify-content : flex-start ; align-items : center ; } .list { width : 200px ; flex-direction : column ; align-items : center ; border : 2px solid red ; } </ style >
```

除了以上公共方法，还有this.$on、this.$off、this.$dispatch、this.$broadcast、this.$emit等事件方法用于父子组件通信。方法说明如下：

方法 | 参数 | 描述  
---|:---:|---  
this.$on | type: String 事件名  
handler: Function 事件句柄函数 | 添加事件处理句柄用法：this.$on('xxxx', this.fn)，fn 是在<script>中定义的函数  
this.$off | type: String 事件名  
handler: Function 事件句柄函数 | 删除事件处理句柄用法：this.$off('xxxx', this.fn) this.$off('xxx') 删除指定事件的所有处理句柄  
this.$dispatch | type: String 事件名 | 向上层组件发送事件通知用法：this.$dispatch('xxx')正常情况下，会一直向上传递事件（冒泡）如果要停止冒泡，在事件句柄函数中调用evt.stop()即可  
this.$broadcast | type: String 事件名 | 向子组件发送事件通知用法：this.$broadcast('xxx')正常情况下，会一直向下传递事件如果要停止传递，在事件句柄函数中调用evt.stop()即可  
this.$emit | type: String 事件名  
data: Object 事件参数 | 触发事件，对应的句柄函数被调用用法：this.$emit('xxx') this.$emit('xxx', {a:1})传递的事件参数可在事件回调函数中，通过evt.detail来访问，例如evt.detail.a  
  
事件方法使用示例可参考[文档](</vela/quickapp/zh/guide/framework/template/component.html#父子组件通信>)。
