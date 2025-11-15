<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/grammar.html -->

# General Syntax

The framework provides various interfaces to obtain basic application information or invoke system capabilities. Each interface includes several APIs to perform specific tasks. Before using an interface, you need to declare the interface and import the module. Only then can you call the several APIs defined under that interface.

## Interface Declaration

The declaration is made under the features field in the manifest.json file, for example:
```javascript
[ { "name" : "system.network" } ]
```

## Importing Modules

Before using an interface, you need to import the interface module in your code, for example:
```javascript
import network from '@system.network' // or const network = require('@system.network')
```

## Interface API Calls

The APIs provided by interfaces can be called in the following ways:

  * Synchronous APIs
  * Asynchronous APIs
  * Subscription-based APIs

### Synchronous API Calls

If an API does not return a value, it is generally defined as a synchronous API and can be called directly, for example:
```javascript
audio.play()
```

### Asynchronous API Calls

If an API returns a value, it is generally defined as an asynchronous API. In addition to regular parameters, such APIs have three universal parameters: "success", "fail", and "complete". These are callback methods triggered after the API execution is "successful", "failed", or "completed". When calling, you can pass these three parameters to obtain the return value upon successful API execution or to handle execution failure or completion. The descriptions of these three universal parameters are as follows:

Name | Method Parameter | Parameter Type | Parameter Value | Description  
---|:---:|---|:---:|---  
success | data | any | The return value of the API execution. For details, see the interface usage documentation. | Triggered upon successful API execution.  
fail | data | any | The error information content of the API execution, generally a string, but may also be of other types. For details, see the interface usage documentation. | Triggered upon failed API execution.  
| code | number | The error code of the API execution. For details, see Universal Error Codes. |   
complete |:---:| - |:---:| Triggered upon completion of the API execution.  
  
Code example:
```javascript
storage.get({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### Subscription/Unsubscription APIs

Subscription-based APIs do not return results immediately. Such APIs require developers to pass a callback function as a parameter. This callback function will be triggered when the API is completed or when an event changes, and can be executed multiple times. The descriptions of the parameters of this universal callback function are as follows:

Name | Method Parameter | Parameter Type | Parameter Value | Description  
---|:---:|---|:---:|---  
success | data | any | The return value of the API execution. For details, see the interface usage documentation. | Triggered when the API call is successful or when an event changes. May be triggered multiple times.  
fail | data | any | The error information content, generally a string, but may also be of other types. For details, see the interface usage documentation. | Triggered upon failed API execution. Once this callback function is triggered, success will not be called again, and the interface call ends.  
| code | number | The error code of the API execution. For details, see Universal Error Codes. |   
  
Code example:
```javascript
geolocation.subscribe({ success : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## Universal Error Codes

When errors occur during the execution of APIs from all interfaces, they will return universally defined error codes or special error codes defined by the APIs themselves. The descriptions of the universal error codes are as follows:

code | Definition  
---|---  
200 | System general error, thrown when all unknown system exceptions occur. For example, when the framework fails to apply for memory space.  
201 | User rejection  
202 | Parameter error, when the call does not pass parameters correctly according to the API definition.  
203 | This feature is not supported.  
204 | Request timeout  
205 | Duplicate submission  
207 | User rejection and choosing not to ask again  
300 | I/O error
