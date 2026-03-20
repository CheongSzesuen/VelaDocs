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
---|---|---|---
data | String \| Uint8Array | No | Content to be computed. Either data or uri must be provided.
uri | String | No | Address of the file to be computed. Either data or uri must be provided.
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512 

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
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback 

#### success Return Value Object:

Parameter | Type | Description
---|---|---
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
---|---|---|---
data | String \| Uint8Array | No | Text to be signed. Either data or uri must be provided.
uri | String | No | Address of the file to be signed. Either data or uri must be provided.
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'<br>Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512
privateKey | String | Yes | Private key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback 

#### success Return Value Object:

Parameter | Type | Description
---|---|---
data | String \| Uint8Array | If input is a string, returns a base64-encoded string; otherwise, returns Uint8Array; if only uri is passed, returns string by default 

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
---|---|---|---
data | String \| Uint8Array | No | Text to be signed. Either data or uri must be provided.
uri | String | No | Address of the file to be signed. Either data or uri must be provided.
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'<br>Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512
signature | String \| Uint8Array | Yes | Signature
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
---|---|---|---
data | String \| Uint8Array | Yes | Data to be encrypted<br>string: plaintext to be encrypted, processed with 'utf-8' encoding by default<br>Uint8Array: other encoding formats such as hexadecimal or base64 need to be converted to this type
algo | String | No | Encryption algorithm. Default: RSA<br>Optional: RSA, AES
key | String \| Uint8Array | Yes | Key used for encryption<br>AES encryption mode supports 128-bit (Uint8Array 16 bytes) / 192-bit (Uint8Array 24 bytes) / 256-bit (Uint8Array 32 bytes) keys<br>String: string generated after base64 encoding; RSA encryption requires a PEM format string<br>Uint8Array: other encoding formats such as hexadecimal can be converted to this type
options | Object | No | Encryption parameters
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback 

#### RSA Parameters options:

Parameter | Type | Required | Description
---|---|---|---
transformation | String | No | Encryption mode and padding for RSA algorithm, supports "RSA/None/PKCS1Padding" 

#### AES Parameters options:

Type | Description
---|---
String | Computed digest content0 

#### transformation Support Details:

Type | Description
---|---
String | Computed digest content1 

#### success Return Value Object:

Type | Description
---|---
String | Computed digest content2 

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

Type | Description
---|---
String | Computed digest content3 

#### RSA Parameters options:

Type | Description
---|---
String | Computed digest content4 

#### AES Parameters options:

Type | Description
---|---
String | Computed digest content5 

#### transformation Support Details:

Type | Description
---|---
String | Computed digest content6 

#### success Return Value Object:

Type | Description
---|---
String | Computed digest content7 

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

Type | Description
---|---
String | Computed digest content8 

#### Return Value String:

Type | Description
---|---
String | Computed digest content9 

#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### crypto.atob(STRING)

Decodes a base-64 encoded string.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback0 

#### Return Value String:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback1 

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
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback2 

#### success Return Value Object:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback3 

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

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback4 

#### Return Value:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback5 

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
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback6 

#### success Return Value Object:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback7 

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
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback8 

#### Return Value:

Parameter | Type | Required | Description
---|---|---|---
data | String | Yes | Data to be computed
algo | String | No | Algorithm. Default: SHA256<br>Optional: MD5, SHA1, SHA256, SHA512
key | String | Yes | Key
success | Function | No | Success callback
fail | Function | No | Failure callback
complete | Function | No | Completion callback9 

#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ecdh.getPublicKey(encoding)

Get the public key from the generated key pair.

#### Parameters:

Parameter | Type | Description
---|---|---
data | String | Digest0 

#### Return Value:

Parameter | Type | Description
---|---|---
data | String | Digest1 

#### Example:

```javascript
import crypto from '@system.crypto' 
// or 
const crypto = require('@system.crypto')
```

### ecdh.setPrivateKey(Object)

Set the private key, will attempt to generate the associated public key with the set private key.

#### Parameters:

Parameter | Type | Description
---|---|---
data | String | Digest2 

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

Parameter | Type | Description
---|---|---
data | String | Digest3 

#### success Callback Return Value Object:

Parameter | Type | Description
---|---|---
data | String | Digest4 

#### Example:

```javascript
const digest = crypto.hashDigest({
  data: 'hello',
  algo: 'MD5'
})
```

## Support Details

Parameter | Type | Description
---|---|---
data | String | Digest5
