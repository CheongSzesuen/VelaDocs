<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/grammar.html -->

# General Syntax

The framework provides various interfaces to obtain basic application information or invoke system capabilities. Each interface includes several APIs to perform specific tasks. Before using an interface, you need to declare the interface and import the module. Then, you can call the several APIs defined under that interface.

## Interface Declaration

Declare the interface under the `features` field in the `manifest.json` file, for example:
```javascript
[ { "name" : "system.network" } ]
```

## Importing Modules

Before using an interface, you need to import the interface module in your code, for example:
```javascript
import network from '@system.network' // or const network = require('@system.network')
```

## Interface API Invocation

The APIs provided by the interface can be invoked in the following ways:

  * Synchronous APIs
  * Asynchronous APIs
  * Subscription-based APIs

### Synchronous API Invocation

If an API does not return a value, it is generally defined as a synchronous API. You can call it directly, for example:
```javascript
audio.play()
```

### Asynchronous API Invocation

If an API returns a value, it is generally defined as an asynchronous API. In addition to regular parameters, these APIs have three common parameters: "success", "fail", and "complete", which are callback methods triggered after the API execution is "successful", "failed", or "completed". When calling, you can pass these three parameters to obtain the return value of a successful API execution or handle the execution after a failure or completion. The descriptions of these three common parameters are as follows:

Name | Method Parameter | Parameter Type | Parameter Value | Description  
---|:---:|---|:---:|---  
success | data | any | The return value of the API execution. For details, see the interface usage documentation. | Triggered after the API execution is successful.  
fail | data | any | The error information content of the API execution, usually a string, but may also be of other types. For details, see the interface usage documentation. | Triggered after the API execution fails.  
| code | number | The error code of the API execution. For details, see General Error Codes. |   
complete |:---:| - |:---:| Triggered after the API execution is completed.  
  
Code example:
```javascript
storage.get({ key : 'A1' , success : function(data){ console.log('handling success')} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

### Subscription/Unsubscription APIs

Subscription-based APIs do not return results immediately. These APIs require developers to pass a callback function as a parameter. This callback function is triggered when the API is completed or when an event changes, and it can be executed multiple times. The parameter descriptions of this general callback function are as follows:

Name | Method Parameter | Parameter Type | Parameter Value | Description  
---|:---:|---|:---:|---  
success | data | any | The return value of the API execution. For details, see the interface usage documentation. | Triggered when the API call is successful or when an event changes. It may be triggered multiple times.  
fail | data | any | The error information content, usually a string, but may also be of other types. For details, see the interface usage documentation. | Triggered when the API execution fails. Once this callback function is triggered, `success` will not be called again, and the interface call ends.  
| code | number | The error code of the API execution. For details, see General Error Codes. |   
  
Code example:
```javascript
geolocation.subscribe({ success : function(data){ console.log(` handling success: longitude = ${ data.longitude } , latitude = ${ data.latitude } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} })
```

## General Error Codes

When errors occur during the execution of APIs in all interfaces, they will return uniformly defined general error codes or special error codes defined by the APIs themselves. The descriptions of the general error codes are as follows:

Code | Definition  
---|---  
200 | General system error, thrown when all unknown system exceptions occur. For example, the framework fails to apply for memory space.  
202 | Parameter error, occurs when the parameters are not passed correctly according to the API definition during the call.  
203 | The function is not supported.  
204 | Request timeout.  
300 | I/O error.
