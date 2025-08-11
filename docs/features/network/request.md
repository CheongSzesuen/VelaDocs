<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/network/request.html -->

# # 下载 request

## # 接口声明

``` { "name": "system.request" } ```

## # 导入模块

``` import request from '@system.request' // 或 const request = require('@system.request') ```

## # 接口定义

### # request.download(OBJECT)

下载文件

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
url | String | 是 | 资源 url  
header | String | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分  
filename | String | 否 | 下载文件名。默认从网络请求或 url 中获取  
success | Function | 否 | 成功返回的回调函数  
fail | Function | 否 | 失败的回调函数  
complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行）  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
token | String | 下载的 token，根据此 token 获取下载状态  
  
#### # 示例：

``` request.download({ url: 'http://www.example.com', success: function(data) { console.log(`handling success${data.token}`) }, fail: function(data, code) { console.log(`handling fail, code = ${code}`) } }) ```

### # request.onDownloadComplete(OBJECT)

监听下载任务

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
token | String | 是 | download 接口返回的 token  
success | Function | 否 | 成功返回的回调函数  
fail | Function | 否 | 失败的回调函数  
complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行）  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
uri | String | 下载文件的 Uri（默认情况下该文件处于应用缓存目录。如果文件类型为图片或者视频且要求用户可以在相册等应用内查看，则需要将该文件转存至公共目录，参考media接口中的方法实现即可）  
  
#### # fail 返回错误代码：

错误码 | 说明  
---|---  
1000 | 下载失败  
1001 | 下载任务不存在  
  
#### # 示例：

``` request.onDownloadComplete({ token: '123', success: function(data) { console.log(`handling success${data.uri}`) }, fail: function(data, code) { console.log(`handling fail, code = ${code}`) } }) ```

## # 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持
