<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/event.html -->

# Event4+

## Interface Declaration
```json
{ "name" : "system.event" }
```

## Import Module
```javascript
import event from '@system.event' // or const event = require('@system.event')
```

## Interface Definition

### event.publish (OBJECT)

Publish a public event.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
eventName | String | Yes | Event name. Reserved names for public events are occupied by the system. Do not use them.  
options | Object | No | Event parameters  
  
#### options Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
params | Object | No | Event parameters  
permissions | Array | No | Permissions of subscribers. Only packages with permissions can receive the sent event.  
  
#### Public Events Supported by the System:

System Internal Event Name | Permissions Required for Subscribers | Description  
---|:---:|---  
usual.event.BATTERY_CHANGED | None | Battery level changed. Parameter: level: between 0.0 and 1.0  
usual.event.DISCHARGING | None | Charging stopped  
usual.event.CHARGING | None | Charging started  
  
#### Return Value:

None

#### Example:
```javascript
event.publish({ eventName : 'myEventName' , options : { params : { age : 10 , name : 'peter' } , permissions : [ 'com.example.demo' ] } })
```

### event.subscribe(OBJECT)

Subscribe to a public event.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
eventName | String | Yes | Event name  
callback | Function | Yes | Callback function  
  
#### Callback Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
params | Object | No | Event parameters  
package | String | No | Package name of the event sender  
  
#### Return Value:

Type | Required | Description  
---|:---:|---  
Number | Yes | Event ID. Returns undefined if subscription fails.  
  
#### Example:
```javascript
const evtId = event.subscribe({ eventName : 'myEventName' , callback : function(res){ if(res.package === 'com.example.demo'){ console.log(res.params)} } })console.log(evtId)
```

### event.unsubscribe(OBJECT)

Unsubscribe from a public event.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
id | Number | Yes | Subscription ID  
  
#### Example:
```javascript
const evtId = event.subscribe({ eventName : 'myEventName' , callback : function(res){ if(res.package === 'com.example.demo'){ console.log(res.params)} } })event.unsubscribe({ id : evtId })
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Not supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG and Blood Pressure Monitor | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
