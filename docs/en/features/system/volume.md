<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/volume.html -->

# System Volume

## Interface Declaration
```json
{ "name" : "system.volume" }
```

## Import Module
```javascript
import volume from '@system.volume' // or const volume = require('@system.volume')
```

## Interface Definition

### volume.getMediaValue (OBJECT)

Gets the current media volume.

#### Parameters

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### success Return Value:

Parameter | Type | Description  
---|:---:|---  
value | Number | Current system media volume, between 0.0 and 1.0  
  
#### Example
```javascript
volume.getMediaValue({ success : function(data){ console.log(` handling success: ${ data.value } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### volume.setMediaValue (OBJECT)

Sets the current media volume.

#### Parameters

Parameter | Type | Required | Description  
---|:---:|---|---  
value | Number | Yes | Volume to set, between 0.0 and 1.0  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### fail Return Value:

[Supports common error codes](</vela/quickapp/en/features/grammar.html#common-error-codes>)

#### Example
```javascript
volume.setMediaValue({ value : 0.5 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## Events

### volume.onMediaValueChanged

Triggered when the media volume changes.

#### Callback Object Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
value | Number | Yes | Current system media volume, range: between 0.0 and 1.0  
  
#### Example
```javascript
volume.onMediaValueChanged = function(res){ console.log('volume media value changed:' , res.value)}
```
