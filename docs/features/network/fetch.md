<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/network/fetch.html -->

# # 数据请求 fetch

## # 接口声明

``` { "name": "system.fetch" } ```

## # 导入模块

``` import fetch from '@system.fetch' // 或 const fetch = require('@system.fetch') ```

## # 接口定义

### # fetch.fetch(OBJECT)

获取网络数据

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
url | String | 是 | 资源 url  
data | String/Object/ArrayBuffer | 否 | 请求的参数，可以是字符串，或者是 js 对象、arraybuffer 对象。参考 `data与Content-Type关系` 部分  
header | Object | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分。User-Agent 设置示例：{"Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,en-US;q=0.8,en;q=0.6"}  
method | String | 否 | 默认为 GET，可以是：OPTIONS，GET，HEAD，POST，PUT，DELETE，TRACE，CONNECT  
responseType | String | 否 | 支持返回类型是 text，json，file，arraybuffer，默认会根据服务器返回 header 中的 Content-Type 确定返回类型，详见 `success返回值`  
success | Function | 否 | 成功返回的回调函数  
fail | Function | 否 | 失败的回调函数，可能会因为权限失败  
complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行）  
  
#### # data 与 Content-Type 关系

data | Content-Type | 说明  
---|---|---  
String | 不设置 | Content-Type 默认为 text/plain，data 值作为请求的 body  
String | 任意 Type | data 值作为请求的 body  
Object | 不设置 | Content-Type 默认为 application/x-www-form-urlencoded，data 按照 url 规则进行 encode 拼接作为请求的 body  
Object | application/x-www-form-urlencoded | data 按照 url 规则进行 encode 拼接作为请求的 body  
Object | application/x-www-form-urlencoded 之外的任意 type | -  
ArrayBuffer | 不设置 | Content-Type 默认为 application/octet-stream，data 值作为请求的 body  
ArrayBuffer | 任意 Type | data 值作为请求的 body  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
code | Integer | 服务器状态 code  
data | String/Object /ArrayBuffer | 参考 `responseType与success中data关系` 部分  
headers | Object | 服务器 response 的所有 header  
  
#### # responseType 与 success 中 data 关系：

responseType | data | 说明  
---|---|---  
无 | String | 服务器返回的 header 中 type 是 text/*或 application/json、application/javascript、application/xml，值是文本内容，否则是存储的临时文件的 uri，临时文件如果是图片或者视频内容，可以将图片设置到 image  
text | String | 返回普通文本  
json | Object | 返回 js 对象  
file | String | 返回存储的临时文件的 uri  
arraybuffer | ArrayBuffer | 返回 ArrayBuffer 对象  
  
#### # 示例：

``` fetch.fetch({ url: 'http://www.example.com', responseType: 'text', success: function(response) { console.log(`the status code of the response: ${response.code}`) console.log(`the data of the response: ${response.data}`) console.log( `the headers of the response: ${JSON.stringify(response.headers)}` ) }, fail: function(data, code) { console.log(`handling fail, errMsg = ${data}`) console.log(`handling fail, errCode = ${code}`) } }) // 我们也可以使用promise的方式处理回调 fetch .fetch({ url: 'http://www.example.com', responseType: 'text' }) .then(res => { const result = res.data console.log(`the status code of the response: ${result.code}`) console.log(`the data of the response: ${result.data}`) console.log( `the headers of the response: ${JSON.stringify(result.headers)}` ) }) .catch(error => { console.log(`handling fail, errMsg = ${error.data}`) console.log(`handling fail, errCode = ${error.code}`) }) ```

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
  
← [ 应用配置 configuration ](</vela/quickapp/zh/features/basic/configuration.html>) [ 设备通信 interconnect ](</vela/quickapp/zh/features/network/interconnect.html>) → 

快速导航

接口声明

导入模块

接口定义

fetch.fetch(OBJECT)

支持明细
