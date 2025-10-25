<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/other/prompt.html -->

# Popup

## Interface declaration
```json
{ "name" : "system.prompt" }
```

## Import module
```javascript
import prompt from '@system.prompt' // or const prompt = require('@system.prompt')
```

## Interface definition

### prompt.showToast(OBJECT)

Displays Toast prompt information

#### Parameters

Parameter name | Type | Required | Description  
---|:---:|---|---  
message | String | Yes | The text information to be displayed  
duration | Number | No | The display duration in milliseconds. The default value is 1500. The recommended range is 1500-10000.  
  
#### Example:
```javascript
prompt.showToast({ message : 'Message Info' , duration : 2000 })
```
