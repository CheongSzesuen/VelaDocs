<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/geolocation.html -->

# # 地理位置 geolocation

## # 接口声明

``` { "name": "system.geolocation" } ```

## # 导入模块

``` import geolocation from '@system.geolocation' // 或 const geolocation = require('@system.geolocation') ```

## # 接口定义

### # geolocation.getLocation(OBJECT)

获取地理位置

#### # 权限要求

精确设备定位

开发者需要在 manifest.json 里面配置权限：

``` { "permissions": [ { "name": "hapjs.permission.LOCATION" } ] } ```

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
timeout | Number | 否 | 设置超时时间，单位是 ms，默认值为 30000  
success | Function | 是 | 成功回调  
fail | Function | 否 | 失败回调，可能是因为缺乏权限  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
longitude | Number | 经度，小数点后四舍五入保留五位小数，下同  
latitude | Number | 纬度  
altitude | Number | 海拔、高度，单位m  
speed | Number | 速度值，单位m/s  
accuracy | Number | 精确度，值为正整数  
accuracyInfo | { horizontal: Number, vertical: Number } | 精确度信息，包含水平和垂直方向精准度  
  
#### # fail 返回错误代码：

错误码 | 说明  
---|---  
203 | 该功能不支持  
204 | 超时返回  
  
#### # 示例：

``` geolocation.getLocation({ success: function(data) { console.log( `handling success: longitude = ${data.longitude}, latitude = ${ data.latitude }, speed = ${data.speed}, altitude = ${data.altitude}` ) }, fail: function(data, code) { console.log(`handling fail, code = ${code}, errorMsg=${data}`) } }) ```

### # geolocation.subscribe(OBJECT)

监听地理位置。如果多次调用，仅最后一次调用生效

#### # 权限要求

精确设备定位

开发者需要在 manifest.json 里面配置权限：

``` { "permissions": [ { "name": "hapjs.permission.LOCATION" } ] } ```

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
callback | Function | 是 | 每次位置信息发生变化，都会被回调  
fail | Function | 否 | 失败回调  
  
#### # callback 返回值：

参数名 | 类型 | 说明  
---|---|---  
longitude | Number | 经度，小数点后四舍五入保留五位小数，下同  
latitude | Number | 纬度  
altitude | Number | 海拔、高度，单位m  
speed | Number | 速度值，单位m/s  
accuracy | Number | 精确度，值为正整数  
  
#### # fail 返回错误代码：

错误码 | 说明  
---|---  
203 | 该功能不支持  
  
#### # 示例：

``` geolocation.subscribe({ callback: function(data) { console.log( `handling success: longitude = ${data.longitude}, latitude = ${ data.latitude }, speed = ${data.speed}, altitude = ${data.altitude}` ) }, fail: function(data, code) { console.log(`handling fail, code = ${code}, errorMsg=${data}`) } }) ```

### # geolocation.unsubscribe()

取消监听地理位置

#### # 权限要求

精确设备定位

开发者需要在 manifest.json 里面配置权限：

``` { "permissions": [ { "name": "hapjs.permission.LOCATION" } ] } ```

#### # 参数：

无

#### # 示例：

``` geolocation.unsubscribe() ```

## # 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持
