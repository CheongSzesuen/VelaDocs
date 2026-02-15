<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/security/crypto.html -->

# Cryptographic Algorithm crypto

## Interface Declaration
```json
{ "name" : "system.crypto" }
```

## Module Import
```javascript
import crypto from '@system.crypto' // or const crypto = require('@system.crypto')
```

## Interface Definition

### crypto.hashDigest(OBJECT)

Create a hash digest of data.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Content to be computed. Either data or uri must be provided.  
uri | String | No | Address of the file to be computed. Either data or uri must be provided.  
algo | String | No | Algorithm. Default: SHA256   
Optional: MD5, SHA1, SHA256, SHA512  
  
#### Return Value:

Type | Description  
---|---  
String | Computed digest content  
  
#### Example:
```javascript
const digest = crypto.hashDigest({ data : 'hello' , algo : 'MD5' })
```

### crypto.hmacDigest(OBJECT)

Create a cryptographic HMAC digest.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Yes | Data to be computed  
algo | String | No | Algorithm. Default: SHA256   
Optional: MD5, SHA1, SHA256, SHA512  
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
crypto.hmacDigest({ data : 'hello' , algo : 'SHA256' , key : 'a secret' , success : function(res){ console.log(` ### crypto.hmacDigest success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.hmacDigest fail ### ${ code } : ${ data } `)} })
```

### crypto.sign(OBJECT)

Used to generate a signature.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Text to be signed. Either data or uri must be provided.  
uri | String | No | Address of the file to be signed. Either data or uri must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   
Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512  
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
crypto.sign({ data : 'hello' , algo : 'RSA-SHA256' , privateKey : 'a secret' , success : function(res){ console.log(` ### crypto.sign success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.sign fail ### ${ code } : ${ data } `)} })
```

### crypto.verify(OBJECT)

Used to verify a signature.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | No | Text to be signed. Either data or uri must be provided.  
uri | String | No | Address of the file to be signed. Either data or uri must be provided.  
algo | String | No | Signature algorithm. Default: 'RSA-SHA256'   
Optional: RSA-MD5, RSA-SHA1, RSA-SHA256, RSA-SHA512  
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
crypto.verify({ data : 'hello' , algo : 'RSA-SHA256' , publicKey : 'public key' , signature : 'signature' , success : function(data){ console.log(` ### crypto.verify success: ` , data)} , fail : function(data , code){ console.log(` ### crypto.verify fail ### ${ code } : ${ data } `)} })
```

### crypto.encrypt(OBJECT)

Encryption.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | Yes | Data to be encrypted   
string: plaintext to be encrypted, processed with 'utf-8' encoding by default   
Uint8Array: other encoding formats such as hexadecimal or base64 need to be converted to this type  
algo | String | No | Encryption algorithm. Default: RSA   
Optional: RSA, AES  
key | String | Uint8Array | Yes | Key used for encryption   
AES encryption mode supports 128-bit (Uint8Array 16 bytes) / 192-bit (Uint8Array 24 bytes) / 256-bit (Uint8Array 32 bytes) keys   
String: string generated after base64 encoding; RSA encryption requires a PEM format string   
Uint8Array: other encoding formats such as hexadecimal can be converted to this type  
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
transformation | String | No | Encryption mode and padding for AES algorithm, defaults to "AES/CBC/PKCS7Padding"   
See transformation support details  
iv | String | No | Initialization vector for AES encryption/decryption, string after base64 encoding   
AES CBC/ECB mode:   
Default value is key   
Default value extraction method:   
1\. If key is a string, the string is decoded and the byte content is used as iv   
2\. If key is a uint8array, the byte content is used as iv   
AES-CCM mode:   
No default value  
ivOffset | Number | No | Offset of the initialization vector for AES encryption/decryption, integer, default is 0  
ivLen | Number | No | Byte length of the initialization vector for AES encryption/decryption, integer   
AES CBC/ECB mode: default is keyLen 16   
AES-CCM mode: no default value  
aad | String | Uint8Array | No | Additional authenticated data for AES-CCM encryption, provides additional authentication information during encryption   
String: string after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
tagLen | Number | No | Length of the authentication tag generated by AES-CCM encryption   
Must be even, valid range is 4~16   
Default is 4  
  
#### transformation Support Details:

Padding Mode / Encryption Mode | CBC | ECB | CCM  
---|:---:|---|---  
PKCS5Padding | AES/CBC/PKCS5Padding | AES/ECB/PKCS5Padding | -  
PKCS7Padding | AES/CBC/PKCS7Padding | AES/ECB/PKCS7Padding | -  
NoPadding | AES/CBC/NoPadding |:---:| AES/CCM/NoPadding  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Uint8Array | Encrypted data   
If input data is a string, returns a base64-encoded string; otherwise, returns Uint8Array  
tag | String | Uint8Array | AES-CCM encryption returns an authentication tag   
If input data is a string, returns a base64-encoded string; otherwise, returns Uint8Array  
  
#### Example:
```javascript
// AES-CBC Encryption crypto.encrypt({ // Text content to be encrypted data : 'hello' , // Encryption public key after base64 encoding key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , success : function(res){ console.log(` ### crypto.encrypt success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.encrypt fail ### ${ code } : ${ data } `)} })
```

```javascript
// AES-CCM Encryption crypto.encrypt({ // Text content to be encrypted data : 'hello' , // Encryption public key after base64 encoding key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , options : { transformation : 'AES/CCM/NoPadding' , iv : crypto.btoa('iv_info'), aad : crypto.btoa('Associated Data'), tagLen : 16 } , success : function(res){ console.log('### crypto.encrypt success:' , res.data , res.tag)} , fail : function(data , code){ console.log('### crypto.encrypt fail ### ' , code , data)} })
```

### crypto.decrypt(OBJECT)

Decryption.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
data | String | Uint8Array | Yes | Data to be decrypted   
String: data to be decrypted, processed with base64 encoding by default   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
algo | String | No | Decryption algorithm. Default: RSA   
Optional: RSA, AES  
key | String | Uint8Array | Yes | Key used for encryption   
AES encryption mode supports 128-bit (Uint8Array 16 bytes) / 192-bit (Uint8Array 24 bytes) / 256-bit (Uint8Array 32 bytes) keys   
String: string generated after base64 encoding; RSA encryption requires a PEM format string   
Uint8Array: other encoding formats such as hexadecimal can be converted to this type  
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
transformation | String | No | Encryption mode and padding for AES algorithm, defaults to "AES/CBC/PKCS7Padding"   
See transformation support details  
iv | String | No | Initialization vector for AES encryption/decryption, string after base64 encoding   
AES CBC/ECB mode:   
Default value is key   
Default value extraction method:   
1\. If key is a string, the string is decoded and the byte content is used as iv   
2\. If key is a uint8arrary, the byte content is used as iv   
AES-CCM mode:   
No default value  
ivOffset | Number | No | Offset of the initialization vector for AES encryption/decryption, integer, default is 0  
ivLen | Number | No | Byte length of the initialization vector for AES encryption/decryption, integer   
AES CBC/ECB mode: default is keyLen 16   
AES-CCM mode: no default value  
aad | String | Uint8Array | No | Additional authenticated data for AES-CCM encryption, provides additional authentication information during encryption   
String: string after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
tag | String | Uint8Array | No | Authentication tag for AES-CCM, used to verify data integrity and authenticity   
String: string after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
  
#### transformation Support Details:

Padding Mode / Encryption Mode | CBC | ECB | CCM  
---|:---:|---|---  
PKCS5Padding | AES/CBC/PKCS5Padding | AES/ECB/PKCS5Padding | -  
PKCS7Padding | AES/CBC/PKCS7Padding | AES/ECB/PKCS7Padding | -  
NoPadding | AES/CBC/NoPadding |:---:| AES/CCM/NoPadding  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
data | String | Uint8Array | Decrypted data   
If input data is a string, returns plaintext after decryption. If the decrypted content cannot be converted to a utf-8 string, an error will occur (CODE: 200); otherwise, returns Uint8Array  
  
#### Example:
```javascript
// AES-CBC Decryption crypto.decrypt({ // Content to be decrypted data : 'WB96uM08PfYIHu5G1p6YwA==' , // Encryption public key after base64 encoding key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , success : function(res){ console.log(` ### crypto.decrypt success: ` , res.data)} , fail : function(data , code){ console.log(` ### crypto.decrypt fail ### ${ code } : ${ data } `)} })
```

```javascript
// AES-CCM Decryption crypto.decrypt({ // Text content to be decrypted data : '9KFkqz8=' , // Encryption public key after base64 encoding key : crypto.btoa('KEYKEYKEYKEYKEYK'), algo : 'AES' , options : { transformation : 'AES/CCM/NoPadding' , iv : crypto.btoa('iv_info'), aad : crypto.btoa('Associated Data'), tag : 'kHX6EGYOEvKwA0PS79TAUQ==' } , success : function(res){ console.log('### crypto.decrypt success:' , res.data)} , fail : function(data , code){ console.log('### crypto.decrypt fail ### ' , code , data)} })
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
const encodeData = crypto.btoa('hello')
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
const encodeString = crypto.btoa('hello')const res = crypto.atob(encodeString)
```

### crypto.hkdf(OBJECT)

Create a derived key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
algo | String | No | Digest algorithm to be used. Default: SHA256   
Optional: SHA256, SHA512  
key | String | Uint8Array | Yes | Key material, source key   
String: string generated after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
salt | String | Uint8Array | Yes | Salt value   
String: string generated after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
info | String | Uint8Array | Yes | Additional information value. Length cannot exceed 1024 bytes   
String: string generated after base64 encoding   
Uint8Array: other encoding formats such as hexadecimal need to be converted to this type  
keyLen | Number | Yes | Length of the key to be generated, in bytes   
Maximum allowed value is 255 times the number of bytes produced by the selected digest function (e.g., sha256 produces 32-byte hashes, maximum HKDF output is 8160 bytes; sha512 produces 64-byte hashes, maximum HKDF output is 16320 bytes)  
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
// Convert hexadecimal string to uint8Array function hexToUint8Array(hex){ // Remove possible prefix 0x hex = hex.replace(/ ^0x / , ''); // If length is odd, pad with a leading zero if(hex.length % 2 !== 0){ hex = '0' \+ hex ; } // Check for invalid characters if(/ [^0-9A-Fa-f] / . test(hex)) { throw new Error('Invalid hex string: contains non-hexadecimal characters.'); } // Calculate length of byte array const byteLength = hex.length / 2 ; const bytes = new Uint8Array(byteLength); // Convert each pair of hexadecimal characters to a byte for(let i = 0 ; i < byteLength ; i ++){ const byteString = hex.substr(i * 2 , 2); bytes [ i ] = parseInt(byteString , 16); } return bytes ; } // Convert uint8Array to hexadecimal string function uint8ArrayToHex(bytes){ if(!(bytes instanceof Uint8Array)) { throw new TypeError('Expected input to be an instance of Uint8Array.'); } // Convert each byte to a two-digit hexadecimal string return Array.from(bytes , byte => byte.toString(16). padStart(2 , '0')) . join(''); } /** * Create Base64 decoding table (outside the function, created only once) */ const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' ; const base64Map = new Map() ; for(let i = 0 ; i < base64Chars.length ; i ++){ base64Map.set(base64Chars [ i ] , i); } // Convert Base64 encoded string to Uint8Array function base64ToUint8Array(base64){ // Remove possible whitespace characters from Base64 string base64 = base64.trim() ; // Base64 length must be a multiple of 4 if(base64.length % 4 !== 0){ throw new Error('Invalid Base64 string length'); } // Calculate number of padding characters const padding = base64.endsWith('==')? 2 :(base64.endsWith('=')) ? 1 : 0 ; // Calculate length of output array const outputLength =(base64.length * 3)/ 4 \- padding ; const output = new Uint8Array(outputLength); let buffer = 0 ; let bufferLength = 0 ; let outputIndex = 0 ; for(let i = 0 ; i < base64.length ; i ++){ const char = base64 [ i ] ; if(char === '=')continue ; const value = base64Map.get(char); if(value === undefined){ throw new Error('Invalid Base64 character'); } buffer =(buffer << 6)| value ; bufferLength += 6 ; if(bufferLength >= 8){ bufferLength -= 8 ; output [ outputIndex ++ ] =(buffer >> bufferLength)& 0xFF ; } } return output ; }
```

utf8-String
```javascript
// Define input parameters const key = crypto.btoa('initialkeymaterial'); // Initial key material const salt = crypto.btoa('salt'); // Salt const info = crypto.btoa('info'); // Additional information const keyLen = 32 ; // Length of the key to be generated crypto.hkdf({ key , salt , info , keyLen , success(res){ try { const derivedKey = res.data console.log('Derived Key (hex): ' , uint8ArrayToHex(derivedKey)) ; // Derived key (hex): 00e02dcb12e9ca343bc57a1441ccd76a845d9f80e716cfc5a61f8daea81e57ec } catch(e){ console.error('Decoding error:' , e.message); } } , fail(msg , code){ console.log('crypto.hkdf error:' , msg , code); } })
```

Hexadecimal
```javascript
// Define input parameters const key = hexToUint8Array('696e697469616c6b65796d6174657269616c'); // Initial key material initialkeymaterial hex const salt = hexToUint8Array('73616c74'); // Salt salt hex const info = hexToUint8Array('696e666f'); // Additional information info hex const keyLen = 32 ; // Length of the key to be generated crypto.hkdf({ key , salt , info , keyLen , success(res){ try { const derivedKey = res.data console.log('Derived Key (hex): ' , uint8ArrayToHex(derivedKey)) ; // Derived key (hex): 00e02dcb12e9ca343bc57a1441ccd76a845d9f80e716cfc5a61f8daea81e57ec } catch(e){ console.error('Decoding error:' , e.message); } } , fail(msg , code){ console.log('crypto.hkdf error:' , msg , code); } })
```

base64
```javascript
// Define input parameters const key = 'aW5pdGlhbGtleW1hdGVyaWFs' ; // Initial key material initialkeymaterial base64 const salt = 'c2FsdA==' ; // Salt salt base64 const info = 'aW5mbw==' ; // Additional information info base64 const keyLen = 32 ; // Length of the key to be generated crypto.hkdf({ key , salt , info , keyLen , success(res){ try { const derivedKey = res.data console.log('Derived Key (hex): ' , uint8ArrayToHex(derivedKey)) ; // Derived key (hex): 00e02dcb12e9ca343bc57a1441ccd76a845d9f80e716cfc5a61f8daea81e57ec } catch(e){ console.error('Decoding error:' , e.message); } } , fail(msg , code){ console.log('crypto.hkdf error:' , msg , code); } })
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
// Create an ECDH object using the secp256r1 curve const ecdh = crypto.createECDH('secp256r1');
```

### ECDH

Elliptic Curve Diffie-Hellman (ECDH) key exchange object.

### ecdh.generateKeys(Object)

Generate a key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned public key. Default is buffer   
Supports base64, hex, buffer  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Return Value Object:

Parameter | Type | Description  
---|:---:|---  
publicKey | String | Uint8Array | Public key from the generated key pair, returned in different types based on the set public key encoding format   
base64, hex return String, buffer returns Uint8Array  
  
#### Example:
```javascript
// Create an ECDH object using the secp256r1 curve const ecdh = crypto.createECDH('secp256r1'); ecdh.generateKeys({ encoding : 'base64' , success : function(res){ console.log('### generateKeys success publicKey: ' , res.publicKey)} , fail : function(data , code){ console.log('### generateKeys fail ### ' , code , data)} })
```

### ecdh.getPrivateKey(encoding)

Get the private key from the generated key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned private key, default is buffer   
Supports base64, hex, buffer  
  
#### Return Value:

Type | Description  
---|---  
String | Uint8Array | Returns the corresponding type based on the encoding parameter:   
base64, hex encoding return String   
buffer encoding returns Uint8Array  
  
#### Example:
```javascript
const privateKey = ecdh.getPrivateKey('hex'); console.log('privateKey hex: ' , privateKey);
```

### ecdh.getPublicKey(encoding)

Get the public key from the generated key pair.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
encoding | String | No | Defines the encoding format of the returned public key, default is buffer   
Supports base64, hex, buffer  
  
#### Return Value:

Type | Description  
---|---  
String | Uint8Array | Returns the corresponding type based on the encoding parameter:   
base64, hex encoding return String   
buffer encoding returns Uint8Array  
  
#### Example:
```javascript
const publicKey = ecdh.getPublicKey('hex'); console.log('publicKey hex: ' , publicKey);
```

### ecdh.setPrivateKey(Object)

Set the private key, will attempt to generate the associated public key with the set private key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
privateKey | String | Uint8Array | Yes | Private key value to be set:   
String type: must be a PEM format string   
Uint8Array type: byte array converted from other formats (such as hexadecimal)  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### Example:
```javascript
// Create an ECDH object using the secp256r1 curve const ecdh = crypto.createECDH('secp256r1'); const key = '-----BEGIN EC PRIVATE KEY-----\n' \+ 'MHcCAQEEIB6c3X+2K7f3B3XXo4KPbQv0YP5ddTx0/zh8S2C0AXfkoAoGCCqGSM49\n' \+ 'AwEHoUQDQgAEp4K5yOimfJxvZ0fX0TQh4h2d7G2JDo5pujpJwZmLdrX7vF7Lp1HU\n' \+ 'AoIttMRXxktBjdvY9m7hfRp/Uu9paU7X3Q==\n' \+ '-----END EC PRIVATE KEY-----' ecdh.setPrivateKey({ privateKey : key , success :() => { console.log('#### privateKey: ' , ecdh.getPrivateKey('base64')) console.log('#### publicKey: ' , ecdh.getPublicKey('base64')) } , fail :(data , code)=> { console.log('### setPrivateKey fail ### ' , code , data)} })
```

### ecdh.computeSecret(Object)

Compute the shared secret using the provided public key.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
otherPublicKey | String | Uint8Array | Yes | Other party's public key used to compute the shared secret  
inputEncoding | String | No | Encoding format of the provided public key, default is buffer   
Supports base64, hex, buffer  
outputEncoding | String | No | Encoding format of the returned computed shared secret, default is buffer   
Supports base64, hex, buffer  
success | Function | No | Success callback  
fail | Function | No | Failure callback  
complete | Function | No | Completion callback  
  
#### success Callback Return Value Object:

Parameter | Type | Description  
---|:---:|---  
shareKey | String | Uint8Array | Generated computed shared secret  
  
#### Example:
```javascript
async function fn() { try { // Create Alice's ECDH object and generate key pair const alice = crypto.createECDH('secp256r1'); // Create Bob's ECDH object and generate key pair const bob = crypto.createECDH('secp256r1'); // Interface processing as promise const aliceGen = promisify(alice.generateKeys)const bobGen = promisify(bob.generateKeys)const aliceCompute = promisify(alice.computeSecret)const bobCompute = promisify(bob.computeSecret)await aliceGen() await bobGen() // Get Alice's and Bob's public keys const alicePublicKey = alice.getPublicKey('hex'); const bobPublicKey = bob.getPublicKey('hex'); // Alice computes the shared secret using Bob's public key const { shareKey : aliceSharedSecret } = await aliceCompute(bobPublicKey , 'hex' , 'hex'); // Bob computes the shared secret using Alice's public key const { shareKey : bobSharedSecret } = await bobCompute(alicePublicKey , 'hex' , 'hex'); // Print results console.log('Alice Public Key:' , alicePublicKey); console.log('Bob Public Key:' , bobPublicKey); console.log('Alice Shared Secret:' , aliceSharedSecret); console.log('Bob Shared Secret:' , bobSharedSecret); // Verify shared secrets are the same if(aliceSharedSecret === bobSharedSecret){ console.log('Shared secrets match!'); } else { console.log('Shared secrets do not match!'); } } catch(e){ console.log('error： ' , e)} } fn()
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
