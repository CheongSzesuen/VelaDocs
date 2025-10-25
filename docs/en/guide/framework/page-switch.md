<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/page-switch.html -->

# Page Switching

## Switching Pages and Passing Parameters via the Router Interface

### Switching Pages

Before using the router interface, you need to import the module first.

You can switch pages using `router.push(OBJECT)`. For details about the `uri` parameter format supported by this method, refer to [Page Routing](</vela/quickapp/en/features/basic/router.html>).

**Example** :
```html
< template > < div class = " page " > < input class = " btn " type = " button " value = " Jump to New Page " onclick = " routePage " > </ input > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } .btn { width : 400px ; height : 60px ; margin-top : 70px ; border-radius : 30px ; background-color : #09ba07 ; font-size : 30px ; color : #ffffff ; } </ style > < script > // Import module import router from '@system.router' export default { routePage () { // Jump to a page within the app; cannot return to the current page router.replace ({ uri : '/Pages/newPage' }) } } </ script >
```

### Passing Parameters

The `params` parameter of the `router` interface can be used to configure parameters to be passed during page jumps.

**Example** :
```html
< template > < div class = " page " > < input class = " btn " type = " button " value = " Jump with Parameters " onclick = " routePageReplaceWithParams " > </ input > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } .btn { width : 400px ; height : 60px ; margin-top : 70px ; border-radius : 30px ; background-color : #09ba07 ; font-size : 30px ; color : #ffffff ; } </ style > < script > // Import module import router from '@system.router' export default { private : { title : 'Hello, world!' } , onInit () { console.info ('Switch pages and pass parameters via the router interface') } , routePageReplaceWithParams () { // Jump to a page within the app router.replace ({ uri : '/PageParams/receiveparams' , params : { key : this.title } }) } } </ script >
```

## Receiving Parameters

Now that you know how to pass parameters between pages using the `router` interface, how do you receive them?

It's actually very simple: the method for receiving parameters passed by the `router` interface is consistent: declare the properties to be used in the `protected` attribute of the page's ViewModel.

Note

  * Properties defined in `protected` can be overwritten by data passed from internal page requests within the app but not by data passed from external requests.
  * If you want parameters to be overwriteable by data passed from external requests, declare the properties in the `public` attribute of the page's ViewModel.

**Example** :
```html
< template > < div class = " page " > < text > page </ text > <!-- Display parameters passed to the page in the template --> < text > {{key}} </ text > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } </ style > < script > export default { protected : { key : '' } , onInit () { // Output parameters passed to the page in JavaScript console.info ('key: ' \+ this.key) } } </ script >
```
