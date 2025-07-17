<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/best-practice/memory.html -->

# # 内存优化

由于运动手表整体内存较小，对于三方应用内存占用量要求比较高。根据之前遇到的问题，给出一份三方应用开发时的注意事项清单，以帮助开发者尽量降低应用的内存占用，符合手表应用验收标准。

## # 代码注意事项

  1. 和 UI 无关，不需要绑定的数据，不要声明到 viewModel 的数据里，减少 observer 或者数据代理

``` <template> <div> <text>{{name}}</text> </div> </template> <script> const someObj = { a: 1 } // 推荐写法 export default { protected: { name: 'aaa', someObj: { // 不推荐写法 a: 1 } } } </script> ```

  2. 页面对象更新时，尽量原地更新，不要重新赋值，开辟新的内存空间

``` export default { protected: { list: [{ name: 'aa', age: 22 }] }, onClick() { // 不推荐写法 this.list = [{ name: 'bb', age: 21 }] // 推荐写法 this.list[0].name = 'bb', this.list[0].age = 21 } } ```

  3. 页面中声明的属性和方法不要缓存到全局上

页面销毁时，为清理内存，会将页面对象相关的属性和方法尽量解除引用。如果被引用到全局，就无法清理其占用的内存，并且在其他地方调用该缓存的属性和方法，可能引起报错。

``` export default { protected: { list: [{ name: 'aa', age: 22 }] }, onShow() { this.$app.$def.somearray.push(this.foo) // 不推荐写法 }， foo() { this.list.push({ name: 'bb', age: 21 }) } } ```

  4. 页面销毁时，清除未执行完的定时器

``` export default { protected: { timer: null } onShow() { this.timer = setTimeout(()=>{}, 1000000) } onDestroy() { if(this.timer){ clearTimeout(this.timer) } } } ```

  5. 读取文件数据，用完后及时释放

``` let foo = await storage.getItem('key') let bar = await file.readText('path') let fooObj = JSON.parse(foo) let barObj = JSON.parse(bar) // 用完后及时释放 foo = null bar = null fooObj = null barObj = null ```

  6. 调用runGC方法

通过执行全局对象global上的runGC方法，及时进行垃圾回收，避免内存泄漏。不要频繁调用，防止页面卡顿。

``` global.runGC() ```

  7. `static`属性

`template`模板中提供了`static`属性支持，如果绑定的变量后面不会再改变，添加`static`标记有助于框架减少实现动态节点，减少内存，也会降低页面销毁删除对象的时间。

``` <template> <div> <text static >{{name}}</text> <image static src="/assets/icon/a.png"/> </div> </template> <script> export default { protected: { name: 'aaa' } } </script> ```

另外，还支持在 `template` 上使用`.static`修饰符修饰节点的某个静态属性，适用于节点的该属性值仅在初始时被赋值一次，之后不会再变更。使用语法：`attr.static="{{ attrValue }}"`

注意

  * 节点的 `if` / `for` 静态属性只能通过 `.static` 修饰词进行修饰
  * 节点的 `static` 属性优先级比 `.static`高。对于声明了 `static` 属性的节点，可以不需要额外声明某个属性的静态修饰词 `attr.static`

``` <template> <div> <div if.static="{{ bool }}"> <text style="{{ styl }}" someattr="{{ some }}" class="{{ cls }}" static>{{name}}</text> <input style="{{ styl }}" name="{{ some }}" class="{{ cls }}" value="{{ name }}" static /> </div> <text if.static="{{ bool }}" style.static="{{ styl }}" someattr.static="{{ some }}" class.static="{{ cls }}" value.static >{{name}}</text> <input if.static="{{ bool }}" style.static="{{ styl }}" someattr.static="{{ some }}" class.static="{{ cls }}" value.static="{{name}}" /> </div> </template> <script> export default { private: { name: 'aaa', bool: true, cls: 'basic-text', some: 'someattr', styl: { backgroundColor: '#d1d1d1' } } } </script> ```

`block`组件是一个逻辑区块节点，如果增加了`static`属性，表示`block`包含的所有节点都是静态数据绑定，绑定的数据只计算一次，后面不会再发生改变，适用于绑定一些枚举值或者不可变的列表数据等，有效减少内存占用。

``` <template> <!-- block 内部节点数据只计算一次只渲染一次 --> <block static> <text class="{{cls}}">标题： {{title}}</text> <text>条件渲染</text> <list> <list-item for="{{list}}" type="item"> <text>{{$item}}</text> </list-item> </list> </block> </template> <script> export default { private: { title: '我是标题1', cls: 'txt-cls', display: true, list: ['a', 'b', 'c'] } } </script> ```

## # 减少打包代码体积

  1. 减少不必要的三方依赖，选用轻量的三方依赖

对于`package.json`中的三方依赖，去除没有用到的依赖，对于必要的大型依赖，尽可能替换成轻量的依赖。

  2. 使用全局方法

将通用的方法、常量和对象实例统一挂在`global`上，在页面中不用再`import`，需要用的时候直接从`global`上取。

``` // global.js import foo from './foo' import bar from './bar' global.foo = foo global.bar = bar // app.ux import './global' // pages/xxx/index.js const {foo, bar} = global export default { // 调用foo、bar //...... } ```

以QQ音乐为例，以下为优化前后效果对比：

| 优化前 | 替换轻量级依赖 | 使用全局方法  
---|---|---|---  
代码行数 | 21965 | 13156 | 6807  
最大内存 | 4842844 | 3295928 | 1872528  
  
  3. 在保证图片质量的前提下，尽量用低分辨率图片  
大尺寸图片在加载时会占用较多内存，可以先将大尺寸图片缩放成小尺寸图片，再进行压缩(<https://tinypng.com>[ (opens new window)](<https://tinypng.com>))，减少图片的体积。

  4. 去除没有用到的css和js  
对于css中没有用到的样式，js中没有用到的变量和函数，可以删除或者注释，精简代码。

  5. 尽可能减少页面数量  
在不影响业务需求的前提下，用最少的页面去实现，减少代码体积，简化应用逻辑。

← [ 多屏设计 ](</vela/quickapp/zh/guide/design/multi-screens.html>) [ 常用业务优化 ](</vela/quickapp/zh/guide/best-practice/business.html>) → 

快速导航

代码注意事项

减少打包代码体积
