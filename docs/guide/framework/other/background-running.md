<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/other/background-running.html -->

# # 后台运行

为了节省系统资源，通常情况下，应用切换到后台后将会停止运行，等到再次切换回前台时重新运行。但音乐\运动等类型的应用，退到后台后可能仍然需要继续运行，为满足此类需求，加入了对后台运行的支持。后台运行模式的工作原理如下：

在应用切换到后台时，系统将会检查是否满足后台运行的条件，如果满足，应用将继续运行，否则将被停止。此条件包括：

  1. `manifest.json`中声明了后台运行接口

  2. 当前至少有一个（已在`manifest.json`中声明的）后台运行接口正在运行

实践建议：

  * 后台运行需要消耗较多的系统资源，应用需要根据自身需求审慎使用。针对申请后台运行的应用，上线审核时将会审核其后台运行的需求是否合理。
  * 后台运行接口的导入和后台执行的工作放到`app.ux`中，而不是放到页面中，以免避免页面切换和销毁的影响。

## # 配置方法

manifest.json 中声明所需的后台运行接口。后台运行接口包括：

  1. 音频播放： `system.audio`
  2. 上传下载： `system.request`
  3. 地理位置： `system.geolocation`

``` { "package": "com.hybrid.demo.sample", // ...... "config": { "logLevel": "trace", "background": { "features":[ "system.audio", "system.request" ] } } // ...... } ```
