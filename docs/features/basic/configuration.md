<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/features/basic/configuration.html -->

# # 应用配置 configuration

## # 接口声明

无需声明

## # 导入模块

``` import configuration from '@system.configuration' // 或 const configuration = require('@system.configuration') ```

## # 接口定义

### # configuration.getLocale()

获取应用当前的语言环境。默认使用系统的语言环境，会因为设置或系统语言环境改变而发生变化

#### # 参数：

无

#### # 返回值：

参数名 | 类型 | 说明  
---|---|---  
language | String | 语言  
countryOrRegion | String | 国家或地区  
  
#### # 示例：

``` const locale = configuration.getLocale() console.log(locale.language) ```
