<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/network.html -->

# # 网络信息 network

## # 接口声明

``` { "name": "system.network" } ```

## # 导入模块

``` import network from '@system.network' // 或 const network = require('@system.network') ```

## # 接口定义

### # network.getType(OBJECT)

获取网络类型

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调，可能是因为缺乏权限  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
type | String | 网络类型，可能的值为 2g，3g，4g，wifi，none，5g，bluetooth，others  
  
#### # 示例：

``` network.getType({ success: function(data) { console.log(`handling success: ${data.type}`) } }) ```

### # network.subscribe(OBJECT)

监听网络类型变化。如果多次调用，仅最后一次调用生效

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
callback | Function | 否 | 每次网络发生变化，都会被回调  
fail | Function | 否 | 失败回调，可能是因为缺乏权限  
  
#### # callback 返回值：

参数名 | 类型 | 说明  
---|---|---  
type | String | 网络类型，可能的值为 2g，3g，4g，wifi，none，5g，bluetooth，others。注：网络类型为 none 以外的值并不保证设备一定能访问到目标服务器，需要请求接口进行判断  
  
#### # 示例：

``` network.subscribe({ callback: function(data) { console.log('handling callback') } }) ```

### # network.unsubscribe()

取消监听网络类型变化

#### # 参数：

无

#### # 示例：

``` network.unsubscribe() ```

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
  
← [ 文件存储 file ](</vela/quickapp/zh/features/data/file.html>) [ 振动 vibrator ](</vela/quickapp/zh/features/system/vibrator.html>) → 

快速导航

接口声明

导入模块

接口定义

network.getType(OBJECT)

network.subscribe(OBJECT)

network.unsubscribe()

支持明细
