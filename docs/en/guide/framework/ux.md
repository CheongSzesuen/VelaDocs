<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/ux.html -->

# UX File

The APP and its pages are all written in files with the `.ux` suffix. These files consist of three parts: [template](</vela/quickapp/en/guide/framework/template/>), [style](</vela/quickapp/en/guide/framework/style/>), and [script](</vela/quickapp/en/guide/framework/script/>). A typical example of a page with the `.ux` suffix is shown below:
```html
< template > <!-- Only one root node is allowed in the template --> < div class = " page " > < text class = " title " > Welcome to {{title}} </ text > <!-- Click to navigate to the details page --> < input class = " btn " type = " button " value = " Navigate to Details Page " onclick = " routeDetail " > </ div > </ template > < style > .page { flex-direction : column ; justify-content : center ; align-items : center ; } .title { font-size : 30px ; text-align : center ; } .btn { width : 400px ; height : 60px ; margin-top : 75px ; border-radius : 43px ; background-color : #09ba07 ; font-size : 30px ; color : #ffffff ; } </ style > < script > import router from '@system.router' export default { // The data model for page-level components, affecting the override mechanism of incoming data: attributes defined within private are not allowed to be overridden private : { title : 'Example Page' } , routeDetail () { // Navigate to a page within the app. For more details on router usage, refer to: Documentation -> API -> Page Routing router.push ({ uri : '/DemoDetail' }) } } </ script >
```

## app.ux

After compilation, the current `app.ux` will include `manifest configuration information` (you can check the file content after running `npm run build`). Therefore, please do not delete the comment `/**manifest**/`.

You can import some common scripts in the `<script>` section and expose them on the current app object, as shown below. Then, you can access them in the ViewModel of the page `.ux` file via `this.$app.$def.util`.
```html
< script > /** * Application-level configuration, shared by all pages */ import util from './util' export default { showMenu : util.showMenu , createShortcut : util.createShortcut , util } </ script >
```
