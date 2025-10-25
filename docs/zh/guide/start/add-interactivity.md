<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/start/add-interactivity.html -->

# 添加交互

在上一章节中，我们已经编写了两个页面的结构和样式，但是两个页面之间没有任何关联， 在本章中，我们会实现页面间的跳转。

## 注册事件

页面跳转由用户触发，需要给页面的特定元素添加对应的事件，比如`click`/`touchstart`。 有关事件更多的细节，请参考[通用事件](</vela/quickapp/zh/components/general/events.html>)。

在这个天气预报App中，我们采用的交互是滑动切换页面：

  1. 在实时天气页面中，向上滑动进入未来3天天气页面；
  2. 在未来3天天气页面，向右滑动返回到实时天气页面。

我们希望在页面任何地方滑动都执行跳转动作，所以将滑动事件(`swipe`)注册到根节点上。

模板代码如下：
```html
< template > < div class = " page column " @swipe = " toListPage " > <!-- 页面其它内容 --> </ div > </ template >
```

说明

`@swipe="toListPage"`也可以写成`onswipe="toListPage"`，详情请参考[事件绑定](</vela/quickapp/zh/guide/framework/template/event.html>)。

## 页面跳转

注册完事件后，需要在JavaScript代码中，定义`toListPage()`回调方法，通过判断滑动方向，决定是否做页面跳转。 页面跳转，需要使用到`@system.router`模块，使用前请先在`manifest.json`中声明：
```js
{ // ... "features" : [ { "name" : "system.router" } ] }
```

说明

更多router相关细节，请参考[页面切换](</vela/quickapp/zh/guide/framework/page-switch.html>)。

声明模块后，即可在JavaScript脚本中引入模块，然后使用`router`提供的API在页面间跳转：
```html
< script > import router from '@system.router' export default { // ... toListPage (eve) { if (eve.direction === 'up') { router.push ({ uri : '/pages/list' }) } } } </ script >
```

同样，在未来3天天气页面中，使用相同的方式来实现页面返回逻辑。对应的代码为：
```html
< template > < div class = " page column " @swipe = " toHomePage " > <!-- 页面其它内容 --> </ div > </ template >
```

```html
< script > import router from '@system.router' export default { // ... toHomePage (eve) { if (eve.direction === 'right') { router.back () } } } </ script >
```
