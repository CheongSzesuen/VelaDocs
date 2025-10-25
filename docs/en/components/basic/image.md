<!-- 源地址: https://iot.mi.com/vela/quickapp/en/components/basic/image.html -->

# image

## Overview

Render images.

## Subcomponents

Not supported.

## Attributes

Supports [General Attributes](</vela/quickapp/en/components/general/properties.html>).

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
src | `<uri>` |:---:| No | URI of the image, supporting both local and cloud paths. Supported image formats include png and jpg.  
alt | `<uri>` | 'blank' |:---:| No | Placeholder image displayed during loading; only supports local image resources.  
  
Note: Details about the alt attribute are as follows:

  * If the alt value is not set for the Image component, the terminal will add a default gray placeholder image.

  * When src is a local image address, there will be no placeholder image.

  * When src is a remote image address, if the image has been successfully loaded before and cached locally, there will be no placeholder image.

  * When src is a remote image address and the alt value of the Image component is set to the string "blank", there will be no placeholder image (this can avoid the instant flickering of small icons from remote addresses during the first load).

  * When alt is set to a local image address, the placeholder image scaling mode is changed from center-no-scaling to center-keep-aspect-ratio scaling, reducing the resolution and size of the placeholder image resource file.

Note: The scaling mode can be configured through the style value `object-fit`, with a default value of `cover` (center-keep-aspect-ratio scaling). For details, see the Style section.

## Style

Supports [General Styles](</vela/quickapp/en/components/general/style.html>).

Name | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
object-fit | contain | cover | none | scale-down | cover | No | Scaling type of the image.  
  
Note:

  1. The object-fit parameter list is as follows:

Type | Description  
---|---  
contain | Maintains aspect ratio, scales down or up so that the image is fully displayed within the display boundary, centered.  
cover | Maintains aspect ratio, scales down or up so that both sides are greater than or equal to the display boundary, centered.  
none | Centers without scaling.  
scale-down | Maintains aspect ratio, scales down or remains unchanged, takes the smaller display between `contain` and `none`, centered.  
  
## Events

Supports [General Events](</vela/quickapp/en/components/general/events.html>).

Name | Parameters | Description  
---|:---:|---  
complete | {width: widthValue(px), height: heightValue(px)} | Triggered when the image is fully loaded.  
error |:---:| Triggered when the image fails to load.  
  
## Sample Code
```html
< template > < div > < image src = " /common/logo.png " /> </ div > </ template >
```

![](../../images/image-example.png)
