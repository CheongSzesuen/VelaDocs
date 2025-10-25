<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/system/zip.html -->

# Unzip

## Interface Declaration
```json
{ "name" : "system.zip" }
```

## Import Module
```javascript
import zip from '@system.zip' // or const zip = require('@system.zip')
```

## Interface Definition

### zip.decompress(OBJECT)

Unzip file

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
srcUri | String | Yes | URI of the source file, cannot be a tmp type URI  
dstUri | String | Yes | URI of the target directory, cannot be an application resource path or a tmp type URI  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Callback after execution ends  
  
#### success Return Value:

None

#### fail Return Value:

Error Code | Description  
---|---  
202 | Parameter error  
300 | I/O error  
  
#### Example:
```javascript
zip.decompress({ srcUri : 'internal://cache/test.zip' , dstUri : 'internal://files/unzip/' , success : function() { console.log(` handling success `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```
