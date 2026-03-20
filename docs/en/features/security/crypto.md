<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/security/crypto.html -->

# Cryptographic Algorithm crypto

## Interface Declaration

```json
{ "name": "system.crypto" }
```

## Module Import

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

## Interface Definition

### crypto.hashDigest(OBJECT)

Create a hash digest of data.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Content to be computed. Either data or uri must be provided.  
uri | String | No | Address of the file to be computed. Either data or uri must be provided.  
algo | String | No | Algorithm. Default: SHA256   <br>Optional: MD5, SHA1, SHA256, SHA512
  
#### Return Value:

Type | Description  
---|---  
String | Computed digest content  
  
#### Example:

```javascript
const digest = crypto.hashDigest({
  data: 'hello',
  algo: 'MD5'
})
```

### crypto.hmacDigest(OBJECT)

Create a cryptographic HMAC digest.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Yes | Data to be computed  
algo | String | No | Algorithm. Default: SHA256   <br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Digest  
  
#### Example:

```javascript
crypto.hmacDigest({
  data: 'hello',
  algo: 'SHA256',
  key: 'a secret',
  success: function(res) {
    console.log(`### crypto.hmacDigest success:`, res.data)
  },
  fail: function(data, code) {
    console.log(`### crypto.hmacDigest fail ### ${code}: ${data}`)
  }
})
```

### crypto.sign(OBJECT)

Used to generate a signature.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Text to be signed. Either data or uri must be provided.  
uri | String | No | Address of the file to be signed. Either data or uri must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   <br>Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512
privateKey | String | Yes | Private key  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Uint8Array | If input is a string, returns a base64-encoded string; otherwise, returns Uint8Array; if only uri is passed, returns string by default  
  
#### Example:

```javascript
crypto.sign({
  data: 'hello',
  algo: 'RSA-SHA256',
  privateKey: 'a secret',
  success: function(res) {
    console.log(`### crypto.sign success:`, res.data)
  },
  fail: function(data, code) {
    console.log(`### crypto.sign fail ### ${code}: ${data}`)
  }
})
```

### crypto.verify(OBJECT)

Used to verify a signature.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Text to be signed. Either data or uri must be provided.  
uri | String | No | Address of the file to be signed. Either data or uri must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   <br>Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512
signature | String | Uint8Array | Yes | Signature  
publicKey | String | Yes | Public key  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Boolean:

Type | Description  
---|---  
Boolean | Verification result. True if passed, false if not passed  
  
#### Example:

```javascript
crypto.verify({
  data: 'hello',
  algo: 'RSA-SHA256',
  publicKey: 'public key',
  signature: 'signature',
  success: function(data) {
    console.log(`### crypto.verify success:`, data)
  },
  fail: function(data, code) {
    console.log(`### crypto.verify fail ### ${code}: ${data}`)
  }
})
```

### crypto.encrypt(OBJECT)

Encryption.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | Yes | Data to be encrypted   <br>string: plaintext to be encrypted, processed with 'utf-8' encoding by default<br>Uint8Array: other encoding formats such as hexadecimal or base64 need to be converted to this type
algo | String | No | Encryption algorithm. Default: RSA   <br>Optional: RSA, AES
key | String | Uint8Array | Yes | Key used for encryption   <br>AES encryption mode supports 128-bit (Uint8Array 16 bytes) / 192-bit (Uint8Array 24 bytes) / 256-bit (Uint8Array 32 bytes) keys<br>String: string generated after base64 encoding; RSA encryption requires a PEM format string<br>Uint8Array: other encoding formats such as hexadecimal can be converted to this type
options | Object | No | Encryption parameters  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### RSA Parameters options:

Parameter | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for RSA algorithm, supports "RSA/None/PKCS1Padding"  
  
#### AES Parameters options:

Parameter | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for AES algorithm, defaults to "AES/CBC/PKCS7Padding"   <br>See transformation support details
iv | String | No | Initialization vector for AES encryption/decryption, string after base64 encoding   <br>AES CBC/ECB mode:<br>Default value is key<br>Default value extraction method:<br>1\. If key is a string, the string is decoded and the byte content is used as iv<br>2\. If key is a uint8array, the byte content is used as iv<br>AES-CCM mode:<br>No default value
ivOffset | Number | No | Offset of the initialization vector for AES encryption/decryption, integer, default is 0  
ivLen | Number | No | Byte length of the initialization vector for AES encryption/decryption, integer   <br>AES CBC/ECB mode: default is keyLen 16<br>AES-CCM mode: no default value
aad | String | Uint8Array | No | Additional authenticated data for AES-CCM encryption, provides additional authentication information during encryption   <br>String: string after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
tagLen | Number | No | Length of the authentication tag generated by AES-CCM encryption   <br>Must be even, valid range is 4~16<br>Default is 4
  
#### transformation Support Details:

Padding Mode / Encryption Mode | CBC | ECB | CCM  
---|:---:|---|---  
PKCS5Padding | AES/CBC/PKCS5Padding | AES/ECB/PKCS5Padding | -  
PKCS7Padding | AES/CBC/PKCS7Padding | AES/ECB/PKCS7Padding | -  
NoPadding | AES/CBC/NoPadding |:---:| AES/CCM/NoPadding  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Uint8Array | Encrypted data   <br>If input data is a string, returns a base64-encoded string; otherwise, returns Uint8Array
tag | String | Uint8Array | AES-CCM encryption returns an authentication tag   <br>If input data is a string, returns a base64-encoded string; otherwise, returns Uint8Array
  
#### Example:

```javascript
// AES-CBC Encryption
crypto.encrypt({
  // Text content to be encrypted
  data: 'hello',
  // Encryption public key after base64 encoding
  key: crypto.btoa('KEYKEYKEYKEYKEYK'),
  algo: 'AES',
  success: function(res) {
    console.log(`### crypto.encrypt success:`, res.data)
  },
  fail: function(data, code) {
    console.log(`### crypto.encrypt fail ### ${code}: ${data}`)
  }
})
```

```javascript
// AES-CCM Encryption
crypto.encrypt({
  // Text content to be encrypted
  data: 'hello',
  // Encryption public key after base64 encoding
  key: crypto.btoa('KEYKEYKEYKEYKEYK'),
  algo: 'AES',
  options: {
    transformation: 'AES/CCM/NoPadding',
    iv: crypto.btoa('iv_info'),
    aad: crypto.btoa('Associated Data'),
    tagLen: 16
  },
  success: function(res) {
    console.log('### crypto.encrypt success:', res.data, res.tag)
  },
  fail: function(data, code) {
    console.log('### crypto.encrypt fail ### ', code , data)
  }
})
```

### crypto.decrypt(OBJECT)

Decryption.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | Yes | Data to be decrypted   <br>String: data to be decrypted, processed with base64 encoding by default<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
algo | String | No | Decryption algorithm. Default: RSA   <br>Optional: RSA, AES
key | String | Uint8Array | Yes | Key used for encryption   <br>AES encryption mode supports 128-bit (Uint8Array 16 bytes) / 192-bit (Uint8Array 24 bytes) / 256-bit (Uint8Array 32 bytes) keys<br>String: string generated after base64 encoding; RSA encryption requires a PEM format string<br>Uint8Array: other encoding formats such as hexadecimal can be converted to this type
options | Object | No | Decryption parameters  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### RSA Parameters options:

Parameter | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for RSA algorithm, supports "RSA/None/PKCS1Padding"  
  
#### AES Parameters options:

Parameter | Type | Required | Description  
---|:---:|---|---  
transformation | String | No | Encryption mode and padding for AES algorithm, defaults to "AES/CBC/PKCS7Padding"   <br>See transformation support details
iv | String | No | Initialization vector for AES encryption/decryption, string after base64 encoding   <br>AES CBC/ECB mode:<br>Default value is key<br>Default value extraction method:<br>1\. If key is a string, the string is decoded and the byte content is used as iv<br>2\. If key is a uint8arrary, the byte content is used as iv<br>AES-CCM mode:<br>No default value
ivOffset | Number | No | Offset of the initialization vector for AES encryption/decryption, integer, default is 0  
ivLen | Number | No | Byte length of the initialization vector for AES encryption/decryption, integer   <br>AES CBC/ECB mode: default is keyLen 16<br>AES-CCM mode: no default value
aad | String | Uint8Array | No | Additional authenticated data for AES-CCM encryption, provides additional authentication information during encryption   <br>String: string after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
tag | String | Uint8Array | No | Authentication tag for AES-CCM, used to verify data integrity and authenticity   <br>String: string after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
  
#### transformation Support Details:

Padding Mode / Encryption Mode | CBC | ECB | CCM  
---|:---:|---|---  
PKCS5Padding | AES/CBC/PKCS5Padding | AES/ECB/PKCS5Padding | -  
PKCS7Padding | AES/CBC/PKCS7Padding | AES/ECB/PKCS7Padding | -  
NoPadding | AES/CBC/NoPadding |:---:| AES/CCM/NoPadding  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Uint8Array | Decrypted data   <br>If input data is a string, returns plaintext after decryption. If the decrypted content cannot be converted to a utf-8 string, an error will occur (CODE: 200); otherwise, returns Uint8Array
  
#### Example:

```javascript
// AES-CBC Decryption
crypto.decrypt({
  // Content to be decrypted
  data: 'WB96uM08PfYIHu5G1p6YwA==',
  // Encryption public key after base64 encoding
  key: crypto.btoa('KEYKEYKEYKEYKEYK'),
  algo: 'AES',
  success: function(res) {
    console.log(`### crypto.decrypt success:`, res.data)
  },
  fail: function(data, code) {
    console.log(`### crypto.decrypt fail ### ${code}: ${data}`)
  }
})
```

```javascript
// AES-CCM Decryption
crypto.decrypt({
  // Text content to be decrypted
  data: '9KFkqz8=',
  // Encryption public key after base64 encoding
  key: crypto.btoa('KEYKEYKEYKEYKEYK'),
  algo: 'AES',
  options: {
    transformation: 'AES/CCM/NoPadding',
    iv: crypto.btoa('iv_info'),
    aad: crypto.btoa('Associated Data'),
    tag: 'kHX6EGYOEvKwA0PS79TAUQ=='
  },
  success: function(res) {
    console.log('### crypto.decrypt success:', res.data)
  },
  fail: function(data, code) {
    console.log('### crypto.decrypt fail ### ', code , data)
  }
})
```

### crypto.btoa(STRING)

Creates a base-64 encoded ASCII string from a String object, where each character in the string is treated as a binary data byte.

#### Parameters:

Type | Required | Description  
---|:---:|---  
String | Yes | Text to be encoded  
  
#### Return Value String:

Type | Description  
---|---  
String | Result after encoding  
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### crypto.atob(STRING)

Decodes a base-64 encoded string.

#### Parameters:

Type | Required | Description  
---|:---:|---  
String | Yes | Text to be decoded  
  
#### Return Value String:

Type | Description  
---|---  
String | Result after decoding  
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### crypto.hkdf(OBJECT)

Create a derived key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
algo | String | No | Digest algorithm to be used. Default: SHA256   <br>Optional: SHA256, SHA512
key | String | Uint8Array | Yes | Key material, source key   <br>String: string generated after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
salt | String | Uint8Array | Yes | Salt value   <br>String: string generated after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
info | String | Uint8Array | Yes | Additional information value. Length cannot exceed 1024 bytes   <br>String: string generated after base64 encoding<br>Uint8Array: other encoding formats such as hexadecimal need to be converted to this type
keyLen | Number | Yes | Length of the key to be generated, in bytes   <br>Maximum allowed value is 255 times the number of bytes produced by the selected digest function (e.g., sha256 produces 32-byte hashes, maximum HKDF output is 8160 bytes; sha512 produces 64-byte hashes, maximum HKDF output is 16320 bytes)
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | Uint8Array | Derived key result  
  
#### Example:

Conversion utility functions:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

utf8-String

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

Hexadecimal

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

base64

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### crypto.createECDH(String)

ECDH (Elliptic-curve Diffie-Hellman) is a key exchange protocol based on elliptic curve cryptography, used to securely generate a shared key. Create an Elliptic Curve Diffie-Hellman (ECDH) key exchange object using the curve name.

#### Parameters:

Type | Required | Description  
---|:---:|---  
String | Yes | Name of the elliptic curve   
Optional values: secp256r1  
  
#### Return Value:

Type | Description  
---|---  
<ECDH> | Elliptic Curve Diffie-Hellman (ECDH) key exchange instance object  
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ECDH

Elliptic Curve Diffie-Hellman (ECDH) key exchange object.

### ecdh.generateKeys(Object)

Generate a key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned public key. Default is buffer   <br>Supports base64, hex, buffer
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
publicKey | String | Uint8Array | Public key from the generated key pair, returned in different types based on the set public key encoding format   <br>base64, hex return String, buffer returns Uint8Array
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ecdh.getPrivateKey(encoding)

Get the private key from the generated key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned private key, default is buffer   <br>Supports base64, hex, buffer
  
#### Return Value:

Type | Description  
---|---  
String | Uint8Array | Returns the corresponding type based on the encoding parameter:   
base64, hex encoding return String   
buffer encoding returns Uint8Array  
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ecdh.getPublicKey(encoding)

Get the public key from the generated key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned public key, default is buffer   <br>Supports base64, hex, buffer
  
#### Return Value:

Type | Description  
---|---  
String | Uint8Array | Returns the corresponding type based on the encoding parameter:   
base64, hex encoding return String   
buffer encoding returns Uint8Array  
  
#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ecdh.setPrivateKey(Object)

Set the private key, will attempt to generate the associated public key with the set private key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
privateKey | String | Uint8Array | Yes | Private key value to be set:   <br>String type: must be a PEM format string<br>Uint8Array type: byte array converted from other formats (such as hexadecimal)
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Example:

```javascript
const digest = crypto.hashDigest({
  data: 'hello',
  algo: 'MD5'
})
```

### ecdh.computeSecret(Object)

Compute the shared secret using the provided public key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
otherPublicKey | String | Uint8Array | Yes | Other party's public key used to compute the shared secret  
inputEncoding | String | No | Encoding format of the provided public key, default is buffer   <br>Supports base64, hex, buffer
outputEncoding | String | No | Encoding format of the returned computed shared secret, default is buffer   <br>Supports base64, hex, buffer
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Callback Return Value Object:

Parameter | Type | Description  
---|:---:|---  
shareKey | String | Uint8Array | Generated computed shared secret  
  
#### Example:

```javascript
const digest = crypto.hashDigest({
  data: 'hello',
  algo: 'MD5'
})
```

## Support Details

Device Product | Description  
---|---  
Xiaomi S1 Pro Sports Health Watch | Not supported  
Xiaomi Band 8 Pro | Not supported  
Xiaomi Band 9 / 9 Pro | Not supported  
Xiaomi Watch S3 | Supported  
Redmi Watch 4 | Not supported  
Xiaomi Wrist ECG Blood Pressure Monitor | Not supported  
Xiaomi Band 10 | Not supported  
Xiaomi Watch S4 | Supported  
REDMI Watch 5 | Supported  
REDMI Watch 6 | Supported
