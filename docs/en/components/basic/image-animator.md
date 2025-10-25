<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/image-animator.html -->

# image-animator2+

## Overview

Image frame animation player.

## Subcomponents

Not supported

## Attributes

[Common attributes](</vela/quickapp/en/components/general/properties.html>) are supported.

Name | Type | Default Value | Mandatory | Description  
---|:---:|---|:---:|---  
images | `Array<ImageFrame>` |:---:| Yes | Sets the collection of image frame information. The frame information of each frame includes the image path, image size, and image position information.  
iteration | `<number>`|`<string>` | `infinite` | No | Sets the number of frame animation playbacks. **number** indicates a fixed number of times, and the **infinite** enumeration indicates infinite playbacks.  
reverse | `<boolean>` | `false` | No | Sets the playback sequence. **false** indicates that the playback starts from the first image to the last image; **true** indicates that the playback starts from the last image to the first image.  
fixedsize | `<boolean>` | `true` | No | Sets whether the image size is fixed to the component size. **true** indicates that the image size is the same as the component size. In this case, the **width** , **height** , **top** , and **left** attributes of the image are invalid. **false** indicates that the **width** , **height** , **top** , and **left** attributes of each image must be set separately.  
duration | `<string>` |:---:| No | Sets the duration of a single playback. The unit supports [s(second)|ms(millisecond)], and the default unit is ms.  
fillmode | `<string>` | `forwards` | No | Specifies the state of the frame animation after the execution is complete. The options are as follows:  
**none** : restores to the initial state.  
**forwards** : maintains the state of the frame animation at the end (defined in the last keyframe).  
  
Description of **ImageFrame**

Name | Type | Default Value | Mandatory | Description  
---|:---:|---|:---:|---  
src | `<uri>` |:---:| Yes | Image path  
width | `<length>` | 0 | No | Image width  
height | `<length>` | 0 | No | Image height  
top | `<length>` | 0 | No | Vertical coordinate of the image relative to the upper left corner of the component  
left | `<length>` | 0 | No | Horizontal coordinate of the image relative to the upper left corner of the component  
  
## Styles

[Common styles](</vela/quickapp/en/components/general/style.html>) are supported.

## Methods

[Common methods](</vela/quickapp/en/components/general/methods.html>) are supported.

Name | Parameters | Description  
---|:---:|---  
start |:---:| Starts playing the image frame animation. If this method is called again, the playback starts from the first frame.  
pause |:---:| Pauses the image frame animation.  
stop |:---:| Stops the image frame animation.  
resume |:---:| Continues to play the image frame.  
getState |:---:| Obtains the playback status. The options are as follows:  
\- **playing** : being played  
\- **paused** : paused  
\- **stopped** : stopped  
  
## Example Code
```html
< template > < div class = " container " > < image-animator class = " animator " id = " animator " images = " {{frames}} " duration = " 1s " /> < div class = " btn-box " > < input class = " btn " type = " button " value = " start " @click = " handleStart " /> < input class = " btn " type = " button " value = " stop " @click = " handleStop " /> < input class = " btn " type = " button " value = " pause " @click = " handlePause " /> < input class = " btn " type = " button " value = " resume " @click = " handleResume " /> </ div > </ div > </ template >
```

```css
.container { flex-direction : column ; justify-content : center ; align-items : center ; left : 0px ; top : 0px ; width : 454px ; height : 454px ; background-color : black ; } .animator { width : 70px ; height : 70px ; } .btn-box { width : 264px ; height : 120px ; flex-wrap : wrap ; justify-content : space-around ; align-items : center ; } .btn { border-radius : 8px ; width : 120px ; margin-top : 8px ; }
```

```js
export default { data : { frames : [ { src : "/common/asserts/001.png" , } , { src : "/common/asserts/002.png" , } , { src : "/common/asserts/003.png" , } , { src : "/common/asserts/004.png" , } , { src : "/common/asserts/005.png" , } ] , } , handleStart () { this . $element ('animator') . start () ; } , handlePause () { this . $element ('animator') . pause () ; } , handleResume () { this . $element ('animator') . resume () ; } , handleStop () { this . $element ('animator') . stop () ; } , } ;
```

![](../../images/image_animator.gif)
