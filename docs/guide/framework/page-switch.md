<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/page-switch.html -->

# 页面切换

## 通过接口 router 切换页面和传递参数

### 切换页面

router 接口在使用前，需要先导入模块。

通过`router.push(OBJECT)`可以完成页面切换，其支持的参数`uri`的格式详细描述参见[页面路由](</vela/quickapp/zh/features/basic/router.html>)。

**示例如下：**
```html
< template > < div class = " page " > < input class = " btn " type = " button " value = " 跳转到新页面 " onclick = " routePage " > </ input > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } .btn { width : 400px ; height : 60px ; margin-top : 70px ; border-radius : 30px ; background-color : #09ba07 ; font-size : 30px ; color : #ffffff ; } </ style > < script > // 导入模块 import router from '@system.router' export default { routePage () { // 跳转到应用内的某个页面，当前页面无法返回 router.replace ({ uri : '/Pages/newPage' }) } } </ script >
```

### 传递参数

`router`接口的参数`params`可配置页面跳转时需要传递的参数。

**示例如下：**
```html
< template > < div class = " page " > < input class = " btn " type = " button " value = " 携带参数跳转页面 " onclick = " routePageReplaceWithParams " > </ input > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } .btn { width : 400px ; height : 60px ; margin-top : 70px ; border-radius : 30px ; background-color : #09ba07 ; font-size : 30px ; color : #ffffff ; } </ style > < script > // 导入模块 import router from '@system.router' export default { private : { title : 'Hello, world!' } , onInit () { console.info ('接口router切换页面并传递参数') } , routePageReplaceWithParams () { // 跳转到应用内的某个页面 router.replace ({ uri : '/PageParams/receiveparams' , params : { key : this.title } }) } } </ script >
```

## 接收参数

现在，开发者已经了解了通过接口`router`在页面之间传递参数的方法，如何接收参数呢？

其实很简单，接口`router`传递的参数的接收方法完全一致：在页面的 ViewModel 的`protected`属性中声明使用的属性。

注意

  * `protected`内定义的属性，允许被应用内部页面请求传递的数据覆盖，不允许被应用外部请求传递的数据覆盖
  * 若希望参数允许被应用外部请求传递的数据覆盖，请在页面的 ViewModel 的`public`属性中声明使用的属性

**示例如下：**
```html
< template > < div class = " page " > < text > page </ text > <!-- template中显示页面传递的参数 --> < text > {{key}} </ text > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } </ style > < script > export default { protected : { key : '' } , onInit () { // js中输出页面传递的参数 console.info ('key: ' \+ this.key) } } </ script >
```
