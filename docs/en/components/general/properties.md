<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/general/properties.html -->

# Common Attributes

Common attributes are those supported by all components.

Developers can use `common attributes` on all component tags.

## Sample Code
```html
< template > < div > < text id = " text1 " class = " text-normal " > line 1 </ text > < text id = " text2 " class = " text-normal red " > line 2 </ text > </ div > </ template >
```

## Common Attributes

Name | Type | Default Value | Description  
---|:---:|---|---  
id | `<string>` |:---:| Unique ID  
style | `<string>` |:---:| Style declaration  
class | `<string>` |:---:| Reference to a style sheet  
  
## Rendering Attributes

Name | Type | Default Value | Description  
---|:---:|---|---  
for | `<array>` |:---:| Expands the current tag cyclically based on a data list  
if | `<boolean>` |:---:| Adds or removes the current tag based on a data boolean value  
show | `<boolean>` |:---:| Shows or hides the current tag based on a data boolean value, which is equivalent to controlling { display: flex | none }  
  
For details about how rendering attributes work, see [template](</vela/quickapp/en/guide/framework/template/>).

Note

Attributes and styles cannot be mixed. Do not set styles in the attribute field.

## data Attributes

Bind data attributes to components and then obtain them through `dataset` during runtime for further judgment.

**Example** :
```html
< template > < div > < div id = " elNode1 " data-person-name = " Jack " > </ div > </ div > </ template > < script > export default { onReady () { const el = this . $element ('elNode1') const elData = el.dataset.personName console.info (` Output data attribute: ${ elData } `) } } </ script >
```
