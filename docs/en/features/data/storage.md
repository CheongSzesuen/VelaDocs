<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/data/storage.html -->

# Data Storage

## Interface Declaration
```json
{ "name" : "system.storage" }
```

## Import Module
```javascript
import storage from '@system.storage' // or const storage = require('@system.storage')
```

## Methods

### storage.get(OBJECT)

Reads stored content.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
key | String | Yes | Index  
default | String | No | If the key does not exist, returns default. If default is not specified, returns an empty string with a length of 0  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### success Return Value:

Stored content corresponding to the key

#### Example:
```javascript
storage.get({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.set(OBJECT)

Modifies stored content.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
key | String | Yes | Index  
value | String | No | New value. If the new value is an empty string with a length of 0, deletes the data item indexed by key  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### Example:
```javascript
storage.set({ key : 'A1' , value : 'V1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.clear(OBJECT)

Clears stored content.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### Example:
```javascript
storage.clear({ success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### storage.delete(OBJECT)

Deletes stored content.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
key | String | Yes | Index  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### Example:
```javascript
storage.delete({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
