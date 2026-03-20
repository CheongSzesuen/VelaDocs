<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/data/file.html -->

# File Storage

## Interface Declaration

```json
{ "name": "system.file" }
```

## Import Module

```javascript
import file from '@system.file' 
// or 
const file = require('@system.file')
```

## Interface Definition

### file.move(OBJECT)

Moves a source file to a specified location. For URI descriptions used in the interface, refer to [File Organization](</vela/quickapp/en/guide/framework/project-structure.html#uri>).

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file. Cannot be an app resource path or a tmp-type URI.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends. 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error 

#### Example:

```javascript
file.move({
  srcUri: 'internal://cache/path/to/file',
  dstUri: 'internal://files/path/to/file',
  success: function(uri) {
    console.log(`move success: ${uri}`)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.copy(OBJECT)

Copies a source file and stores it in a specified location. For URI descriptions used in the interface, refer to [File Organization](</vela/quickapp/en/guide/framework/project-structure.html#uri>).

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends. 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error 

#### Example:

```javascript
file.copy({
  srcUri: 'internal://cache/path/to/file',
  dstUri: 'internal://files/path/to/file',
  success: function(uri) {
    console.log(`copy success: ${uri}`)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.list(OBJECT)

Gets a list of files in a specified directory. For URI descriptions used in the interface, refer to [File Organization](</vela/quickapp/en/guide/framework/project-structure.html#uri>).

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
uri | String | Yes | Directory URI.
success | Function | No | Success callback, returns {fileList:[{uri:'file1', lastModifiedTime:1234456, length:123456} ...]}
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends. 

#### Return Values of success:

Parameter | Type | Description
---|---|---
fileList | Array | List of files, each in the format {uri:'file1', lastModifiedTime:1234456, length:123456} 

#### Metadata for Each File:

Parameter | Type | Description
---|---|---
uri | String | URI of the file, which can be accessed by other components or features.
length | Number | File size in bytes.
lastModifiedTime | Number | Timestamp of when the file was saved, in milliseconds from 1970/01/01 00:00:00 GMT. 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error 

#### Example:

```javascript
file.list({
  uri: 'internal://files/movies/',
  success: function(data) {
    console.log(data.fileList)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.get(OBJECT)

Gets file information for a local file. For URI descriptions used in the interface, refer to [File Organization](</vela/quickapp/en/guide/framework/project-structure.html#uri>).

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
uri | String | Yes | URI of the file. Cannot be an app resource path or a tmp-type URI.
recursive | Boolean | No | Whether to recursively get the file list in subdirectories. Default is false.
success | Function | No | Success callback, returns {uri:'file1', length:123456, lastModifiedTime:1233456}
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends. 

#### Return Values of success:

Parameter | Type | Description
---|---|---
uri | String | URI of the file, which can be accessed by other components or features.
length | Number | File size in bytes. Returns 0 when type = dir.
lastModifiedTime | Number | Timestamp of when the file was saved, in milliseconds from 1970/01/01 08:00:00.
type | String | File type: dir for directory, file for file.
subFiles | Array | When type = dir, returns the list of files in the directory. When recursive is true, also returns file information in subdirectories. 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error0 

#### Example:

```javascript
file.get({
  uri: 'internal://files/path/to/file',
  success: function(data) {
    console.log(data.uri)
    console.log(data.length)
    console.log(data.lastModifiedTime)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.delete(OBJECT)

Deletes a locally stored file. For URI descriptions used in the interface, refer to [File Organization](</vela/quickapp/en/guide/framework/project-structure.html#uri>).

#### Parameters:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error1 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error2 

#### Example:

```javascript
file.delete({
  uri: 'internal://files/path/to/file',
  success: function(data) {
    console.log('handling success')
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.writeText(OBJECT)

Writes text to a file.

WARNING

When using file write interfaces, ensure to clean up unused files promptly, especially on IoT devices with limited memory, to avoid memory overload and application crashes.

#### Parameters:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error3 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error4 

#### Example:

```javascript
file.writeText({
  uri: 'internal://files/work/demo.txt',
  text: 'test',
  success: function() {
    console.log('handling success')
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.writeArrayBuffer(OBJECT)

Writes a Buffer to a file.

WARNING

When using file write interfaces, ensure to clean up unused files promptly, especially on IoT devices with limited memory, to avoid memory overload and application crashes.

#### Parameters:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error5 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error6 

#### Example:

```javascript
file.writeArrayBuffer({
  uri: 'internal://files/work/demo',
  buffer: buffer,
  success: function() {
    console.log('handling success')
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.readText(OBJECT)

Reads text from a file.

#### Parameters:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error7 

#### Return Values of success:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error8 

#### Error Codes Returned by fail:

Error Code | Description
---|---
202 | Parameter error
300 | I/O error9 

#### Example:

```javascript
file.readText({
  uri: 'internal://files/work/demo.txt',
  success: function(data) {
    console.log('text: ' + data.text)
  },
  fail: function(data, code) {
    console.log(`handling fail, code = ${code}`)
  }
})
```

### file.readArrayBuffer(OBJECT)

Reads a Buffer from a file.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.0 

#### Return Values of success:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.1 

#### Error Codes Returned by fail:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.2 

#### Example:

```javascript
import file from '@system.file' 
// or 
const file = require('@system.file')
```

### file.access(OBJECT)

Checks if a file or directory exists.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.3 

#### Error Codes Returned by fail:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.4 

#### Example:

```javascript
import file from '@system.file' 
// or 
const file = require('@system.file')
```

### file.mkdir(OBJECT)

Creates a directory.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.5 

#### Error Codes Returned by fail:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.6 

#### Example:

```javascript
import file from '@system.file' 
// or 
const file = require('@system.file')
```

### file.rmdir(OBJECT)

Deletes a directory.

#### Parameters:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.7 

#### Error Codes Returned by fail:

Parameter | Type | Required | Description
---|---|---|---
srcUri | String | Yes | URI of the source file.
dstUri | String | Yes | URI of the destination file. Cannot be an app resource path or a tmp-type URI.
success | Function | No | Success callback, returns the URI of the destination file.
fail | Function | No | Failure callback.
complete | Function | No | Callback after execution ends.8 

#### Example:

```javascript
import file from '@system.file' 
// or 
const file = require('@system.file')
```
