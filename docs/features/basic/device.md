<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/basic/device.html -->

# # 设备信息 device

## # 接口声明

``` { "name": "system.device" } ```

## # 导入模块

``` import device from '@system.device' // 或 const device = require('@system.device') ```

## # 接口定义

### # device.getInfo(OBJECT)

获取设备信息

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数值 | 类型 | 说明  
---|---|---  
brand | string | 设备品牌  
manufacturer | string | 设备生产商  
model | string | 设备型号  
product | string | 设备代号  
osType | string | 操作系统名称  
osVersionName | string | 操作系统版本名称  
osVersionCode | number | 操作系统版本号  
platformVersionName | string | 运行平台版本名称  
platformVersionCode | number | 运行平台版本号  
language | string | 系统语言  
region | string | 系统地区  
APILevel[2+](</vela/quickapp/zh/guide/version/APILevel2>) | number | 框架api版本  
screenWidth | number | 屏幕宽  
screenHeight | number | 屏幕高  
screenDensity[3+](</vela/quickapp/zh/guide/version/APILevel3>) | number | 屏幕密度，即：设备像素比（device pixel ratio），是设备物理像素和逻辑像素（DP）的比值，其计算公式为：DPR = 设备 PPI / 160，PPI（pixels per inch）表示每英寸的像素数  
screenShape | string | 屏幕形状，可取值：rect 表示方形屏，circle 表示圆形屏，pill-shaped[3+](</vela/quickapp/zh/guide/version/APILevel3>) 表示胶囊形屏  
deviceType[2+](</vela/quickapp/zh/guide/version/APILevel2>) | string | 设备类型，可取值：watch、band、smartspeaker  
  
#### # 示例：

``` device.getInfo({ success: function(ret) { console.log(`handling success， brand = ${ret.brand}`) } }) ```

### # device.getDeviceId(OBJECT)

获取设备唯一标识

#### # 权限要求

获取设备信息

开发者需要在 manifest.json 里面配置权限：

``` { "permissions": [ { "name": "hapjs.permission.DEVICE_INFO" } ] } ```

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数值 | 类型 | 说明  
---|---|---  
deviceId | String | 设备唯一标识  
  
#### # 示例：

``` device.getDeviceId({ success: function (data) { console.log(`handling success: ${data.deviceId}`) }, fail: function (data, code) { console.log(`handling fail, code = ${code}`) }, }) ```

### # device.getSerial(OBJECT)

获取设备序列号

#### # 权限要求

获取设备信息

开发者需要在 manifest.json 里面配置权限：

``` { "permissions": [ { "name": "hapjs.permission.DEVICE_INFO" } ] } ```

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数值 | 类型 | 说明  
---|---|---  
serial | String | 设备序列号  
  
``` device.getSerial({ success: (data) => { console.log(`handling success: ${data.serial}`) }, fail: (data, code) => { console.log(`handling fail, code = ${code}`) } }) ```

### # device.getTotalStorage(OBJECT)

获取存储空间的总大小

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数值 | 类型 | 说明  
---|---|---  
totalStorage | Number | 存储空间的总大小，单位是 Byte  
  
``` device.getTotalStorage({ success: (data) => { console.log(`handling success: ${data.totalStorage}`) }, fail: (data, code) => { console.log(`handling fail, code = ${code}`) } }) ```

### # device.getAvailableStorage(OBJECT)

获取存储空间的可用大小

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数值 | 类型 | 说明  
---|---|---  
availableStorage | Number | 存储空间的可用大小，单位是 Byte  
  
``` device.getAvailableStorage({ success: (data) => { console.log(`handling success: ${data.availableStorage}`) }, fail: (data, code) => { console.log(`handling fail, code = ${code}`) } }) ```
