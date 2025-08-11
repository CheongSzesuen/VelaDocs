<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/image.html -->

# image

## 概述

渲染图片

## 子组件

不支持

## 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
src | `<uri>` |:---:| 否 | 图片的 uri，同时支持本地和云端路径，支持的图片格式包括png，jpg  
alt | `<uri>` | 'blank' |:---:| 否 | 加载时显示的占位图；只支持本地图片资源  
  
注意：alt 属性详情如下：

  * 如果 Image 组件没有设置 alt 值，终端会加上默认的灰色占位图；

  * src 为本地图片地址时，不会有占位图；

  * src 为远程图片地址时，如果之前已经成功加载过图片，有本地缓存，则不会有占位图；

  * src 为远程图片地址时，且 Image 组件 的 alt 值传入字符串 "blank" 值，不会有占位图（可避免一些远程地址的小图标第一次加载时瞬间闪烁的现象）；

  * 设置 alt 为本地图片地址时，占位图缩放模式由原来的居中不缩放改为居中保持宽高比缩放，减少了占位图资源文件的分辨率与体积大小。

注：缩放模式可以通过样式值`object-fit`配置，默认值为`cover`（居中保持宽高比缩放），详情查看样式一节

## 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|:---:|---|:---:|---  
object-fit | contain | cover | none | scale-down | cover | 否 | 图片的缩放类型  
  
注意：

  1. object-fit参数列表如下：

类型 | 描述  
---|---  
contain | 保持宽高比，缩小或者放大，使得图片完全显示在显示边界内，居中显示  
cover | 保持宽高比，缩小或者放大，使得两边都大于或等于显示边界，居中显示  
none | 居中，无缩放  
scale-down | 保持宽高比，缩小或保持不变，取 `contain` 和 `none`中显示较小的一个，居中显示  
  
## 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

名称 | 参数 | 描述  
---|:---:|---  
complete | {width: widthValue(px), height: heightValue(px)} | 图片加载完成时触发  
error |:---:| 图片加载失败时触发  
  
## 示例代码
```html
< template > < div > < image src = " /common/logo.png " /> </ div > </ template >
```

![](../../data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHwAAAB/CAIAAACi6DFHAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAOCElEQVR4nO2daWwc53mAn5nZ++ItUqJEKY6d+EQdu7ZlG+ivokWRAvGfIEjgOMiBoGjRX0FgBAjqxAlq1DVqO0hRJHUNFz5qV76tyNZly7IiUmIkUxJFXZRIiqR4Lo+9r5npj93RUiZF7vXtzLB6IAic4XLmnWdnv/mO9/tW0nWdG9QX2ewA/j9yQ7oJ3JBuAjekm8AN6SZgXempLJmc2UGIwbrSxxbYcZyFpNlxCMC60m9u49NBnvrI7DgEYF3pwNc28/R+/veY2XHUGktL/9s7aQ7y3VfpHzM7lJpiaelbmrl/K5lRfvwGczGzo6kdlpYOPNwFbXT385O3zQ6ldlhd+gPb8AXBzUvdPLvP7GhqhNWl372ZZi8oIPHL3Xx63uyAaoHVpTf5uLMNAC+Lizz+/noo3K0u3eHg7k4jzABHzvPEH0wOqXqsLh24rQMADRzg4bef8upRk0OqEptIV0ADHdyg8s+7GZ83O6wqsIH0kIfNIbg6qhhgYJRf7DIzpCqxgfS2ALe2gWp4V8DFy728f8LkwCrGBtKb/WxrAc3Y1sFLOsWv9zC1aGZgFWMD6UhsCi2RnsdH7wV+f8iciKrEDtKho8F4kF5FARfPHeTEqGlRVYw9pHeGkAPLbnY3c/M8f8CUiKrCHtJb/Wzwg3rtXhk8vHycj/rNiapi7CG9yUejd9mdDrjJxXj+oAkhVYM9pPvd+F3XlulX8bLnHO98Xu+QqsEe0tsCtAaWFS953GgJXuhBXfG3lsQe0hUJZZVI/ew6zc5T9YunSuwh3eUi5FmpTM/jhCwvHCaVqWtUFWMP6UCL7/rSAQ87z7F7oH7xVINtpKurp9E7Ic3vD1/nYWsxbCN9DSRw0H2ZnktmR1IC60U64GZ+gdfskJm0jqQrILFrgAuTZkeyFutIug4+Ll7hD5Z/nK4j6YAMEu+dImrtXN/1JR3wcWCQ7iGzw1iVdSddgQz7zpkdxqqsO+kSOHnrlKVH8mwjXZZKfqnCpTkOW7jCbhvp8QyU6N0BaT6w8MiGPaTncszFQSnt1TLo9IxZN+vRHtJlkKRy+lVcjMzx2QWBIVWDPaTPJ1lIlBOsi0SEAxcFhlQN9pAejhNOlFy8ABLonJwglhIYVcXYQ3o8TaL0B2keDwNT9I8DZFVrzQO2h/TpGFOxcu50wMnkNJ+PAzgV9p2l/4qY4MrHHtKnoiRiZQYrgcSJ8cLW8By/2EnaGve7PaTPxCFXZvECODlxhYkFgO1f4tAQP39fQHDlYw/p4wuF7vIykEDm9BSTEYB7tnDbRp75gHf7xIRYDjaQnkhzeb6iSGWiSS7MFLa2b4Mk/gmA2YX7jaQvpBgZK5C6cA5YyDpgS58Wxgb4fF3yWRrGGDZ2ED6dIyBmcIARXnIoHN8HE0DuKODjiB42XmS5z4REGg5cVmdkTkSqYoilUCnf4pIEuCWDWxqAAkUfrWXT87WOtCSsYH081NApZFKzKUYXywc4abGQoJ1bJEnPiRuUnvV8tJ1+sZBL79syaMQz3B2orB1x0ZwgQZ+Pjtr2oQCq0uPp+mbAK3SSGXSGYbCha1b23E4QQMnyPzmAMdGahdrGUFZmzOTjEfL7ABYigxZRoyZvlubccnG9KUAU2Ge2WdCJp7VpR8ZZjEJjkr/XoYMFxcKWx0hNgWXJKL6eP0k79Z9PqrVpXePQFmdusuRmU+g5gB8br7cXKjVQCHt9On9ROv7RLW09HiK09NApU/RPArRNNMxAL+LzgbAkC6Bh+4hXj5SXaBlYmnpJ0cZWwB3dUdRiKaYiQLIMpsarv2tE3K8dJRIorqzlIOlpX98kdlZcFV3FIlUrliAtIeAax+eXnov8kpvdWcpBwtL1zl2GdTqCnRAIZxgzHiWbggWDl7ECRov9jBfr+wB60o/McaRUfBVXaWTUHOkjB6uoHvZNBodAhwb4n/qldtuXendw1yZAWctjqWTMsaMGr34l894V0DitWMs1qVkt6j0dJb9ZwtDbtWiQIJhI7WxycPG5dIBN3+8zMd1yTy1qPThMJ8MgaMW0iXQiqOjWn7O2PLDOiDN68erPl0JWFT6wQuEyx3+XwUJybjQRi/tK06+lkDm4DBnxI8rWVK6zlsnIVtF6/6+FwEvaCv9Hx2Mzlbj8epFaX/aYRjYxUNFZWApqNebxKwAiqfDArvZ7ei9Lf7mF0Ejxnn9nFklL1nxJ7EctJnIuw5V0UHepU4yC5yYFDsSSwn/Z2THBsCn0mnz3eBjXBlYe3XVoy1pKcyvNUHWu3qLRXgpHeMC9MCz2At6YcG2XPevNs8j4ye5jORJYyVpOv87jBkBNQUdfRVli35AjIo9AwXu2tqjoWkH77IuwPgrHVNUQMnrcanR8rPpFkFCSSOjjMmbA1lC0l/pZdcoure8+Vo4KUzVNiSSrlmhdkkfcKW2bSK9L7LvN0PipiI9EJmHbCYYja+VstLRs9yQtj3/FhF+r8fYmoWvAIOreHzGGMXEEszF1/ruhXI0L2+pe87wyu94BYTjkrjEumsWaYXXsTwPNMRAfFYQbqq8V+HScXBLSbvR8ProsH4DM3GuRwp4bqdzMY5LabH0Xzp7/exo19MwZJHI+imLVDYSuXQ0iVUkBQiSUbnhERksvRkmt8cRE3VaFhuRVRCHpoM6VPR0gakHOhx+sW0S02W/rtDHDgPbiG9uFBI9233F3dMllhMS6AWkyBri5nSB6d49lPQRd7mGri4paW4Yy4/9FzKe+xkJk5cwMpUZkp/ai+Xx8G/9isrRwMnm42srlSW4VmgNOkKs/FCPl5tMU3667282A0BwSFoBNx8tb2wFU9zqfRno8xifiGIWmOO9HCUZz+GHFxvVfRaoeJ3crMhPZFhKJ+LUcqdLhNLExEwdGeO9Cc/5OgQBNZ+ZVXoAJtDtBol2HS0nBWSZOYShNfHnf7mcX77GTjEj1ToIHFvJz4j7/f8FGm15It2QIwJAY3Seksfm+PJj9Cy4BU/70QDuHNjccepcbRMyW+2DjIOAXdGXaXrGj99j1NDgmssxfOBwlfaizsGZiBbzkVLxAUshF9X6f+2n9d7wF+vIVCVrY1saypsxZIML5QzO1ICuZhjXUPqJ33/GZ7YDU5w1mVCmw4qd3SwsbGwY2CSmZjIhljJ1En68Ax/ybxqMiOreXk+NpmQsYZByaYiJY9AFtSP3CZ1EN6Ms0/7OD8iPg64lJUJB/3bSnuODGBHhOSH1ku9ZD+s/fYdRKC9c1myXD7Bm43qi6pDAOTleRH6gJKQuHSn9nD8wfAVa+i/CppbuvgFqPqMjDBmSkBo94VIfbD9l4f/7QbJGNUaEXpEqjGEl35n5fmqOjX+SKv1cmByr2bizu6RxgdAa+RJaks+R7fFW+8/ARfjRYBRaJA6R+c4lv/TToOPsj3YGjG/kf9MKXGMs+vAHQyGm0hGj1kdMANB2vk7YAioxWzqckmmZziEfuKu6ZWKCtk1Y/ToVwgtkEDhlkkjG0/NqmsvGu58vA/BICaZoEJA+Lkr73HI+9SHoaQgRcdARxSmxrRpZp8dESIKuysYG2AMksbT46guTy0v20BYrSfU42BMuWrusoSrExmVH5/nYevQ+HjCIzG2M2jkPGITMZZTaBQ2E6wnyCeIapKJkcExHCCcYTQlYVlHQBT4qsyo7jDM5wVyeNPkJuGt3IMi1+ZAmfG9n8odnroJNIk9VYTJLMMB1jaytdTWv/XVkIkZ7T0HWcJmbeWhsh0tdE09A0ZIlwnMUksoQiEc8wE0PXC+2RfNLhdIz5FJK0Wk1P1fEpdARxOYqlUE4j5KEtgK6j6rgdtAVxKQCy2XeDqDJ9IclMhPk48QwLSaaj6DpD88SyABNRMjkc8helT18rXZeIxFGTa1WudXDgD+JRrpHe4GVDAE0zpAdwKug6LQH8bhSdrgaCHnxONoZwOmgP0eShyY/Tec2xa94mFXWn/3GQx15lOoVHJpElkQEdkqAuqSFw7bqi0kqtJ7m0tsSKNculO/Ul38eerz5J4AEHDoWgG4dMwI3HideFW+GrzSgSD97EDx8q78JLQdSdfu9WtgS5dIZYq1EXliAkLNWCipq7KujkVOajADNq8b3pViHLzY/WOkhAaJl+/DJf/w8mw9Cw9osthAQ5mOev7mPnj3EKuC0F1t3u6eKF79DUBBF7fE0oGMajPHwnL35biHFE9718/S5efpTmRlg0ilGLk4IIf3EHr36PzlpXz69SjyrjwfP83Q7O5CcquqyqXoMESDy2nX/9BhtEFol1qqdPLvDLD/nPHtQUuC2mXoM0pNjWyZN/w3e3Cz9hXRtHewf4l/3sH4QEuMFTWPjZNFRIgoangR/cy+N/SVfL2n9UPfVukaoqu07xwlH2XyIeBgd4jNpefe79/OVmIQkynRt55FZ+9CB3d9Xl7IBZ3QBAz0Xe6GPvBU6PQ6aw+G2hp7smCxotJV/7Vo3/s/gbeOgm/vorfPNuulpreq4SME16nqkFDg9xaIieIXonyKYBoxmpGO9BBWuQXFWc/0Eu/NsQ4MEu7t/KwzfxwJfwmJQZYLL0q8zHGZ2nb4yjw3x+hbEokTTRDGoGUsZCgfn67YrfSHJ1YCTf/e0CFx4XXgfNPm5v5c828edbub2DLU14zB60s4r0pagqs1EuzDAc5soig2HCqcIIgyIxlySWRjG86zpINHoJuACCHpq8bGukM8SWJjY1cms7IXMXG1iGFaWvSDZHIoMMUxHmkjiMVl0+/PYQjV4kCb8pS/OUiW2krycsO262nrkh3QRuSDeB/wMXHsKWsgphKQAAAABJRU5ErkJggg==)
