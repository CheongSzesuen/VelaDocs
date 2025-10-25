<!-- 源地址: https://iot.mi.com/vela/quickapp/en/guide/framework/script/page-data.html -->

# Page Data Object

Property | Type | Description  
---|:---:|---  
data | Object | Component-level data model. Property names must not start with $ or _. Do not use reserved words such as for, if, show, tid.  
public | Object | Page-level component data model. It affects the override mechanism of incoming data: Properties defined within public can be overridden by incoming data. If an external incoming data property is not declared in public, it will not be added.  
protected | Object | Page-level component data model. It affects the override mechanism of incoming data: Properties defined within protected can be overridden by data passed from internal page requests within the application, but not by data passed from external requests.  
private | Object | Page-level component data model. It affects the override mechanism of incoming data: Properties defined within private cannot be overridden.  
computed | Object | Computed properties. Property names must not start with $ or _. Do not use reserved words such as for, if, show, tid.  
  
Helpful Tip

**Note that public, protected, and private cannot be used simultaneously with data.**
