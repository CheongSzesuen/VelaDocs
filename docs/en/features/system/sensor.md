<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/sensor.html -->

# Sensor

## Interface Declaration
```json
{ "name" : "system.sensor" }
```

## Import Module
```javascript
import sensor from '@system.sensor' // or const sensor = require('@system.sensor')
```

## Interface Definition

### sensor.subscribePressure(OBJECT)

Listens for pressure sensor data. If called multiple times, only the last call will take effect.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Called back each time the position information changes  
  
#### Callback Return Value:

Parameter Name | Type | Description  
---|:---:|---  
pressure | Number | Pressure, in hpa (hectopascals). Rounded to five decimal places  
  
#### Example:
```javascript
sensor.subscribePressure({ callback : function(ret){ console.log(` handling callback, pressure = ${ ret.pressure } `)} })
```

### sensor.unsubscribePressure()

Cancels pressure sensor data listening.

#### Parameters:

None

#### Example:
```javascript
sensor.unsubscribePressure()
```

### sensor.subscribeAccelerometer(OBJECT)

Listens for accelerometer sensor data.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
interval | String | No | The execution frequency of the callback function for listening to accelerometer data. Default is normal.  
callback | Function | Yes | This function is called back when gravity sensor data changes.  
fail | Function | No | Callback for subscription errors.  
  
#### Valid Values for interval:

Value | Description  
---|---  
game | Suitable callback frequency for updating games, around 20ms per call.  
ui | Suitable callback frequency for updating UI, around 60ms per call.  
normal | Normal callback frequency, around 200ms per call.  
  
#### Callback Return Value:

Parameter Name | Type | Description  
---|:---:|---  
x | Integer | X-axis coordinate  
y | Integer | Y-axis coordinate  
z | Integer | Z-axis coordinate  
  
#### Example:
```javascript
sensor.subscribeAccelerometer({ callback : function(ret){ console.log(` handling callback, x = ${ ret.x } , y = ${ ret.y } , z = ${ ret.z } `)} , fail : function(msg , code){ console.log(` handling callback, fail: ` , msg , code)} })
```

### sensor.unsubscribeAccelerometer(OBJECT)

Cancels listening for accelerometer sensor data.

#### Parameters:

None

#### Example:
```javascript
sensor.unsubscribeAccelerometer()
```

## Support Details

Interface | Supported Device Products | Unsupported Device Products  
---|:---:|---  
subscribePressure | Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4 | Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1, REDMI Watch 5  
unsubscribePressure | Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4 | Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1, REDMI Watch 5  
subscribeAccelerometer | Xiaomi Band 9, Xiaomi Band 9 Pro | Xiaomi Watch S3, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Redmi Watch 4, Xiaomi Watch H1, Xiaomi Watch S4, REDMI Watch 5  
unsubscribeAccelerometer | Xiaomi Band 9, Xiaomi Band 9 Pro | Xiaomi Watch S3, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Redmi Watch 4, Xiaomi Watch H1, Xiaomi Watch S4, REDMI Watch 5
