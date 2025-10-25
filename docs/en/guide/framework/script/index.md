<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/script/ -->

# script

Logical code used in the ux file to define the behavior of a page, including data objects, lifecycle interfaces, custom methods, and general methods.

## Syntax

Supports ES5 / ES6 syntax

### Module Declaration

You can import functional modules using `import` and call module methods in your code (refer to the interface documentation for details):
```javascript
import fetch from '@system.fetch'
```

### Code Reference

It is recommended to use `import` to import JS code, for example:
```javascript
import utils from '../common/utils.js'
```

Note

The JS application environment is not a Node.js environment, so do not import native Node.js modules such as `import fs from 'fs'`.

## Page Data Object

You can define page-level data objects in the page file for binding in the template and manipulation in page methods. For example:
```html
< template > < div > < text > {{a}} </ text > </ div > </ template > < script > export default { // Page data object, affects the override mechanism of incoming data: properties defined in private cannot be overridden private : { a : 1 } } </ script >
```

For more detailed information, refer to [Page Data Object](</vela/quickapp/en/guide/framework/script/page-data.html>).

## Lifecycle Interfaces

Both applications and pages have a predefined series of lifecycles. You can declare lifecycle hook functions in the script, which will be called when the application/page reaches a specific lifecycle stage. For example:
```javascript
// This function will be executed when the application/page is initialized onInit() { console.log('page initialized！')}
```

For more detailed information, refer to [Lifecycle](</vela/quickapp/en/guide/framework/script/lifecycle.html>).

## Custom Methods

Developers can declare custom methods as needed in the application/page ux file, including utility methods, event callback methods, etc. For example:
```javascript
onBtnClick() { console.log('button clicked!')}
```

## Global Objects and Methods

Properties and methods declared by developers in the application ux file (`app.ux`) can be accessed in any page via `this.$app.$def`. For more details, refer to [Global Objects and Methods](</vela/quickapp/en/guide/framework/script/global-data-method.html>).

## General Methods

The framework provides some predefined general methods that can be called by pages/components. For more details, refer to [General Methods](</vela/quickapp/en/components/general/methods.html>).
