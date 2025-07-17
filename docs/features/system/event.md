<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/system/event.html -->

# # 事件 event[4+](</vela/quickapp/zh/guide/version/APILevel4>)

## # 接口声明

``` { "name": "system.event" } ```

## # 导入模块

``` import event from '@system.event' // 或 const event = require('@system.event') ```

## # 接口定义

### # event.publish (OBJECT)

发布公共事件

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
eventName | String | 是 | 事件名称，公共事件保留名称被系统占用，请勿使用  
options | Object | 否 | 事件参数  
  
#### # options 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
params | Object | 否 | 事件参数  
permissions | Array | 否 | 订阅者的权限，拥有权限的包才能收到发送的事件  
  
#### # 系统支持的公共事件：

系统内部事件名称 | 订阅者所需权限 | 说明  
---|---|---  
usual.event.BATTERY_CHANGED | 无 | 电量改变，参数：level:0.0 - 1.0 之间  
usual.event.DISCHARGING | 无 | 停止充电  
usual.event.CHARGING | 无 | 开始充电  
  
#### # 返回值：

无

#### # 示例：

``` event.publish({ eventName: 'myEventName', options: { params: { age: 10, name: 'peter' }, permissions: ['com.example.demo'] } }) ```

### # event.subscribe(OBJECT)

订阅公共事件

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
eventName | String | 是 | 事件名称  
callback | Function | 是 | 回调函数  
  
#### # 回调参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
params | Object | 否 | 事件参数  
package | String | 否 | 事件推送者包名  
  
#### # 返回值：

类型 | 必填 | 说明  
---|---|---  
Number | 是 | 事件id，订阅失败返回undefined  
  
#### # 示例：

``` const evtId = event.subscribe({ eventName: 'myEventName', callback: function(res) { if (res.package === 'com.example.demo') { console.log(res.params) } } }) console.log(evtId) ```

### # event.unsubscribe(OBJECT)

取消订阅公共事件

#### # 参数：

参数名 | 类型 | 必填 | 说明  
---|---|---|---  
id | Number | 是 | 订阅id  
  
#### # 示例：

``` const evtId = event.subscribe({ eventName: 'myEventName', callback: function(res) { if (res.package === 'com.example.demo') { console.log(res.params) } } }) event.unsubscribe({ id: evtId }) ```

## # 支持明细

设备产品 | 说明  
---|---  
小米 S1 Pro 运动健康手表 | 不支持  
小米手环 8 Pro | 不支持  
Xiaomi Watch S3 | 不支持  
Redmi Watch 4 | 不支持  
小米腕部心电血压记录仪 | 不支持  
Xiaomi Watch S4 | 支持  
REDMI Watch 5 | 支持  
  
← [ 传感器 sensor ](</vela/quickapp/zh/features/system/sensor.html>) [ 电量信息 battery ](</vela/quickapp/zh/features/system/battery.html>) → 

快速导航

接口声明

导入模块

接口定义

event.publish (OBJECT)

event.subscribe(OBJECT)

event.unsubscribe(OBJECT)

支持明细
