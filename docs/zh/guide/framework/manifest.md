<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/manifest.html -->

# 项目配置

`manifest.json`文件中包含了应用描述、接口声明、页面路由信息。

## manifest

属性 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
package | String |:---:| 是 | 应用包名，**确认与原生应用的包名不一致** ，推荐采用 com.company.module 的格式，如：com.example.demo  
name | String |:---:| 是 | 应用名称，**6 个汉字以内，与应用商店保存的名称一致** ，用于在桌面图标、弹窗等处显示应用名称  
icon | String |:---:| 是 | 应用图标，提供 192x192 大小的即可  
versionName | String |:---:| 否 | 应用版本名称，如："1.0"  
versionCode | Integer |:---:| 是 | 应用版本号，从`1`自增，**推荐每次重新上传包时`versionCode`+1**  
minAPILevel | Integer | 1 | 否 | 支持的最小 API 标准版本号，**兼容性检查，避免上线后在低版本平台运行并导致不兼容** ；如果不填按照内测版本处理  
features | Array |:---:| 否 | 接口列表，绝大部分接口都需要在这里声明，否则不能调用，详见每个接口的文档说明  
config | Object |:---:| 是 | 系统配置信息，详见下面说明  
router | Object |:---:| 是 | 路由信息，详见下面说明  
display | Object |:---:| 否 | UI 显示相关配置，详见下面说明  
deviceTypeList | Array<String> | watch | 否 | 可选值有：watch、tv、car、phone，现只支持watch  
permissions | Array |:---:| 否 | 权限申请，示例：[{ "name": "hapjs.permission.LOCATION" }]  
  
### config

用于定义系统配置和全局数据。

属性 | 类型 | 默认值 | 描述  
---|:---:|---|---  
logLevel | String | log | 打印日志等级，分为 off、error、warn、info、log、debug  
designWidth | Integer |:---:| 页面设计基准宽度，根据实际设备宽度来缩放元素大小  
background | Object |:---:| 后台运行配置信息，可使用 features 字段申请需要在后台使用的接口（同时仍需在最外层的 features 字段中声明）。可申请的接口为：  
system.audio   
system.geolocation   
system.request 等   
详细用法参见 [后台运行](</vela/quickapp/zh/guide/framework/other/background-running.html>) 脚本  
  
### minAPILevel

支持的最小 API 标准版本号，标识开发者的 rpk 包能兼容运行在最小实现了该版本 API 标准的设备上，其值默认为1。当使用了 1 及以上的 API 标准版本新增特性时，就必须确保 minAPILevel 最低为该版本号，避免上线后在实现了更低版本 API 标准的设备上运行出错。

示例如下：
```json
{ "minAPILevel" : 1 }
```

### router

用于定义页面的组成和相关配置信息，如果页面没有配置路由信息，则在编译打包时跳过。

属性 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
entry | String |:---:| 是 | 首页名称，使用分包功能时，建议将首页定义在基础包  
pages | Object |:---:| 是 | 页面配置列表，key 值为页面名称（对应页面目录名，例如 Hello 对应'Hello'目录），value 为页面详细配置 page，详见下面说明  
  
示例代码：
```json
"router" : { "entry" : "Demo" , "pages" : { "Demo" : { "component" : "index" } } }
```

#### router.pages

用于定义单个页面路由信息。

属性 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
component | String |:---:| 是 | 页面对应的组件名，与 ux 文件名保持一致，例如"hello" 对应 "hello.ux"  
path | String | /<页面名称> | 否 | 页面路径，例如"/user",不填则默认为/<页面名称>  
path 必须唯一，不能和其他 page 的 path 相同  
下面 page 的 path 因为缺失，会被设置为"/Index"：  
`"Index": {"component": "index"}`  
launchMode | String | standard | 否 | 声明页面的启动模式，支持"singleTask"，"standard"两种页面启动模式  
标识为"singleTask"模式时每次打开目标页面都会打开已有的目标页面并回调 onRefresh 生命周期函数，清除该页面上打开的其他页面，没有打开过此页面时会创建新的目标页面实例  
标识为"standard"模式时会每次打开新的目标页面（多次打开目标页面地址时会存在多个相同页面）  
  
### 示例代码
```json
{ "package" : "com.company.unit" , "name" : "appName" , "icon" : "/Common/icon.png" , "versionName" : "1.0" , "versionCode" : 1 , "minPlatformVersion" : 1000 , "features" : [ { "name" : "system.network" } ] , "router" : { "entry" : "Hello" , "pages" : { "Hello" : { "component" : "hello" , "path" : "/" } } } }
```

### display

用于定义与 UI 显示相关的配置。

如果在 display 对象下定义以下属性值，则生效范围为此JS 应用全部页面；

属性 | 类型 | 默认值 | 描述  
---|:---:|---|---  
backgroundColor | String | #ffffff | 窗口背景颜色  
  
### 权限说明

权限名 | feature | api | 描述 | 权限错误码  
---|:---:|---|:---:|---  
hapjs.permission.LOCATION | system.geolocation | getLocation   
subscribe   
unsubscribe | 地理位置 | 400： 拒绝授予权限   
402： 权限错误（未声明该权限）  
hapjs.permission.DEVICE_INFO | system.device | getSerial   
getDeviceId | 获取设备信息 | 400： 拒绝授予权限   
402： 权限错误（未声明该权限）
