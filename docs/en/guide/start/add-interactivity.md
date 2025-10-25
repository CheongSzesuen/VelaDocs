<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/start/add-interactivity.html -->

# Adding Interaction

In the previous chapter, we have already written the structure and style of two pages, but there is no connection between the two pages. In this chapter, we will implement page jumps.

## Registering Events

Page jumps are triggered by users and require adding corresponding events to specific elements on the page, such as `click`/`touchstart`. For more details about events, please refer to [General Events](</vela/quickapp/zh/components/general/events.html>).

In this weather forecast app, the interaction we use is swiping to switch pages:

  1. On the real-time weather page, swipe up to enter the 3-day weather forecast page;
  2. On the 3-day weather forecast page, swipe right to return to the real-time weather page.

We want the swipe action to perform the jump no matter where it occurs on the page, so we register the swipe event (`swipe`) on the root node.

The template code is as follows:
```html
< template > < div class = " page column " @swipe = " toListPage " > <!-- Other content of the page --> </ div > </ template >
```

Note

`@swipe="toListPage"` can also be written as `onswipe="toListPage"`. For details, please refer to [Event Binding](</vela/quickapp/zh/guide/framework/template/event.html>).

## Page Jump

After registering the event, we need to define the `toListPage()` callback method in the JavaScript code. By judging the swipe direction, we decide whether to perform a page jump. Page jumps require the use of the `@system.router` module. Please declare it in `manifest.json` before using it:
```js
{ // ... "features" : [ { "name" : "system.router" } ] }
```

Note

For more details about router, please refer to [Page Switching](</vela/quickapp/zh/guide/framework/page-switch.html>).

After declaring the module, you can import it in the JavaScript script and then use the API provided by `router` to jump between pages:
```html
< script > import router from '@system.router' export default { // ... toListPage (eve) { if (eve.direction === 'up') { router.push ({ uri : '/pages/list' }) } } } </ script >
```

Similarly, on the 3-day weather forecast page, use the same method to implement the page return logic. The corresponding code is:
```html
< template > < div class = " page column " @swipe = " toHomePage " > <!-- Other content of the page --> </ div > </ template >
```

```html
< script > import router from '@system.router' export default { // ... toHomePage (eve) { if (eve.direction === 'right') { router.back () } } } </ script >
```
