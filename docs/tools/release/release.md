<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/tools/release/release.html -->

# 发布应用

不同于顶部按钮区域的打包按钮，点击`发布`按钮发布应用，将生成**release** 包。

**release** 包是为了发布到生产环境而设计的，因此它会进行更严格的优化，以减少文件大小和加载时间。通常情况下，release 只包含必要的文件和代码，会删除所有的调试信息、注释和未使用的代码，以减小文件大小并提高性能。

同时，在生成release包前，会检查当前目录下是否**包含签名文件** ，如果没有会进入创建签名页面，按提示点击完成即可创建签名文件。

![alt text](../../images/ide-debug-11.73c430b2.gif)

签名文件**创建成功** 后，再次**点击发布** 即可创建release包。

![alt text](../../images/ide-debug-12.5740fefa.png)
