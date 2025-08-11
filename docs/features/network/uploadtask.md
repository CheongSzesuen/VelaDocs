<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/network/uploadtask.html -->

# # 上传 uploadtask[3+](</vela/quickapp/zh/guide/version/APILevel3>)

## # 接口声明

``` { "name": "system.uploadtask" } ```

## # 导入模块

``` import uploadtask from '@system.uploadtask' // 或 const uploadtask = require('@system.uploadtask') ```

## # 接口定义

### # 方法

### # UploadTask uploadtask.uploadFile(OBJECT)

创建一个上传请求，每次成功调用 uploadtask.uploadFile 将返回本次请求的 UploadTask 实例

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
url | String | 是 | 开发者服务器接口地址  
filePath | String | 是 | 要上传文件资源的路径 (本地路径)  
name | String | 是 | 文件对应的 key，开发者在服务端可以通过这个 key 获取文件的二进制内容  
header | Object | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分  
formData | Object | 否 | HTTP 请求中其他额外的 form data  
timeout | Number | 否 | 超时时间，单位为毫秒  
success | Function | 否 | 成功返回的回调函数  
fail | Function | 否 | 失败的回调函数  
complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行）  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
statusCode | Integer | 服务器状态 code  
data | String | 开发者服务器返回的数据  
headers | Object | 服务器 response 的所有 header  
  
# # UploadTask

## # 方法

### # UploadTask.abort()

中断上传任务

### # UploadTask.onProgressUpdate(callback)

监听上传进度变化事件

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
callback | Function | 是 | 上传进度变化事件的回调函数  
  
#### # callback 返回值：

参数名 | 类型 | 说明  
---|---|---  
progress | Number | 上传进度百分比  
totalBytesSent | Number | 已经上传的数据长度，单位 Bytes  
totalBytesExpectedToSend | Number | 预期需要上传的数据总长度，单位 Bytes  
  
### # UploadTask.offProgressUpdate(function callback)

取消监听上传进度变化事件。callback 是可选的，如果不传则取消所有通过 onProgressUpdate 监听的上传进度变化事件

#### # 示例：

``` const retUploadTask = uploadtask.uploadFile({ url: 'http://www.example.com', filePath: "internal://mass/download/test.png", name: "testImg", success: function(res){ console.log("Upload success.resp = " + JSON.stringify(res)) }, fail: function(data, code) { console.log(`handling fail, errMsg = ${data)}`) console.log(`handling fail, errCode = ${code}`) } }) // 中断请求任务 retUploadTask.abort() // 监听上传进度事件 retUploadTask.onProgressUpdate(res => { console.log( `listening upload progress update event, progressUpdate data = ${JSON.stringify(res)}` ) }) // 取消监听上传进度事件 retUploadTask.offProgressUpdate() ```

取消特定的上传进度事件

``` function cb(res) { console.log( `listening for upload progress update event 1, progressUpdate data = ${JSON.stringify( res )}` ) } // 此次监听会被取消 retUploadTask.onProgressUpdate(cb) // event2 监听依然有效，不会被取消 retUploadTask.onProgressUpdate((res) => { console.log( `listening for upload progress update event 2, progressUpdate data = ${JSON.stringify( res )}` ) }) retUploadTask.offProgressUpdate(cb) ```

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
