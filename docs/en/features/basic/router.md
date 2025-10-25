<!-- 源地址: https://iot.mi.com/vela/quickapp/en/features/basic/router.html -->

# Page Routing

## Interface Declaration

No declaration is required.

## Importing the Module
```javascript
import router from '@system.router' // or const router = require('@system.router')
```

## Interface Definitions

### router.push(OBJECT)

Navigates to a page within the application.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
uri | String | Yes | The URI to navigate to, which can be in the following formats:  
1\. A complete URI containing the schema;  
2\. A path to a page within the application starting with '/'; for example, /about  
3\. The name of a page within the application not starting with '/'; for example, About  
4\. If the URI value is "/", it navigates to the page with the path "/", or to the home page if no such page exists.  
  
Complete URIs containing the schema are supported. For URIs with a schema, the processing flow is as follows:  
If the schema is hap (refer to [hap Links](</vela/quickapp/en/guide/framework/other/hap-schema.html>)), it navigates to the type supported by the hap link.  
params | Object | No | Data to be passed during navigation. Parameters can be used in the target page via `this.param1`, where param1 is the parameter name in the JSON. The value corresponding to param1 will be uniformly converted to the String type. When using the `this.param1` variable, you need to define a property with the same key name under `public` (for parameters passed outside the application) or `protected` (for parameters passed within the application) in the target page.  
  
#### params Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
___PARAM_LAUNCH_FLAG___ | String | No | JS application launch parameter. Currently only "clearTask" is supported. When launching the target page, it clears all other pages except this one. For details, see [Page Launch Modes](</vela/quickapp/en/guide/framework/other/launch-mode.html>).  
  
#### Examples:

  * Switching pages within the application

    * Switching by path
```javascript
router.push({ uri : '/about' , params : { testId : '1' } })
```

    * Switching by name
```javascript
// Open page by name router.push({ uri : 'About' , params : { testId : '1' } })
```

    * Switching pages and clearing others
```javascript
router.push({ uri : '/about' , params : { ___PARAM_LAUNCH_FLAG___ : 'clearTask' } })
```

### router.replace(OBJECT)

Replaces the current page with a page within the application and destroys the replaced page.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
uri | String | Yes | The URI to navigate to, which can be in the following formats:

  1. A path to a page within the application starting with '/'; for example, /about
  2. The name of a page within the application not starting with '/'; for example, About
  3. If the URI value is "/", it navigates to the page with the path "/", or to the home page if no such page exists.

  
params | Object | No | Data to be passed during navigation. Parameters can be used in the target page via `this.param1`, where param1 is the parameter name in the JSON. The value corresponding to param1 will be uniformly converted to the String type. When using the `this.param1` variable, you need to define a property with the same key name under `public` (for parameters passed outside the application) or `protected` (for parameters passed within the application) in the target page.  
  
#### Example:
```javascript
router.replace({ uri : '/test' , params : { testId : '1' } })
```

### router.back(OBJECT)

Returns to a specified page.

#### Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
path | String | No | The path of the target page to return to, which can be one of the following:

  1. If not provided, returns to the previous page
  2. A path to an already opened page within the application starting with '/'; for example, /about
  3. If the path value is "/", it navigates to the page with the name "/", or to the home page if no such page exists.

Notes:
  1. The path must be a path to an already opened page within the current application starting with '/', otherwise it is considered an invalid parameter and returns to the previous page.
  2. If no page matching the path is found, returns to the previous page.
  3. If multiple pages match the path parameter, returns to the most recently opened page.

  
  
#### Example:
```javascript
// Page A, open page by name router.push({ uri : 'B' })// Page B, open page by name router.push({ uri : 'C' })// Page C, open page by name router.push({ uri : 'D' })// Page D, open page by name router.push({ uri : 'E' })// Page E does not pass a page path, returns to Page D router.back() // Page D does not pass a page name, returns to Page C router.back() // Page C passes a page path, returns to Page A router.back({ path : '/A' })
```

### router.clear()

Clears all historical page records, keeping only the current page.

#### Parameters:

None

#### Example:
```javascript
router.clear()
```

### router.getLength()

Gets the number of pages in the current page stack.

#### Return Value:

Type | Description  
---|---  
Number | Number of pages  
  
#### Example:
```javascript
var length = router.getLength() console.log(` page's length = ${ length } `)
```

### router.getState()

Gets the current page state.

#### Return Parameters:

Parameter | Type | Description  
---|:---:|---  
index | Number | Position of the current page in the page stack  
name | String | Name of the current page  
path | String | Path of the current page  
  
#### Example:
```javascript
var page = router.getState() console.log(` page index = ${ page.index } `)console.log(` page name = ${ page.name } `)console.log(` page path = ${ page.path } `)
```

### router.getPages()

Gets the current page stack list.

#### Return Value:

Type | Description  
---|---  
Array | Page stack list. Each item in the array is of type Object.  
  
Each item in the array consists of:

Field | Type | Description  
---|:---:|---  
name | String | Name of the page  
path | String | Path of the page  
  
#### Example:
```javascript
var stacks = router.getPages() console.log('Name of the bottom page in the stack:' , stacks [ 0 ] . name)// e.g., list, detail, etc. console.log('Path of the bottom page in the stack:' , stacks [ 0 ] . path)// e.g., /list, /detail, /home/preview
```
