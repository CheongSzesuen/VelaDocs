<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/other/launch-mode.html -->

# Page Launch Mode

Used to define the launch behavior of a page.

## Static Declaration

In the manifest file, the launch mode field launchMode can be added to the page route information router.page to declare the launch mode of the page.

### Page Launch Mode Parameters:

Property | Type | Default Value | Required | Description  
---|:---:|---|:---:|---  
launchMode | String | standard | No | Declares the launch mode of the page. Supports two page launch modes: "singleTask" and "standard".   
When identified as the "singleTask" mode, each time the target page is opened, the existing target page will be opened and the onRefresh lifecycle function will be called back. Other pages opened on this page will be cleared. If this page has not been opened before, a new target page instance will be created.   
When identified as the "standard" mode, a new target page will be opened each time (multiple identical pages will exist when the target page address is opened multiple times).  
  
### Example:
``` "router": { "entry": "PageA", "pages": { "PageA": { "launchMode": "singleTask", "component": "index" }, "PageB": { "launchMode": "standard", "component": "index" }, "PageC": { "launchMode": "singleTask", "component": "index" } } }
```

Behavior logic for opening pages:

If the pages are launched in the order of PageA -> PageB -> PageC -> PageB -> PageC -> PageA:

  * Open PageA. When it is opened for the first time, the page stack is empty. The page stack is PageA.
  * Open PageB. The launch mode of PageB is standard. A new PageB page instance is created on top of PageA and displayed. The page stack is PageA, PageB.
  * Open PageC. When it is opened for the first time, a new PageC page instance is created on top of PageB and displayed. The page stack is PageA, PageB, PageC.
  * Open PageB. The launch mode of PageB is standard. A new PageB page instance is created on top of PageC and displayed. The page stack is PageA, PageB, PageC, PageB.
  * Open PageC. The PageC page instance already exists. The page instances on top of PageC (PageB) are destroyed. The previously opened PageC page instance is returned to, and the onRefresh function of the page lifecycle is called back. The page stack is PageA, PageB, PageC.
  * Open PageA. The PageA page instance already exists. The page instances on top of PageA (PageB and PageC) are destroyed. The previously opened PageA page instance is returned to, and the onRefresh function of the page lifecycle is called back. The page stack is PageA.

## Dynamic Declaration

There are two ways to dynamically declare. One is to carry the launch flag parameter in router.push, and the other is to carry the launch flag parameter in the link to open the page. The launch flag parameter can control the page opening behavior.

### Page Launch Mode Parameters:

Parameter | Type | Required | Description  
---|:---:|---|---  
___PARAM_LAUNCH_FLAG___ | String | No | The page parameter passed when jumping to a JS application page. When carrying clearTask, opening the target page will clear other pages outside this page. When there are multiple target pages, only the earliest opened target page will be retained, and the onRefresh lifecycle will be called back. If the target page does not exist, all pages will be cleared, and a new target page instance will be created.  
  
### Example:
``` router.push({ uri: '/PageB', params: { ___PARAM_LAUNCH_FLAG___: 'clearTask' } })
```

Behavior logic for opening pages:

If the page stack that has already been opened is PageA -> PageB -> PageC, and PageB is launched with the clearTask flag at this time:

  * The PageC page instance is destroyed.
  * The PageA page instance is destroyed.
  * The PageB page instance already exists. Return to this page instance and call back the onRefresh function of the page lifecycle.

If the page stack that has already been opened is PageA -> PageC, and PageB is launched with the clearTask flag at this time:

  * The PageC page instance is destroyed.
  * The PageA page instance is destroyed.
  * The PageB page instance does not exist. Create and display a new PageB page instance.

