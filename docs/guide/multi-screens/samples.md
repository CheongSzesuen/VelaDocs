<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/multi-screens/samples.html -->

# # 代码示例

## # 页面布局及元素适配

一些开发中常见的跨屏适配示例。

### # 自适应容器大小

使用百分比或flex样式替代px写固定容器大小的布局方式可以在多屏适时有更好的兼容性。比如长列表滚动的场景，示例如下：

``` <template> <div class="demo-page"> <text class="title"> 长列表 </text> <list class="list"> <list-item class="item" type="custom" for="{{listData}}"> <text>{{$item.name}}</text> </list-item> </list> </div> </template> <script> export default { private: { listData: [ { name: 'TEST1 TEST1 TEST1' }, { name: 'TEST2 TEST2 TEST2' }, { name: 'TEST3 TEST3 TEST3' }, { name: 'TEST4 TEST4 TEST4' }, { name: 'TEST5 TEST5 TEST5' }, { name: 'TEST6 TEST6 TEST6' }, { name: 'TEST7 TEST7 TEST7' }, { name: 'TEST8 TEST8 TEST8' }, { name: 'TEST9 TEST9 TEST9' }, { name: 'TEST10 TEST10 TEST10' } ] } } </script> <style> .demo-page { flex-direction: column; align-items: center; background-color: #fff; } .title { margin-top: 50px; padding: 20px 0; font-size: 32px; } .list { flex: 1; width: 340px; margin-bottom: 5px; align-items: center; } .item { width: 100%; height: 100px; margin-bottom: 20px; border-radius: 20px; background-color: #ccc; text-align: center; } text { width: 100%; font-size: 30px; text-align: center; color: #000; } </style> ```

效果展示：

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/multi-samples-list-1.345da4e8.png) ![](../../images/multi-samples-list-2.533cdb85.png) ![](../../images/multi-samples-list-3.d5203d2a.png)

### # 单页三行布局

手表、手环场景下单页面三行布局是比较常用的一种设计方式，页面结构大致分为顶部标题栏，底部按钮交互区域以及中部主体内容区。建议采用顶部底部高度固定，主体部分高度自适应的方式来做整体布局。

代码示例：

``` <template> <div class="demo-page"> <div class="header"> <text>header</text> </div> <div class="content"> <text>content</text> </div> <div class="footer"> <text>footer</text> </div> </div> </template> <script> export default {} </script> <style> .demo-page { width: 466px; height: 466px; flex-direction: column; } .header { width: 100%; height: 100px; background-color: red; } .content { flex: 1; background-color: yellow; } .footer { width: 100%; height: 100px; background-color: blue; } text { width: 100%; font-size: 30px; color: black; text-align: center; } </style> ```

效果展示：

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/multi-samples-layout-c.744a8cfb.png) ![](../../images/multi-samples-layout-r.cb8cc25f.png) ![](../../images/multi-samples-layout-s.8c291e19.png)

### # px自动缩放计算

px长度单位会根据配置的项目配置基准宽度进行换算，过程中产生的小数位会做四舍五入处理。因此，在一些需要精准计算的场景中需要考虑到换算带来的误差值（通常为+-1px）。

比如下面这个示例， 在计算行宽的时候没考虑误差，导致某些设备上产生渲染错行的问题：

![](../../images/multi-samples-px-1.c2c1609b.png) ![](../../images/multi-samples-px-2.d64e5b21.png) ![](../../data:image/png;base64,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)

代码示例：

``` <template> <div class="demo-page"> <div class="item" for="nums"> <text>{{$item}}</text> </div> </div> </template> <script> export default { private: { nums: [1, 2, 3, 4] } } </script> <style> .demo-page { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; } .item { width: 110px; height: 110px; margin: 2px; background-color: #ccc; } text { color: #000; font-size: 30px; } </style> ```

效果展示：

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/multi-samples-px-4.9a7cd3d3.png) ![](../../images/multi-samples-px-5.b62f44ed.png) ![](../../images/multi-samples-px-6.cd0893a6.png)

### # 全屏背景图

使用全屏背景图需要考虑到图片在不同尺寸的屏幕下是否都能有比较好的展示效果。 如果背景图片中有一些交互性或严格要求位置的部分，建议作为单独的元素与背景图拆分处理。

效果展示：

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/background-image1.2a4d84b2.png) ![](../../images/background-image2.d089c486.png) ![](../../images/background-image3.1f3b45a8.png)

### # 页面标题栏

页面标题通常位于页面顶部，在不同屏幕形状的设备上，需要考虑内容显示的美观性与完整性。通常在圆屏、胶囊屏等存在边缘剪切的设备上，标题栏会使用多行设计，保证顶部的展示内容长度不会超出屏幕；而在矩形屏幕上则做单行左右布局让整体设计更为舒展。

代码示例：

``` <template> <div class="demo-page"> <div class="title"> <text class="title-text">{{text1}}</text> <text class="title-text">{{text2}}</text> </div> </div> </template> <script> export default { private: { text1: '09:28', text2: '文案' } } </script> <style> .demo-page { justify-content: center; background-color: #5c5c5c; } .title { width: 90%; } .title-text { font-size: 36px; color: #fff; } @media (shape: circle){ .title { flex-direction: column; align-items: center; } } @media (shape: rect) { .title { margin-top: 10px; justify-content: space-between; align-items: flex-start; flex-direction: row-reverse; } .title-text { font-size: 46px; } } @media (shape: pill-shaped) { .title { flex-direction: column; align-items: center; } .title-text { font-size: 72px; } } </style> ```

效果展示：

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/multi-samples-title-c.2de8cb3c.png) ![](../../images/multi-samples-title-r.c870a816.png) ![](../../images/multi-samples-title-s.1ed37904.png)

## # 跨屏应用项目示例

### # 清单应用

圆形屏幕 / 矩形屏 / 胶囊屏

![](../../images/demo-todoList3.bc599d62.png) ![](../../images/demo-todoList1.e05993d0.png) ![](../../images/demo-todoList2.c71bb9dc.png)

项目地址：[点击下载 (opens new window)](<https://quickapp-vela.cnbj3-fusion.mi-fds.com/quickapp-vela/multi-screen-todoList.zip>)

### # 计算器

圆形屏幕 / 矩形屏

![](../../images/demo-calculator1.3cc79b1f.png) ![](../../images/demo-calculator2.93e7e7f6.png)

项目地址：[点击下载 (opens new window)](<https://quickapp-vela.cnbj3-fusion.mi-fds.com/quickapp-vela/multi-screen-calculator.zip>)
