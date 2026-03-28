<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/sensor.html -->

# 传感器 sensor

## 接口声明

```json
{ "name": "system.sensor" }
```

## 导入模块

```javascript
import sensor from '@system.sensor' 
// 或 
const sensor = require('@system.sensor')
```

## 接口定义

### 方法

### sensor.subscribePressure(OBJECT)

监听压力、压强感应数据。如果多次调用，仅最后一次调用生效

#### 参数：

参数名 | 类型 | 必填 | 说明
---|---|---|---
callback | Function | 是 | 每次位置信息发生变化，都会被回调 

#### callback 返回值：

参数名 | 类型 | 说明
---|---|---
pressure | Number | 压力、压强，单位hpa，百帕，浮点数 

#### 示例：

```javascript
sensor.subscribePressure({
  callback: function(ret) {
    console.log(`handling callback, pressure = ${ret.pressure}`)
  }
})
```

### sensor.unsubscribePressure()

取消压力、压强感应数据

#### 参数：

无

#### 示例：

```javascript
sensor.unsubscribePressure()
```

### sensor.subscribeAccelerometer(OBJECT)

监听加速度感应数据

#### 参数：

参数名 | 类型 | 必填 | 说明
---|---|---|---
interval | String | 否 | 监听加速度数据回调函数的执行频率，默认normal
callback | Function | 是 | 重力感应数据变化后会回调此函数
fail | Function | 否 | 订阅错误回调 

#### interval 的合法值：

值 | 说明
---|---
game | 适用于更新游戏的回调频率，在 20ms/次 左右
ui | 适用于更新 UI 的回调频率，在 60ms/次 左右
normal | 普通的回调频率，在 200ms/次 左右 

#### callback 返回值：

参数名 | 类型 | 说明
---|---|---
x | Number | x 轴坐标
y | Number | y 轴坐标
z | Number | z 轴坐标 

#### 示例：

```javascript
sensor.subscribeAccelerometer({
  callback: function(ret) {
    console.log(`handling callback, x = ${ret.x}, y = ${ret.y}, z = ${ret.z}`)
  },
  fail: function(msg, code) {
    console.log(`handling callback, fail:`, msg, code)
  }
})
```

### sensor.unsubscribeAccelerometer()

取消监听加速度感应数据

#### 参数：

无

#### 示例：

```javascript
sensor.unsubscribeAccelerometer()
```

### sensor.subscribeCompass(OBJECT)

监听罗盘数据。如果多次调用，仅最后一次调用生效

#### 参数：

参数名 | 类型 | 必填 | 说明
---|---|---|---
callback | Function | 是 | 罗盘数据变化后会回调此函数
fail | Function | 否 | 订阅失败回调 

#### callback 返回值：

参数名 | 类型 | 说明
---|---|---
direction | Number | 表示设备的 y 轴和地球磁场北极之间的角度，当面朝北，角度为 0；朝南角度为 π；朝东角度 π/2；朝西角度-π/2
accuracy | Number | 精度，详见compass精度说明 

#### fail 返回错误代码：

错误码 | 说明
---|---
1000 | 当前设备不支持罗盘传感器 

#### 示例：

```javascript
sensor.subscribeCompass({
  callback: function (res) {
    console.log(`handling subscribeCompass callback, direction = ${res.direction}, accuracy = ${res.accuracy}`)
  },
  fail: function (data, code) {
    console.log(`handling subscribeCompass fail, code = ${code}`)
  }
})
```

### sensor.unsubscribeCompass()

取消监听加速度感应数据

#### 参数：

无

#### 示例：

```javascript
sensor.unsubscribeCompass()
```

### compass精度说明：

值 | 说明
---|---
3 | 高精度
2 | 中等精度
1 | 低精度
-1 | 不可信，传感器失去连接
0 | 不可信，原因未知 

## 支持明细

接口 | 已支持设备产品 | 不支持设备产品
---|---|---
subscribePressure | Xiaomi Watch S3、小米手环 9 Pro、小米手环 10、Xiaomi Watch S4、Xiaomi Watch S5 | 小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1、REDMI Watch 5、REDMI Watch 6
unsubscribePressure | Xiaomi Watch S3、小米手环 9 Pro、小米手环 10、Xiaomi Watch S4、Xiaomi Watch S5 | 小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1、REDMI Watch 5、REDMI Watch 6
subscribeAccelerometer | 小米手环 9 / 9 Pro、小米手环 10、Xiaomi Watch S5 | Xiaomi Watch S3、小米 S1 Pro 运动健康手表、小米手环 8 Pro、Redmi Watch 4、Xiaomi Watch H1、Xiaomi Watch S4、REDMI Watch 5、REDMI Watch 6
unsubscribeAccelerometer | 小米手环 9 / 9 Pro、小米手环 10、Xiaomi Watch S5 | Xiaomi Watch S3、小米 S1 Pro 运动健康手表、小米手环 8 Pro、Redmi Watch 4、Xiaomi Watch H1、Xiaomi Watch S4、REDMI Watch 5、REDMI Watch 6
subscribeCompass / unsubscribeCompass | Xiaomi Watch S4、REDMI Watch 5 、REDMI Watch 6、Xiaomi Watch S5 | 其余小米环表设备
