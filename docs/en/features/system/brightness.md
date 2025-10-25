<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/brightness.html -->

# Screen Brightness

## Interface Declaration
```json
{ "name" : "system.brightness" }
```

## Import Module
```javascript
import brightness from '@system.brightness' // or const brightness = require('@system.brightness')
```

## Interface Definition

### brightness.getValue(OBJECT)

Gets the current screen brightness value.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Success Return Value:

Parameter | Type | Description  
---|:---:|---  
value | Integer | Screen brightness (range: 0-255)  
  
#### Example:
```javascript
brightness.getValue({ success : function(data){ console.log(` handling success, value = ${ data.value } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setValue(OBJECT)

Sets the current screen brightness value.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
value | Integer | Yes | Screen brightness (range: 0-255)  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Example:
```javascript
brightness.setValue({ value : 100 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.getMode(OBJECT)

Gets the current screen brightness mode.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Success Return Value:

Parameter | Type | Description  
---|:---:|---  
mode | Integer | 0: manual brightness adjustment, 1: auto brightness adjustment  
  
#### Example:
```javascript
brightness.getMode({ success : function(data){ console.log(` handling success, mode = ${ data.mode } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setMode(OBJECT)

Sets the current screen brightness mode.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
mode | Integer | Yes | 0: manual brightness adjustment, 1: auto brightness adjustment  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Example:
```javascript
brightness.setMode({ mode : 1 , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### brightness.setKeepScreenOn(OBJECT)

Sets whether to keep the screen on.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
keepScreenOn | Boolean | Yes | Whether to keep the screen on  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Example:
```javascript
brightness.setKeepScreenOn({ keepScreenOn : true , success : function() { console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
