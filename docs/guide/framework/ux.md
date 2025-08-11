<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/ux.html -->

# # UX 文件

APP，页面均通过 ux 后缀文件编写，ux 后缀文件由[template 模板](</vela/quickapp/zh/guide/framework/template/>)、[style 样式](</vela/quickapp/zh/guide/framework/style/>)和[script 脚本](</vela/quickapp/zh/guide/framework/script/>)3 个部分组成，一个典型的页面 ux 后缀文件示例如下：

``` <template> <!-- template里只能有一个根节点 --> <div class="page"> <text class="title">欢迎打开{{title}}</text> <!-- 点击跳转详情页 --> <input class="btn" type="button" value="跳转到详情页" onclick="routeDetail"> </div> </template> <style> .page { flex-direction: column; justify-content: center; align-items: center; } .title { font-size: 30px; text-align: center; } .btn { width: 400px; height: 60px; margin-top: 75px; border-radius: 43px; background-color: #09ba07; font-size: 30px; color: #ffffff; } </style> <script> import router from '@system.router' export default { // 页面级组件的数据模型，影响传入数据的覆盖机制：private内定义的属性不允许被覆盖 private: { title: '示例页面' }, routeDetail () { // 跳转到应用内的某个页面，router用法详见：文档->接口->页面路由 router.push ({ uri: '/DemoDetail' }) } } </script> ```

## # app.ux

当前`app.ux`编译后会包含`manifest配置信息`（可以在`npm run build`之后查看文件内容），所以请不要删除`/**manifest**/`的注释内容标识。

您可以在`<script>`中引入一些公共的脚本，并暴露在当前 app 的对象上，如下所示，然后就可以在页面 ux 文件的 ViewModel 中，通过`this.$app.$def.util`访问。

``` <script> /** * 应用级别的配置，供所有页面公用 */ import util from './util' export default { showMenu: util.showMenu, createShortcut: util.createShortcut, util } </script> ```
