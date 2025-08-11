<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/guide/framework/script/page-data.html -->

# # 页面数据对象

属性 | 类型 | 描述  
---|---|---  
data | Object | 组件级的数据模型，属性名不能以$或_开头，不要使用 for, if, show, tid 等保留字  
public | Object | 页面级组件的数据模型，影响传入数据的覆盖机制：public 内定义的属性允许被传入的数据覆盖，如果外部传入数据的某个属性未被声明，在 public 中不会新增这个属性  
protected | Object | 页面级组件的数据模型，影响传入数据的覆盖机制：protected 内定义的属性，允许被应用内部页面请求传递的数据覆盖，不允许被应用外部请求传递的数据覆盖  
private | Object | 页面级组件的数据模型，影响传入数据的覆盖机制：private 内定义的属性不允许被覆盖  
computed | Object | 计算属性，属性名不能以$或_开头, 不要使用 for, if, show, tid 等保留字  
  
温馨提示

**注意 public，protected，private 不能与 data 同时使用。**
