<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/other/faq.html -->

# # 常见问题

## # 如何适配不同尺寸的屏幕？

框架默认的屏幕分辨率是480*480，Vela三方应用会自动适配，开发者可以直接按照设计稿的尺寸来开发。 比如，设计稿是466*466，可以在`manifest.json`中配置`designWidth: 466`，然后css中尺寸相关的数值跟设计稿保持一致即可。 更多详细细节信息可以参考：[页面样式和布局](</vela/quickapp/zh/guide/framework/style/page-style-and-layout.html>)。

## # 模拟器怎么跟手表通信？

模拟器跟手机通讯，需要外接蓝牙适配器，并且配置比较复杂，建议使用真机调试。

## # 如何解决通信过程中提示签名不正确的问题？

手表和手机通信前会检查应用的签名，如果签名不正确通信会被拒绝。所以调试通信时需要手机app和手表rpk使用配套的证书打包。  
遇到签名不正确的错误时，请检查导出rpk时使用的证书是否和打包手机app时的证书相同。

## # 如何排查通信(interconnect)相关的问题？

首先检查手表端发送数据的数据结构是否正确（请参考发送数据）、send方法回调行数执行情况。 其次可以排查手机端打印的日志（使用adb logcat工具），看手机端接受的数据情况。

## # 如何解决列表数据更新时闪烁的问题？

通过for循环渲染的列表，在数据更新时，如果出现闪烁，可以增加tid来解决。详细文档可以参考：[循环指令](</vela/quickapp/zh/guide/framework/template/for.html>)。

## # 构建release版本rpk时打包证书有什么要求？

  1. 如果涉及手表跟手机通信，打包rpk时的证书需要跟打包手机app的证书一致，否则无法通信；
  2. 如果不涉及通信，对证书无特殊要求，按照文档中的步骤生成即可；

> 注意：请妥善保管证书，并且保证每次使用相同的证书打release版本rpk包。如果证书改变，可能无法上架。

## # 如何解决手表和手机连接状态获取问题？

进入页面直接获取状态往往会拿到`DISCONNECTED`，因此需要轮询获取状态，根据`getApkStatus()`的返回值，判断手表和手机的连接状态。

## # 模拟器支持哪些平台？

模拟器支持Windows，Mac和Ubuntu三个平台，其中Windows支持Win10+，Mac支持macOS12+

## # Windows和Mac是否可以打包rpk？

Windows和Mac可以打包rpk。

## # 如何将rpk上传到手表真机运行?

  1. 手机安装小米运动健康(目前是通过商务拉群对接的方式提供。开发vela三方应用需求，请邮件联系常健：[changjian@xiaomi.com](<mailto:changjian@xiaomi.com>))；
  2. 点击【小米运动健康】-->【我的】-->【关于】-->【Debug】；
  3. 点击【第三方应用】；
  4. 点击【Click to input package name】；
  5. 随便输个字符（只有卸载时要详细包名）；
  6. 选择【Install third app】；
  7. 选择本地rpk文件安装；
  8. 安装成功会有Toast提示。

## # 如何查看手表真机上的日志？

  1. 手机安装小米运动健康(目前是通过商务拉群对接的方式提供。开发vela三方应用需求，请邮件联系常健：[changjian@xiaomi.com](<mailto:changjian@xiaomi.com>))；
  2. 小米运动健康与手表进行同步；
  3. 在手表上复现问题；
  4. 点击【小米运动健康】-->【我的】-->【关于】-->【Debug】-->【拉取固件日志】；
  5. 拉取成功后保存在手机，日志文件目录: `/sdcard/Android/data/com.mi.health/files/log`。

