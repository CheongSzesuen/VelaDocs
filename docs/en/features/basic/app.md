<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/basic/app.html -->
<!-- 最近更新日期: 2026-05-26 -->

# Application Context app

## Interface Declaration

No declaration required.

## Import Module

```javascript
import app from '@system.app' 
// or 
const app = require('@system.app')
```

## Interface Definition

### app.getInfo()

Obtain current application information.

#### Parameters:

None

#### Return Value:

Parameter Name | Type | Description
---|---|---
packageName | String | Application package name
icon | String | Application icon path
name | String | Application name
versionName | String | Application version name
versionCode | Integer | Application version number
logLevel | String | Log level
source | Object | Application source 

#### source

Parameter Name | Type | Description
---|---|---
packageName | String | Package name of the source app, primary source
type | String | Source type, secondary source. Values can be shortcut, push, url, barcode, nfc, bluetooth, other. 

#### Example:

```javascript
console.log(JSON.stringify(app.getInfo()))
```

```json
// Console output
{
  // Application package name
  "packageName": "com.example.demo",
  // Application name
  "name": "demo",
  // Application version name
  "versionName": "1.0.0",
  // Application version number
  "versionCode": 1,
  // Application image
  "icon": "/common/logo.png",
  // Log level
  "logLevel": "debug",
  // Application source
  "source": {
    // Package name of the source app
    "packageName": "",
    // Source type
    "type": "shortcut"
  }
}
```

### app.terminate()

Exit the current application.

#### Parameters:

None

#### Return Value:

None

#### Example:

```javascript
app.terminate()
```

### app.loadLibrary(name)

Load a dynamic library, requires collaboration with the manufacturer.

#### Parameters:

Parameter Name | Type | Required | Description
---|---|---|---
name | String | Yes | Name of the lib library 

#### Return Value:

Result of dynamic library loading.

#### Example:

```javascript
import app from '@system.app'
const testApp = app.loadLibrary('test_app')

testApp.on('js_task_callback', () => {
  // Callback action
})
```

### app.canIUse()3+

#### Parameters:

Type | Description
---|---
String | The capability to query, format specified below 

#### Return Value:

Type | Description
---|---
Boolean | Whether the queried capability is supported 

### Input Parameter Format

#### Query Interface

```javascript
// Query whether a method under a feature is supported
'@${featureName}.${method}'
// Query whether a feature is supported
'@${featureName}'
```

**Example**

```javascript
import app from '@system.app';

if (app.canIUse('@system.router.push')) {
  // The method @system.router.push can be used
}
if (app.canIUse('@system.router')) {
  // The @system.router interface can be used
}
```

#### Query Component

The value of `type` can be `'attr'`, `'style'`, or `'method'`, corresponding to the component's attributes, styles, and methods, respectively.

```javascript
// Query whether attributes, styles, or methods under a component are supported
`${componentName}.${type}.${name}`
// Query whether a component is supported
`${componentName}`
```

**Example**

```javascript
import app from '@system.app';

if (app.canIUse('scroll')) {
  // The scroll component can be used
}
if (app.canIUse('scroll.attr.scroll-x')) {
  // The scroll-x attribute of the scroll component can be used
}
```
