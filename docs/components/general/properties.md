<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/general/properties.html -->

# # 通用属性

通用属性，即所有组件都支持的属性。

开发者可以在所有的组件标签上都使用`通用属性`。

## # 示例代码

``` <template> <div> <text id="text1" class="text-normal">line 1</text> <text id="text2" class="text-normal red">line 2</text> </div> </template> ```

## # 常规属性

名称 | 类型 | 默认值 | 描述  
---|---|---|---  
id | `<string>` | - | 唯一标识  
style | `<string>` | - | 样式声明  
class | `<string>` | - | 引用样式表  
  
## # 渲染属性

名称 | 类型 | 默认值 | 描述  
---|---|---|---  
for | `<array>` | - | 根据数据列表，循环展开当前标签  
if | `<boolean>` | - | 根据数据 boolean 值，添加或移除当前标签  
show | `<boolean>` | - | 根据数据 boolean 值，显示或隐藏当前标签，相当于控制{ display: flex | none }  
  
渲染属性工作方式详见[template 模板](</vela/quickapp/zh/guide/framework/template/>)。

注意

属性和样式不能混用，不能在属性字段中进行样式设置。

## # data 属性

给组件绑定 data 属性，然后运行时通过 `dataset` 获取，方便进一步判断。

**示例：**

``` <template> <div> <div id="elNode1" data-person-name="Jack"></div> </div> </template> <script> export default { onReady () { const el = this.$element('elNode1') const elData = el.dataset.personName console.info(`输出data属性： ${elData}`) } } </script> ```
