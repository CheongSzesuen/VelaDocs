<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/network/interconnect.html -->

# Device Communication Interconnect

Used for communication with the paired mobile app and for sending and receiving data from the mobile app. The communication connection will be automatically established. There is no need to manage the creation and destruction of connections within the app, but callback functions can be registered to receive notifications about connection status changes for appropriate handling, such as notifying the user.

## Interface Declaration
```json
{ "name" : "system.interconnect" }
```

## Import Module
```javascript
import interconnect from '@system.interconnect' // or const interconnect = require('@system.interconnect')
```

## Interface Definition

### interconnect.instance()

Obtains a connection object that exists as a singleton in the app. Subsequent data sending and receiving are based on this connection object.

#### Parameters:

None

#### Return Value:

An interconnect connection instance, the connect object.

#### Example:
```javascript
const connect = interconnect.instance()
```

### connect.getReadyState(OBJECT)

Obtains the connection status of the app.

#### OBJECT Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
  
#### success Return Value:

Property Value | Type | Description  
---|:---:|---  
status | Number | 1: Connected successfully, 2: Connection disconnected  
  
#### fail Return Value:

Parameter Value | Type | Description  
---|:---:|---  
data | String | Error message  
code | Number | Error code  
  
#### Error Code Descriptions:

[Supports common error codes](</vela/quickapp/en/features/grammar.html#common-error-codes>)

Error Code | Description  
---|---  
1006 | Connection disconnected  
  
#### Example:
```javascript
connect.getReadyState({ success :(data)=> { if(data.status === 1){ console.log('Connected successfully')} else if(data.status === 2){ console.log('Connection failed')} } , fail :(data , code)=> { console.log(` handling fail, code = ${ code } `)} })
```

### connect.diagnosis(OBJECT)

Diagnoses the connection between the watch app and the counterpart app. Returns "ok" if the connection is successful, or the reason for failure if the connection fails. If a connection is in progress when called, it waits for the connection to end before returning the final status.

#### Object Parameters:

Property | Type | Required | Description  
---|:---:|---|---  
timeout | Number | No | Timeout duration for waiting for diagnosis, in milliseconds   
Default value: 10000ms  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
  
#### success Return Value:

Property Value | Type | Description  
---|:---:|---  
status | Number | 0: OK, connection successful  
204: CONNECT_TIMEOUT, connection timeout  
1001: APP_UNINSTALLED, counterpart app not installed  
1000: OTHERS, other connection errors  
  
#### fail Return Value:

Parameter Value | Type | Description  
---|:---:|---  
data | String | Error message  
code | Number | Error code  
  
#### Error Code Descriptions:

[Supports common error codes](</vela/quickapp/en/features/grammar.html#common-error-codes>)

#### Example:
```javascript
connect.diagnosis({ success : function(data){ console.log(` handling success, version = ${ data.status } `)} , fail : function(data , code){ console.log(` handling fail, code = ${ code } `)} , })
```

### connect.send(OBJECT)

Sends data to the mobile app.

#### Object Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | Object | Yes | Data to be sent  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
  
#### success Return Value:

None

#### fail Return Value:

Parameter Value | Type | Description  
---|:---:|---  
data | String | Error message  
code | Number | Error code  
  
#### Error Code Descriptions:

[Supports common error codes](</vela/quickapp/en/features/grammar.html#common-error-codes>)

Error Code | Description  
---|---  
204 | Connection timeout  
1006 | Connection disconnected  
  
#### Example:
```javascript
connect.send({ data : { str : 'test' , num : 123 } , success :() => { console.log(` handling success `)} , fail :(data , code)=> { console.log(` handling fail, errMsg = ${ data.data } , errCode = ${ data.code } `)} })
```

## Events

### connect.onmessage

Receives data from the mobile app.

#### Callback Parameters:

Parameter | Type | Description  
---|:---:|---  
data | String | Received data  
  
#### Example:
```javascript
connect.onmessage =(data)=> { console.log(` received message: ${ data.data } `)}
```

### connect.onopen

Callback function when the connection is opened.

#### Callback Parameters:

Parameter | Type | Description  
---|:---:|---  
isReconnected | Boolean | Whether it is a reconnection  
  
#### Example:
```javascript
connect.onopen = function(data){ console.log('connection opened isReconnected: ' , data.isReconnected)}
```

### connect.onclose

Callback function when the connection is closed.

#### Callback Parameters:

Parameter | Type | Description  
---|:---:|---  
code | Number | Connection closure status code  
data | String | Data returned upon connection closure  
  
#### Example:
```javascript
connect.onclose =(data)=> { console.log(` connection closed, reason = ${ data.data } , code = ${ data.code } `)}
```

### connect.onerror

Callback function when a connection error occurs.

#### Callback Parameters:

Parameter | Type | Description  
---|:---:|---  
code | Number | Error code, see error code descriptions  
data | String | Error message  
  
#### Error Code Descriptions:

[Supports common error codes](</vela/quickapp/en/features/grammar.html#common-error-codes>)

Error Code | Description  
---|---  
1000 | Unknown error  
1001 | Mobile app not installed  
1006 | Connection disconnected  
  
#### Example:
```javascript
connect.onerror =(data)=> { console.log(` connection error, errMsg = ${ data.data } , errCode = ${ data.code } `)}
```

## Development Considerations

For interconnect communication, ensure that the package names and signatures of both the Quick App and the Android version of the third-party app are consistent.

  * Ensure that the package field in the Quick App's manifest.json matches the package name of the third-party Android app to be integrated.
  * The Quick App signature must use the signature of the third-party Android app. The certificate and private key can be extracted from the .jks file as follows:

  1. Convert the jks to p12 by executing the following command. After entering the corresponding password, a p12 format file will be generated in the same directory.
```shell
keytool -importkeystore -srckeystore keystore.jks -destkeystore keystore.p12 -srcstoretype jks -deststoretype pkcs12
```

  2. Convert the p12 to pem by executing the following command. After entering the password set for the p12 file in the previous step, a pem format file will be generated in the same directory.
```shell
openssl pkcs12 -nodes -in keystore.p12 -out keystore.pem
```

  3. Copy the private key and certificate from the pem format file:  
Copy the content from -----BEGIN PRIVATE KEY----- to -----END PRIVATE KEY----- into private.pem.  
Copy the content from -----BEGIN CERTIFICATE----- to -----END CERTIFICATE----- into certificate.pem.

  * If OpenSSL is not installed locally or a simpler operation process is desired, we provide an [online signature generation tool (opens new window)](<https://cdn.hybrid.xiaomi.com/aiot-ide/signature-generate-tool/v2/index.html>). This tool is a web application written in WebAssembly that can directly generate pem format private keys and certificates in the browser environment without uploading signature files and passwords to a remote server, fully ensuring user privacy and security. The steps for using the online signature generation tool are as follows:

    1. Upload the p12 file and enter the corresponding password;

    2. Click the "Generate Signature" button and wait for the signature generation success popup to appear;

    3. Click the "Download Signature" button to download the pem format private key and certificate;

  * The Quick App needs to place the generated private key private.pem and certificate certificate.pem in the root directory of the Quick App under /sign/debug and /sign/release for packaging and testing.

  * When testing on a real device, it is recommended to first enter the package name to uninstall the old package and then install the new package. Observing the desktop icon for uninstallation will ensure that the app icon is deleted, guaranteeing a complete replacement.

Reference Appendix

  1. Xiaomi Wear Third-Party App Capability Open Interface Documentation: [Click to Download (opens new window)](<https://vela-docs.cnbj1.mi-fds.com/vela-docs/files/%E5%B0%8F%E7%B1%B3%E7%A9%BF%E6%88%B4%E7%AC%AC%E4%B8%89%E6%96%B9APP%E8%83%BD%E5%8A%9B%E5%BC%80%E6%94%BE%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3_1.4.pdf> "Download")
  2. Interconnect Development and Testing Demo: [Click to Download (opens new window)](<https://cdn.cnbj3-fusion.fds.api.mi-img.com/quickapp-vela/interconnect_dev_test_demo.zip> "Download")

