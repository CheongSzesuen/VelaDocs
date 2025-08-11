<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/sensor.html -->

# # 传感器 sensor

## # 接口声明

``` { "name": "system.sensor" } ```

## # 导入模块

``` import sensor from '@system.sensor' // 或 const sensor = require('@system.sensor') ```

## # 接口定义

### # sensor.subscribePressure(OBJECT)

监听压力、压强感应数据。如果多次调用，仅最后一次调用生效

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
callback | Function | 是 | 每次位置信息发生变化，都会被回调  
  
#### # callback 返回值：

参数名 | 类型 | 说明  
---|---|---  
pressure | Number | 压力、压强，单位hpa，百帕。小数点后四舍五入保留五位小数  
  
#### # 示例：

``` sensor.subscribePressure({ callback: function(ret) { console.log(`handling callback, pressure = ${ret.pressure}`) } }) ```

### # sensor.unsubscribePressure()

取消压力、压强感应数据

#### # 参数：

无

#### # 示例：

``` sensor.unsubscribePressure() ```

### # sensor.subscribeAccelerometer(OBJECT)

监听加速度感应数据

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
interval | String | 否 | 监听加速度数据回调函数的执行频率，默认normal  
callback | Function | 是 | 重力感应数据变化后会回调此函数  
fail | Function | 否 | 订阅错误回调  
  
#### # interval 的合法值：

值 | 说明  
---|---  
game | 适用于更新游戏的回调频率，在 20ms/次 左右  
ui | 适用于更新 UI 的回调频率，在 60ms/次 左右  
normal | 普通的回调频率，在 200ms/次 左右  
  
#### # callback 返回值：

参数名 | 类型 | 说明  
---|---|---  
x | Integer | x 轴坐标  
y | Integer | y 轴坐标  
z | Integer | z 轴坐标  
  
#### # 示例：

``` sensor.subscribeAccelerometer({ callback: function(ret) { console.log(`handling callback, x = ${ret.x}, y = ${ret.y}, z = ${ret.z}`) }, fail: function(msg, code) { console.log(`handling callback, fail:`, msg, code) } }) ```

### # sensor.unsubscribeAccelerometer(OBJECT)

取消监听加速度感应数据

#### # 参数：

无

#### # 示例：

``` sensor.unsubscribeAccelerometer() ```

## # 支持明细

接口 | 已支持设备产品 | 不支持设备产品  
---|---|---  
subscribePressure | Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4 | 小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1、REDMI Watch 5  
unsubscribePressure | Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4 | 小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1、REDMI Watch 5  
subscribeAccelerometer | 小米手环 9、小米手环 9 Pro | Xiaomi Watch S3、小米 S1 Pro 运动健康手表、小米手环 8 Pro、Redmi Watch 4、Xiaomi Watch H1、Xiaomi Watch S4、REDMI Watch 5  
unsubscribeAccelerometer | 小米手环 9、小米手环 9 Pro | Xiaomi Watch S3、小米 S1 Pro 运动健康手表、小米手环 8 Pro、Redmi Watch 4、Xiaomi Watch H1、Xiaomi Watch S4、REDMI Watch 5
