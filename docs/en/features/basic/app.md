<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/basic/app.html -->

# Application Context

## Interface Declaration

No declaration is required.

## Import Module
```javascript
import app from '@system.app' // or const app = require('@system.app')
```

## Interface Definition

### app.getInfo()

Get current application information.

#### Parameters:

None.

#### Return Value:

Parameter Name | Type | Description  
---|:---:|---  
packageName | String | Application package name  
icon | String | Application icon path  
name | String | Application name  
versionName | String | Application version name  
versionCode | Integer | Application version number  
logLevel | String | Log level  
source | Object | Application source  
  
#### source

Parameter Name | Type | Description  
---|:---:|---  
packageName | String | Package name of the source app, primary source  
type | String | Source type, secondary source, values include shortcut, push, url, barcode, nfc, bluetooth, other  
  
#### Example:
```javascript
console.log(JSON.stringify(app.getInfo()))
```

```json
// console output { // Application package name "packageName" : "com.example.demo" , // Application name "name" : "demo" , // Application version name "versionName" : "1.0.0" , // Application version number "versionCode" : 1 , // Application icon "icon" : "/common/logo.png" , // Log level "logLevel" : "debug" , // Application source "source" : { // Package name of the source app "packageName" : "" , // Source type "type" : "shortcut" } }
```

### app.terminate()

Exit the current application.

#### Parameters:

None.

#### Return Value:

None.

#### Example:
```javascript
app.terminate()
```

### app.canIUse()3+

#### Parameters:

Type | Description  
---|---  
String | The capability to query, format as below  
  
#### Return Value:

Type | Description  
---|---  
Boolean | Whether the queried capability is supported  
  
### Input Parameter Format

#### Query Interface
```javascript
// Query if a method under a feature is supported '@${featureName}.${method}' // Query if a feature is supported '@${featureName}'
```

**Example**
```javascript
import app from '@system.app' ; if(app.canIUse('@system.router.push')) { // Can use method @system.router.push } if(app.canIUse('@system.router')) { // Can use @system.router interface }
```

#### Query Component

The value of type can be `'attr'`, `'style'`, `'method'`, corresponding to component's attributes, styles, and methods respectively.
```javascript
// Query if an attribute, style, or method under a component is supported ` ${ componentName } . ${ type } . ${ name } ` // Query if a component is supported ` ${ componentName } `
```

**Example**
```javascript
import app from '@system.app' ; if(app.canIUse('scroll')) { // Can use scroll component } if(app.canIUse('scroll.attr.scroll-x')) { // Can use scroll-x attribute of scroll component }
```
