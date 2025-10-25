<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/security/crypto.html -->

# Crypto Algorithm

## Interface Declaration
```json
{ "name" : "system.crypto" }
```

## Import Module
```javascript
import crypto from '@system.crypto' // or const crypto = require('@system.crypto')
```

## Interface Definition

### crypto.hashDigest(OBJECT)

Creates a hash digest of the data.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String/Uint8Array | No | Content to be computed. Either this or uri must be provided.  
uri | String | No | File address to be computed. Either this or data must be provided.  
algo | String | No | Algorithm. Default: SHA256   
Options: MD5, SHA1, SHA256, SHA512  
  
#### Return Value:

Type | Description  
---|---  
String | The computed digest content.  
  
#### Example:
```javascript
const digest = crypto.hashDigest({ data : 'hello' , algo : 'MD5' })
```

### crypto.hmacDigest(OBJECT)

Creates a cryptographic HMAC digest.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String | Yes | Data to be computed.  
algo | String | No | Algorithm. Default: SHA256   
Options: MD5, SHA1, SHA256, SHA512  
key | String | Yes | Key.  
success | Function | No | Success callback.  
fail | Function | No | Failure callback.  
complete | Function | No | Completion callback.  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Digest.  
  
#### Example:
```javascript
crypto.hmacDigest({ data : 'hello' , algo : 'SHA256' , key : 'a secret' , success : function(res){ console.log(` ### crypto.hmacDigest success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.hmacDigest fail ### ${ code } : ${ data } `)} })
```

### crypto.sign(OBJECT)

Used to generate a signature.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String/Uint8Array | No | Text to be signed. Either this or uri must be provided.  
uri | String | No | File address to be signed. Either this or data must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   
Options: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512  
privateKey | String | Yes | Private key.  
success | Function | No | Success callback.  
fail | Function | No | Failure callback.  
complete | Function | No | Completion callback.  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String/Uint8Array | If input is a string, returns a base64-encoded string; otherwise returns Uint8Array; if only uri is provided, defaults to returning string.  
  
#### Example:
```javascript
crypto.sign({ data : 'hello' , algo : 'RSA-SHA256' , privateKey : 'a secret' , success : function(res){ console.log(` ### crypto.sign success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.sign fail ### ${ code } : ${ data } `)} })
```

### crypto.verify(OBJECT)

Used to verify a signature.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String/Uint8Array | No | Text to be verified. Either this or uri must be provided.  
uri | String | No | File address to be verified. Either this or data must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   
Options: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512  
signature | String/Uint8Array | Yes | Signature.  
publicKey | String | Yes | Public key.  
success | Function | No | Success callback.  
fail | Function | No | Failure callback.  
complete | Function | No | Completion callback.  
  
#### success Return Value Boolean:

Type | Description  
---|---  
Boolean | Verification result. True if passed, false if not.  
  
#### Example:
```javascript
crypto.verify({ data : 'hello' , algo : 'RSA-SHA256' , publicKey : 'public key' , signature : 'signature' , success : function(data){ console.log(` ### crypto.verify success: ` , data)} , fail : function(data , code){ console.log(` ### crypto.verify fail ### ${ code } : ${ data } `)} })
```

### crypto.encrypt(OBJECT)

Encrypts data.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String/Uint8Array | Yes | Data to be encrypted.  
algo | String | No | Encryption algorithm. Default: RSA   
Options: RSA, AES  
key | String | Yes | Key used for encryption, as a base64-encoded string.  
options | Object | No | Encryption parameters.  
success | Function | No | Success callback.  
fail | Function | No | Failure callback.  
complete | Function | No | Completion callback.  
  
#### RSA Parameters options:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for RSA algorithm. Default: "RSA/None/PKCS1Padding"  
  
#### AES Parameters options:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for AES algorithm. Default: "AES/CBC/PKCS7Padding"  
iv | String | No | Initialization vector for AES encryption/decryption, as a base64-encoded string. Default: key value.  
ivOffset | Number | No | Offset for the initialization vector in AES. Default: 0.  
ivLen | Number | No | Byte length of the initialization vector in AES. Default: 16.  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String/Uint8Array | If input is a string, returns a base64-encoded string; otherwise returns Uint8Array.  
  
#### Example:
```javascript
crypto.encrypt({ // Text content to be encrypted data : 'hello' , // Encryption public key encoded in base64 key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , success : function(res){ console.log(` ### crypto.encrypt success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.encrypt fail ### ${ code } : ${ data } `)} })
```

### crypto.decrypt(OBJECT)

Decrypts data.

#### Parameters:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
data | String/Uint8Array | Yes | Data to be decrypted.  
algo | String | No | Decryption algorithm. Default: RSA   
Options: RSA, AES  
key | String | Yes | Key used for decryption, as a base64-encoded string.  
options | Object | No | Decryption parameters.  
success | Function | No | Success callback.  
fail | Function | No | Failure callback.  
complete | Function | No | Completion callback.  
  
#### RSA Parameters options:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for RSA algorithm. Default: "RSA/None/PKCS1Padding"  
  
#### AES Parameters options:

Parameter Name | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for AES algorithm. Default: "AES/CBC/PKCS7Padding"  
iv | String | No | Initialization vector for AES encryption/decryption, as a base64-encoded string. Default: key value.  
ivOffset | Number | No | Offset for the initialization vector in AES. Default: 0.  
ivLen | Number | No | Byte length of the initialization vector in AES. Default: 16.  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String/Uint8Array | If input is a string, returns a base64-encoded string; otherwise returns Uint8Array.  
  
#### Example:
```javascript
crypto.decrypt({ // Content to be decrypted data : 'WB96uM08PfYIHu5G1p6YwA==' , // Encryption public key encoded in base64 key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , success : function(res){ console.log(` ### crypto.decrypt success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.decrypt fail ### ${ code } : ${ data } `)} })
```

### crypto.btoa(STRING)

Creates a base-64 encoded ASCII string from a String object, where each character in the string is treated as a binary data byte.

#### Parameters:

Type | Required | Description  
---|:---:|---  
String | Yes | Text to be encoded.  
  
#### Return Value String:

Type | Description  
---|---  
String | The encoded result.  
  
#### Example:
```javascript
const encodeData = crypto.btoa('hello')
```

### crypto.atob(STRING)

Decodes a base-64 encoded string.

#### Parameters:

Type | Required | Description  
---|:---:|---  
String | Yes | Text to be decoded.  
  
#### Return Value String:

Type | Description  
---|---  
String | The decoded result.  
  
#### Example:
```javascript
const encodeString = crypto.btoa('hello')const res = crypto.atob(encodeString)
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported
