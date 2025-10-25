<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/basic/configuration.html -->

# Application Configuration

## Interface Declaration

No declaration required

## Import Module
```javascript
import configuration from '@system.configuration' // or const configuration = require('@system.configuration')
```

## Interface Definition

### configuration.getLocale()

Retrieves the current locale of the application. By default, it uses the system's locale, which may change due to settings or system locale changes.

#### Parameters:

None

#### Return Value:

Parameter Name | Type | Description  
---|:---:|---  
language | String | Language  
countryOrRegion | String | Country or region  
  
#### Example:
```javascript
const locale = configuration.getLocale() console.log(locale.language)
```
