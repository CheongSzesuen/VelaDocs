<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/vibrator.html -->

# Vibration

## Interface Declaration
```json
{ "name" : "system.vibrator" }
```

## Import Module
```javascript
import vibrator from '@system.vibrator' // or const vibrator = require('@system.vibrator')
```

## Interface Definition

### vibrator.vibrate(OBJECT)

Trigger vibration

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
mode | String | No | Vibration mode, "long" for long vibration, "short" for short vibration. Defaults to long  
  
#### Example:
```javascript
vibrator.vibrate({ mode : 'long' })
```

### vibrator.start(OBJECT)

Start vibration

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
duration | Number | Yes | Vibration duration (in ms), must be a positive integer  
interval | Number | Yes | Vibration interval (in ms), must be a positive integer  
count | Number | Yes | Number of vibrations, must be a positive integer  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### success Return Value:

Parameter Name | Type | Description  
---|:---:|---  
id | Number | Unique ID identifying the vibration task  
  
#### fail Return Value:

Error Code | Description  
---|---  
205 | Task already exists  
202 | Parameter error  
  
#### Example:
```javascript
vibrator.start({ duration : 1000 , interval : 1000 , count : 10 , success : function(data){ console.log(` handling success, id = ${ data.id } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } , errorMsg= ${ data } `)} , complete : function() { console.log(` handling complete `)} })
```

### vibrator.stop(Number)

Stop vibration

#### Parameters:

Type | Required | Description  
---|:---:|---  
Number | Yes | Vibration task ID  
  
#### Return Value:

Type | Description  
---|---  
Boolean | true: Success; false: Failure  
  
#### Example:
```javascript
vibrator.stop(1)
```

### vibrator.getSystemDefaultMode()

Get system default vibration mode

#### Parameters:

None

#### Return Value:

Type | Description  
---|---  
Number | 0: Vibration off; 1: Standard vibration; 2: Enhanced vibration  
  
#### Example:
```javascript
vibrator.getSystemDefaultMode()
```

## Support Details

Interface | Supported Device Products | Unsupported Device Products  
---|:---:|---  
vibrate | Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1, Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4, REDMI Watch 5 | -  
start |:---:| Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4, REDMI Watch 5, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1  
stop |:---:| Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4, REDMI Watch 5, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1  
getSystemDefaultMode |:---:| Xiaomi Watch S3, Xiaomi Band 9 Pro, Xiaomi Watch S4, REDMI Watch 5, Xiaomi S1 Pro Sports Health Watch, Xiaomi Band 8 Pro, Xiaomi Band 9, Redmi Watch 4, Xiaomi Watch H1
