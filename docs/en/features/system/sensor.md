<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/sensor.html -->

# Sensor

## Interface Declaration

```json
{ "name": "system.sensor" }
```

## Import Module

```javascript
import sensor from '@system.sensor' 
// or 
const sensor = require('@system.sensor')
```

## Interface Definition

### Methods

### sensor.subscribePressure(OBJECT)

Listens for pressure sensor data. If called multiple times, only the last call takes effect.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Called back each time the positional information changes  
  
#### Callback Return Value:

Parameter | Type | Description  
---|:---:|---  
pressure | Number | Pressure, in hPa (hectopascals), floating-point number  
  
#### Example:

```javascript
sensor.subscribePressure({
  callback: function(ret) {
    console.log(`handling callback, pressure = ${ret.pressure}`)
  }
})
```

### sensor.unsubscribePressure()

Cancels listening for pressure sensor data.

#### Parameters:

None

#### Example:

```javascript
sensor.unsubscribePressure()
```

### sensor.subscribeAccelerometer(OBJECT)

Listens for accelerometer data.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
interval | String | No | Frequency at which the accelerometer data callback function is executed. Default is "normal".  
callback | Function | Yes | Called back when gravity sensor data changes  
fail | Function | No | Callback for subscription errors  
  
#### Valid Values for interval:

Value | Description  
---|---  
game | Suitable for game update callback frequency, approximately 20ms per call  
ui | Suitable for UI update callback frequency, approximately 60ms per call  
normal | Normal callback frequency, approximately 200ms per call  
  
#### Callback Return Value:

Parameter | Type | Description  
---|:---:|---  
x | Number | X-axis coordinate  
y | Number | Y-axis coordinate  
z | Number | Z-axis coordinate  
  
#### Example:

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

Cancels listening for accelerometer data.

#### Parameters:

None

#### Example:

```javascript
sensor.unsubscribeAccelerometer()
```

### sensor.subscribeCompass(OBJECT)

Listens for compass data. If called multiple times, only the last call takes effect.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
callback | Function | Yes | Called back when compass data changes  
fail | Function | No | Callback for subscription failure  
  
#### Callback Return Value:

Parameter | Type | Description  
---|:---:|---  
direction | Number | Angle between the device's y-axis and magnetic north. When facing north, the angle is 0; when facing south, it is π; when facing east, it is π/2; when facing west, it is -π/2  
accuracy | Number | Accuracy, see compass accuracy description for details  
  
#### Error Codes Returned by fail:

Error Code | Description  
---|---  
1000 | Current device does not support compass sensor  
  
#### Example:

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

Cancels listening for compass data.

#### Parameters:

None

#### Example:

```javascript
sensor.unsubscribeCompass()
```

### Compass Accuracy Description:

Value | Description  
---|---  
3 | High accuracy  
2 | Medium accuracy  
1 | Low accuracy  
-1 | Unreliable, sensor disconnected  
0 | Unreliable, reason unknown  
  
## Support Details

Interface | Supported Device Products | Unsupported Device Products  
---|:---:|---  
subscribePressure | Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Band 10, Xiaomi Watch S4 | Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1, REDMI Watch 5, REDMI Watch 6  
unsubscribePressure | Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Band 10, Xiaomi Watch S4 | Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1, REDMI Watch 5, REDMI Watch 6  
subscribeAccelerometer | Xiaomi Band 9 / 9 Pro, Xiaomi Band 10 | Xiaomi Watch S3, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Redmi Watch 4, Xiaomi Watch H1, Xiaomi Watch S4, REDMI Watch 5, REDMI Watch 6  
unsubscribeAccelerometer | Xiaomi Band 9 / 9 Pro, Xiaomi Band 10 | Xiaomi Watch S3, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Redmi Watch 4, Xiaomi Watch H1, Xiaomi Watch S4, REDMI Watch 5, REDMI Watch 6  
subscribeCompass / unsubscribeCompass | Xiaomi Watch S4, REDMI Watch 5, REDMI Watch 6 | Other Xiaomi band and watch devices
