<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/vibrator.html -->

# # 振动 vibrator

## # 接口声明

``` { "name": "system.vibrator" } ```

## # 导入模块

``` import vibrator from '@system.vibrator' // 或 const vibrator = require('@system.vibrator') ```

## # 接口定义

### # vibrator.vibrate(OBJECT)

触发振动

#### # 参数：

参数 | 类型 | 必填 | 说明  
---|---|---|---  
mode | String | 否 | 振动模式，"long"表示长振动，"short"表示短振动。默认为 long  
  
#### # 示例：

``` vibrator.vibrate({ mode: 'long' }) ```

### # vibrator.start(OBJECT)

开始振动

#### # 参数：

参数 | 类型 | 必填 | 说明  
---|---|---|---  
duration | Number | 是 | 振动持续时间(单位 ms)，必须为正整数  
interval | Number | 是 | 振动间隔时间(单位 ms)，必须为正整数  
count | Number | 是 | 振动次数，必须为正整数  
success | Function | 否 | 成功回调  
fail | Function | 否 | 失败回调  
complete | Function | 否 | 执行结束后的回调  
  
#### # success 返回值：

参数名 | 类型 | 说明  
---|---|---  
id | Number | 唯一的 ID，标识振动任务  
  
#### # fail 返回值：

错误码 | 说明  
---|---  
205 | 任务已存在  
202 | 参数错误  
  
#### # 示例：

``` vibrator.start({ duration: 1000, interval: 1000, count: 10, success: function (data) { console.log(`handling success, id = ${data.id}`) }, fail: function(data, code) { console.log(`handling fail, code = ${code}, errorMsg=${data}`) }, complete: function () { console.log(`handling complete`) } }) ```

### # vibrator.stop(Number)

停止振动

#### # 参数：

类型 | 必填 | 说明  
---|---|---  
Number | 是 | 振动任务 ID  
  
#### # 返回值：

类型 | 说明  
---|---  
Boolean | true：成功；false：失败  
  
#### # 示例：

``` vibrator.stop(1) ```

### # vibrator.getSystemDefaultMode()

获取系统默认振动模式

#### # 参数：

无

#### # 返回值：

类型 | 说明  
---|---  
Number | 0：关闭振动；1：标准振动；2：加强振动  
  
#### # 示例：

``` vibrator.getSystemDefaultMode() ```

## # 支持明细

接口 | 已支持设备产品 | 不支持设备产品  
---|---|---  
vibrate | 小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1、Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4、REDMI Watch 5 | -  
start | - | Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4、REDMI Watch 5、小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1  
stop | - | Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4、REDMI Watch 5、小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1  
getSystemDefaultMode | - | Xiaomi Watch S3、小米手环 9 Pro、Xiaomi Watch S4、REDMI Watch 5、小米 S1 Pro 运动健康手表、小米手环 8 Pro、小米手环 9、Redmi Watch 4、Xiaomi Watch H1
