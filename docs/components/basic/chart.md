<!-- 源地址: https://iot.mi.com/vela/quickapp/zh/components/basic/chart.html -->

# # chart

## # 概述

图表组件，用于呈现线形图、柱状图界面。

## # 子组件

不支持

## # 属性

支持[通用属性](</vela/quickapp/zh/components/general/properties.html>)

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
type | `<string>` | line | 否 | 设置图表类型（不支持动态修改），可选项有：bar（柱状图） \ line（线形图）  
options | ChartOptions | - | 是 | 图表参数设置，柱状图和线形图必须设置参数。可以设置x轴、y轴的最小值、最大值、刻度数、是否显示、线条宽度、是否平滑等。（不支持动态修改）  
datasets | Array<ChartDataset> | - | 是 | 数据集合，柱状图和线形图必须设置，可以设置多条数据集及其背景色  
  
### # ChartOptions 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
xAxis | ChartAxis | line | 是 | x轴参数设置。可以设置x轴最小值、最大值、刻度数以及是否显示  
yAxis | ChartAxis | - | 是 | y轴参数设置。可以设置y轴最小值、最大值、刻度数以及是否显示  
series | ChartSeries | - | 否 | 数据序列参数设置。可以设置 1）线的样式，如线宽、是否平滑；2）设置线最前端位置白点的样式和大小（仅线形图支持）  
  
### # ChartDataset 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
strokeColor | `<color>` | #ff6384 | 否 | 线条颜色。（仅线形图支持）  
fillColor | `<color>` | #ff6384 | 否 | 填充颜色。线形图表示填充的渐变颜色  
data | Array<`<number`> | - | 是 | 设置绘制线或柱中的点集  
gradient | `<boolean>` | false | 否 | 设置是否显示填充渐变颜色。（仅线形图支持）  
  
### # ChartAxis 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
min | `<number>` | 0 | 否 | 轴的最小值。（不支持负数。仅线形图支持）  
max | `<number>` | dataset 数据个数-1 | 否 | 轴的最大值。（不支持负数。仅线形图支持）  
axisTick | `<number>` | 10 | 否 | 轴显示的刻度数量。（仅支持1~20，且具体显示的效果与如下计算值有关（图的宽度所占的像素/（max-min））。因轻量级智能穿戴为整型运行，在除不尽的情况下会有误差产生，具体的表现形式是x轴末尾可能会空出一段。在柱状图中，每组数据显示的柱子数量与刻度数量一致，且柱子显示在刻度处。）  
display | `<boolean>` | false | 否 | 是否显示轴  
color | `<color>` | #c0c0c0 | 否 | 轴颜色  
  
### # ChartSeries 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
lineStyle | ChartLineStyle | - | 否 | 线样式设置，如线宽、是否平滑  
loop | ChartLoop | - | 否 | 设置屏幕显示满时，是否需要重头开始绘制  
  
### # ChartLineStyle 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
width | `<length>` | 2px | 否 | 线宽设置  
  
### # ChartLoop 说明

名称 | 类型 | 默认值 | 必填 | 描述  
---|---|---|---|---  
margin | `<length>` | 1px | 否 | 擦除点的个数（最新绘制的点与最老的点之间的横向距离）。注意：轻量设备margin和topPoint/bottomPoint/headPoint同时使用时，有概率出现point正好位于擦除区域的情况，导致point不可见，因此不建议同时使用  
  
## # 样式

支持[通用样式](</vela/quickapp/zh/components/general/style.html>)

## # 事件

支持[通用事件](</vela/quickapp/zh/components/general/events.html>)

## # 示例代码

### # 线形图

``` <template> <chart type="line" options="{{lineOpts}}" datasets="{{lineData}}"></chart> </template> <script> export default { data: { lineData: [ { strokeColor: '#f07826', data: [763, 550, 551, 554, 731, 654, 525, 696, 595, 628], }, { strokeColor: '#cce5ff', fillColor: '#cce5ff', data: [535, 776, 615, 444, 694, 785, 677, 609, 562, 410], }, { strokeColor: '#ff88bb', data: [673, 500, 574, 483, 702, 583, 437, 506, 693, 657] }, ], lineOpts: { xAxis: { min: 0, max: 10, display: true, axisTick: 10 }, yAxis: { min: 400, max: 900, display: true, } } } } </script> ```

![](../../data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAACpCAIAAAC9GKYSAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAgAElEQVR4nO2deXgc5Z3nv3X3qW5JrVuyLtvyhTG2AYMNBmMgJOTiym4Sdshmk+wyYYZMZpIn+2Sz7GR22CRPMmRgybKZnWGeDHmeAAFCIBCwwXbMEWMZ35fu+5a61Xed+0e1ru6SVF3V3SqU+vwl1dH1dve33+N3vYSiKLCxsSrkSjfAxmYpbIHaWBpboDaWxhaojaWxBWpjaWyB2lgaW6A2lsYWqI2lsQVqY2myE+jhw4cPHz6cp6bY2GRi96A2loZe+vT8/nLv3r15boyNTTrLCNQWpc3KYg/xNpbGFqiNpbEFamNpbIHaWBpboDaWxhaojaWxBWpjaWyB2lgaW6A2lsYWqI2lsQVqY2lsgdpYGlugNpbGDrezsTR2uJ2NpbGHeBtLYwvUxtLYArWxNLZAbSyNLVAbS2ML1MbS2AK1sTS2QG0sjS1QG0tjC9TG0tgCtbE0tkBtLI0tUBtLs0w0k41+BqcxGoWkgCJQ7kZ10Uo3aFVgx4PmhsFpDEVSf0tK6m9bo+YpUDzoqu9dRqMaR1bf2yw8hRji/xR6FyljS97MIzYGKMQiSbN3WWWQRPoRKuOIjQEKIdBV37vIioZAy90r0ZRVR3ZDfGXby2U9B0Ovx8F5uD0POPY/pOcuikhX5CrrXQamIcrwsogJc++0yLGibVotZCnQjldSfyUjyYNPANCj0XL33Bx09siqIZTAaBRFHNaVpo7EBVwYQ08Qm8pArK6fYuExNcQnjz6t57JK74J/vezqWSHxErqDYEg0+ucOOhlUeJAQMRxZ/E4bfZibgyZ1fQMRHgC8LDaXAwAvmXqmpeiagiijsRg0teB4lRcchaEwEuIKtWy1YE6gnEfPVdMJAChywEHDyyIpYTpp6rEWYSiMCI9KD7xc+imSQL0fCtATXImWrSJMCZTb84Cey1Q5+jgAKHMDwNhH38wU4TEYhptBtVf7Ai+HUiciPMZjhW3Z6iI7gQ433ynRTvVvdreuVTwvIS6CIeFkAMDvAEMimPhoD/SijK4pUASaipdaBtX6QJPoD0H4KL/ZlSVLga771Jn9P2Wv+wIAsqROzy1q91k0MwgSBAJuABj/KHeiPUHwEur9YJe0gtAk6oogKeifLlTLVh1Ghnhm860AhHNv6rl4dgI6S5kLAMZjUD6a5vqxKIIJlLlQ7Fz+4hIXijhMxhFK5L9lqxEjvniq8RrC5Ze6jsnRKdJdvMSVipLegwJgKPgdCCYQTOj6jgtM4sDjyaNPIxnRdEbEBfSF4KBR69P7gmt8OD+G3hA2syDt+NssMRJuR5AUveEm4cRL4sVD7I7PLnF7VICkwM2AXvjFlLkRTGAsajmBJg48rjogAA1nhCyjcwoEgaZiDd/mYnA0qrwYmMZgOAtZ26gYDLdjNt8qnHhJOPfm0gLNHN9Vijg4aIR5JAQ4GP2tzTuZrofk0adnBdo3jYSIel9qwaefCjcmYxiJosQFl5Xer/UxOOTQ624A4xTb/qDwSxlR5huY0gi4AGDMaiaYTNfDzJHJOMZjKHakFnlZQRCo9wNAT/CjOvNeKQwKlGA4ev0eiLx4+ehi14gyogIoAm5W42zABZLARAyybKwJ+SHT9cA4ACRF9AbBUimdGcDNotyNmLAKQw3zivFJ+7Jr+czl0XwoEsVOSAom44abkHvY6+9PPyQJ4sDZrilICpqKQZlY5VR7wVIYDCNp+z91Y0KgG24GSQsX31YkQfOCxSags5Rbb5Snq1oAgKQBgHOD80CWes+cjAqo8WoPBfqhSKzxQVbQG8pBU/9EMJ7yQTiL6KZrxPZ3xc5jzLrdmRcsMQFVcbFwMYgJiPJmv/tcwR9/AYDrPzzJtOwFII20jb78k6mtX3QNf1hRshZYxK2pG58DxQ5MJTAZR4nFLBjWxJRdjt58KwBRa5SPCRBkOGkwVObJOSzlmpdDI+LlIw7fvcxrCn5wAI8dwiVy9OM/pWIT5a9+PfbMQ4qUg7G5zgeKQF8IoqUm31bFlECZTfsBCOcPZJ5adnxXKXGCIjAZt8S3xZ94iXN8nCNuSk0SkyL1XlfZ6b66+Hk6Ni62vxd/8Xvmn8JQqC2CKGPA9n/qwJRAyaJyqu5KJTwm9p5MO7Xs+J56BQKlLijAhAVmokLrrzluX9rByot9pVfcwN30VfWCxNtPmX9QwA0Pi/EYwubCDhMHHg89siP0nZbQIzsSBx433zALYtb1prmWl2REeJAEPDpmlhYZ5cXu4/JED0GkTwxJXgTguP2bzNaPA0i+8RP+1KvmH1fvBwH0BCEbNYumnF6qmTYZSR58IguNHu3AY4dS05ijHQZbUBDMCpTefBsA8dwb8w+GeSiAl9WVkeOg4eWQlFKzgpWCP/5rADKd3mJ5JmDJee8PqPrtAOLPfVvsbjX5OAeNSi+SEobDBl9B0+ml686jHXina3Yag3e6rKxRswKlAvVk+Vp5olcaaZs9qErNpzutccXtTQofE868DsY5sqkh7dTohlRUIUGzrvufJEvXQBJiv3hQGu8x+dBKDxw0hiOIa5vplmNxp9cyHO9b/ohlyEF0TeYoH1rSRJ+Jb6WjmIXTr4GPMVvvGG2pA6COugogUeTQpvrZy0h3seuBnxMuvxILxp7+ihydMvNQkkC9DwrQY8wsmun00peBo+EnsLDnIPcCTYjgJXAUON02VoJIzURXKoqZb/01AHbH3cUD4wAmmqta798/eGUTJclV5xb0lFSgwXX/k6AYeaIn9osHFZE381wPh4ALUR4nBtE6iJNDGNS9tFfDxuejMwNH+4t55SyCVvLpzZADgVI1mwl/tTx4Xp4agG4DUxoBFwhgbCWimKXxbqm7lSytpxt3lg2OAQjVlgEY2VTPu7iK8z1ps2O6YYfz3h8AkHpOxJ/7tsmnqzUs1DetFq7SqVFKzWigaAAgKQBU7VZdd+7MSIVwMjg3jJ+/izcuImKthMZlBHp4HgDq+6TdHwiZq7/5BtGQPgNTGmoUsygjWPClktD6AgBmx10QJUf/hEyS09WlAEiGiu5qJiQZR9LXEOyVn+BufRiAcPp3iTf+wczTM1PqdEaT8B88C8D91V/6Hr3k/dbb4NzxF7+rJHRMQ+uKAaQWsByN3Y34i734xGZ4OXzYj6feweF2JIzNi3MP9cgjjyxxumEeAPyvdZCpH7uMviCgYE0JAIJxCCdeVIQEvf2uvhAA1PuyLqpBk5iIQ5RR6jLyTgwTe+5bSEZd9/6QGEwQ54ZD1aXJDdVbK1HphbPGi/YxdE1gbQCeBb85uvFqOTgkD12Quo+T/iqqepOxpw9krOIVLJopOos0dDH55k/Jyhbn7d8AQDg8pMsvnHpFiQeZjemm3HTe7cJoGHdsxN3bsKtB/QZR7sVVtXCzGJpG1wRODkBRUFlkKjomF5h7/Mzqj266hnAXS10fTIemZQUeQ7kN3pkoZoOrWkMIl44o06P0+htIXwXaxgCE6soWLO/2rQeAty5n3uv87N9SzdcBiL/4PbH9XWMNyCxTped3rXaf7NX3zR5hr/kc1bSLP/as2PHeUneKEi6NgCLRUpHRFBLb6/C13di7FgCOdOCpd9DaB2klvXwmK4vMrf7oDfsAhEaHkY2BKY3ZfLqCIajLo513A0D7OIBgbWCBQNcUY20AfUFVvvMhKNr9xcfJ8rWQpei/PTTf0KafzDJVynKfgCIk+A9fBs2xV31q/nHX3X8HxhF/4bsKv/hyp30cvIS1gUXXsAyFXQ34z7uxqwFJEQcu4efv4uygrjeTB0xWFpl7k+pafhoeZGNgSqN0Joq5MD9aORYUzh8knD564y0YCCHGRwJFsotLD626eR0IAm+3ZQZXEw6v+0s/JzwBJCPRf/mKHE4X8bJUF6HKk+pHKQIOCgB6gkuFyQpnXkcizFzxMcK5oMYVWVLnuO0b8mT/UtPic0MAsLlqmWY5GOxdi6/txvZahJN49Tz+6T1cHi28C8qcQOetB+l1u0V/Pe+pZkg525SdWSgSJU5ICqYKYvEQTv4WksBs+yRBs2hPrd81HGAlblxVg6kYPhzIfBHSX+1+4CkwDiU0FH70RgOe8eoibKvCjmpsq8Km8tT6sntq0Uxl/tivALDXfC7zFLfnAWrNNv6dfxV7PtS4M86jcwIOBk2lGmcz8XC4dQO+cj02V2EiihdPF94FlZ1Au2tIcTZ8bm0Ae5pnTxE0m7z6SwA8MY1vUT+qQbQweRGqezM1vreNAQjWlWkbyPY0gaNxtFPTpk3VbKHVpYkiA9l7xudBEGgqgZeFAnRMakSTSKMdUs8JsqyJbtih+QrOex4FxcSf/46GjfbiKGQFGyuyW/r4nbhzM768SyOTNf8uqOwE2lNHvXM1gy9eDQCx9PcfbdgLwNV50EyDXAzcDOIioqZM4MsjDV6Qhy6QVRuo6k2YimEimvQ6E36P9vzEyeK6BiQEvNul+WripSNpR/R6xjMgCTSXwM1AAdonU7UBZ1mi+1Shypq4Wx6Sx7uSBzN+Ier4vqnSSLMCHo3Alvy7oAwN8TU+lHkwOI2xOauboiDqrIIsscf+2aR/pTCd6Kz3CJjpPmvLWAqOxRxgO9bA50Brr7bHxbBnXAuKxNpSOGnICtonEJsxaygiL5x4CRTDbP/MErdzN36ZrN6UPPL/pIFzc0eDMQyE4HOi1mjiX+a6Sr+30ChG56BbqwHg1NxoHhUgKYQz1EWFR8SO9820qdgJisBUPqOYFZEXTv4WFMNs+yQAdQIaTDMwpUGT2LsWkoLD7RpnDXvGF3/aulJwFCQFbROpOqPC2d8r8RCz5XbStZTICIp23fMoQMSe/85cxti5YQDYbKj7VMl0QWUeyTVGBbqlChSJs0MQU/EdqjvQS8YBiOd1lW1atE0EAq7lrS1mEC+8pcSC9MZ9pLsYcQH9QYmjI2X+ZewPGytRXYSLIxhIj+/I9IPr9YwvDkNhfQAsBVHG5XEkRfDHngXAXnPfsvdSVRu4vV+Rhy8lD/88dci8QPc0Y3djqtdUXVDzFiF5wqhAHQxaypEUcWlUPaB6OP3VdQCEcxpJIFmR7yjmBcujjnEoCNUEQBKZpWjTWcRu79j/EHfL1+d6TZef2/eg+XayFNaXgiEhyLg8KiRHu8lAA910rZ57uX0PkuVrk289KY20YSiEqRgqi1BibnuAPc14+CZ8ez8evqkA6oQpM9O2GgA4OQBAlBATQJPw+vxU/XYlOmkypJejUcSBl/JSFE6eHhHbjhLecnrdHiA1AZ2qLXNl1JDSoMaPlnIMhnBxJO2MY/9DvkdafY9eYrZ/BrGg8OHLOWktR2NdKWgSPJiBzzxNXvtFnTcSNOu851HIUvz57yhnVfOnie4TwEokmZgQaF0xSlzoD2IiqmYgqd1PVsUZl6Asb1HMfOtLUGR2x2cIkoIoo2tCIYnp6lK9/oWb1oEkcKhtMXeCY/9fgGISB/7R5GJxFieDtT6B5CNCSXPP2n+v34tB121ld/+Z1H8OZ3pAENhoSqCmkkyMYs5Qf2UNAJwamB/BlCuBqlHMoTxEMavuTUZdv/dMQpCi1SUyQ+sVqN+JHXUIJdCqbQUki2vYaz6nBAdVk1BOYNsPVP3my4SUjMt020QWnjbHbQ8zJTcSAqXUOE1WHzCeZGKC7MLt0tlSBZLA2aFwTMaMh5MsqSMrW5SpfmnoopmWzUYx53YmqibHUfU7qEADkFq/T9aUkYvUkNLm+kY4GLzbhbh2H8ntexCMM/nWk0sXV9MPf+xXzuGTjUI7AUQFdEzqzbYjGIej9vMAkpOvmWmANNKeW1OaTpYR6N55aJx2sVhfhrjg6RmbX6MhV52oWgFvOJJ1tPkSqLVD2J13pf5vT1lAvWwWJT/hYLC7MeXu04L0lHJ7/kyJTiaP/qvpJkOe7BPb3yNLaoubNjeVAECYR+ekvuBuXiQHJYWQkoMvJt/pZGnT/XHnv1W5LFPaJwzZ0rTg+lovytrAATaBuZHMOVKoPP7zqyizRdD4WPCmdfAOJkr7gCAoWlEeL7MK7i45dfvaWyvRbELJ/oxqd3Dczf+J8LpSx75JzlmdisaNbiO2XkfAL8DjcUAEEqiS09O1OUxiDJaKghfIPHaj+RgFnFJcng8/vLfhn/8MeHD35DlzbT6oc3DvCltWUwLtKGU9zqLhid9ibmxjKraQJbUysOX5ElTvtqcb5MsnHkdfIy54mME5wbm1u8wEIFFkrhpLRQFh7Ts9gDh8HJ7v4JkZM4SaQhFEvnjL4CkZnv9EifqfQAwldCRzHRuCACxtc5519+Bj8Vf+K6uh8anE7/cfhHt/DvPUN4y533/sD7jd+5P/YnCmN83C3fF3nZq1mMCtQScZYczUA9/kFP016Uw460Zxvk8wffx4Au/Oe1P/tYwAmaspmd8nJjvXlqPOjbQy92l0Ze/39hLecf/cX8nS6TUo/4sW3lcg4veFm0ls2ezDghpcFlk1miiTRMwk3i/oSZv0eZvtnxbZ3+NYXlnicwscTh56a/uG+5KH/S3Buxyf/m/ebr7MzntVZU5rvkdYCqBPmBRpOYnxttUIQxNnB+eGSzOb9MG2xz4w2N7NNsjTeI3W3kqVr6MadABCKYywieR3xYq/hANYl4u0BEIyD2/cgxGTyrSeNPmBR71EsI+9AY3i5MAwF2Fipzq+dd/5XwlsWf+Xv5enRzAcpIp9879/CP7ol+fufAOBu+yvv3xzkrv8iQa9k5UGzAg0lITo5viGAKK9GpKvQDTsJT6nU0yqHx5e4fWkyo83NbJO8wLqE1PgeqTc0vs9SWYRNlRgJpwKFMmCvvpcsqeM/eE6a6DXw8nJwULx8hPBVqeUg56NreFno3iScRc5P/3ckwvHf/I+0C/kTL4V/LHEy99XklFu71eLvvWW4+avEezKV4g0G42imujJq2rQNYZTA1hfPvfSG/cJHzwnXnhLj+9YE3VT5NFo6qP3caa2SeZPvARgdrRSBTpebU6gAPauxeVRHG7H+vLMYpMERXO3/mX8V3+dfPOnrn/346zb/MHzANir78k8RRHpiiQASZ4X6jkexUgYpS5Uzn1qzOZbmSvuEM68FvrelRAS4Dz0+hvkkcvyaAcoht31BW7fg6Q3kG0784epHnS2RgOzLoAiBzon5qeQ52Qtr0abtwQAmApuEi4dUaZH6PU3kL5KAEgI6AsqHB0s8zvp9L2Ks6PIgZ1rEE7iuHYfyW77JFnZIpx6JVvDsCJL/PHnQJDsznszz2omM50fmxfjvEh2B+GvBgAhAQDJiHjmNXm0g7nq095vvu789PcspU6YFGhofg2mK6oB4PRcAB7dfB04t9jxnq5k7SXxsHDSiArGEz7nkt9VOiegKIk1AZBktjUmNLiuAS4W73Ujql31wHHbNwBkm0EvqhmnLTeSvowMzIxkpioP6n0QZVyeQF8IsgKcHwY0wpM1/Fusy3XfD8ni2qyaVxhMCXTBNglbq0EApwdnXRwEzTIteyEJwiUtL1SWBEwkfMqxoHD+AOH0qQUmgFkDUwAmx3cVlsaeJggSnjyqmVDGbLyZqt8uXjyUVQzNssHz85OZqosQcGNTGTwsRqPoOTOF6QRq/fBlzCMz3T85cnflA+MClRWEkyBmYkRQ5EBTAOEkuiZmr1miRni2lLhAABMxIwU1hZOvQBKYbXemFqSSjM5xhSRGywMEdBUxXR61YozaOK2EMsft3wSQ+L3eaagcGhEvHSaKyumM5dEScDRaAqgtgrd9GECwuVLD25Tr2Oq8YlygkSQUwMvN8xBeWQ2kAvBUmJa9oBjh0mHjcT0zea70Px5qPNdhLOEz3fzZOwVeEmuLJZZe0H4zZAaOLEwooxt30utvkLpbhYzsJU34489Dkdmd9xBk1hPkCqdc2juikER3RcXF8fR5UT5iq/OHcYFq1FhsLoOHRcfcRJ3g3PTa68HHDBbeWFhqtfhEV9WpjmxHeWnoojx0gaxsmatOoxqY1phev89HR03DrDrR9B9VVnSME0kRzYHyABMTcGEMI/NG9QWx1YVyCBnGuEA19ukiCWyphoL5hShMreUzslorLvRF+OwqW2l80+1jAMaqcipQHQllVPVG5oo75KGL/OnfLf1iwqUjSnCQXn8DWVxjpDGqe3NzVbUXGwLgaPRP49L43E+m8A4hwxgUKC8hIULDQzgTITp7gN50CwhSPH9QkbOP68zohChBRDZLpfTkOAAj0wgnlXJv2OEw6OHURF9CGXfbwyCp5BuPLb2jTWbppSxICOgYB0ejOQDAzWJjGcrdiPA4P7byewFki5HtuJFmYJqP34mGEnRPomsCjaUASHcJVb9d6j4u9ZygG6/OsnVkmvFTYWkCmIijukjX3DGVHLfl9rl97dvGAcQbAphd3uUENUHneF/qR1Xu0UzZoQINzPa7hOPPCSdeWEx/cnhMvPAW4QnQy9ap0+TiKCQFW8pn81dIAnU++B3oDqI3hGACDhoTMUgKKALlblPuj3xjcDvupfbhvLIG3ZM4NaAKFACz+Vap+7hw7s3sBNo5kWmaJ3bU+h2YSiCY0LVT24LkdxUzEUxLs6cZe5ohyfg/72A8inACXg0Tq2P/Q8LJ3yQOPM5s+zTBaLSAb30BssTuuIugDPn5FrHPezlsKkP/NMZjqa8PM1EmgHU1amSIV5TUKkj7C15XBheDtrHZ2iBGpqGDIbx0CgA8LFgKQMqFJ8gBfcXCEwceDz2yXbx0BCDEvpltnKYTGA3Dy417ixZtv0koEjvXQFYWcyyRvgp21xeU6VH+/Wc0LxA+0JtbrMF0Av1BFDlSVWozmlbv1xh5rLwBsxGBRnlICjzsIhV+KBJbqiErs0slsrgGnoASHNSbDTgZxfMnIcgodiWaz4ZCfx0K/nko8jeSL4zjvUX94yyFML9U2ZWZ9C71g1f4t55MPbR9DIDQVCbq2KbRONtqwNE4ObDYao676Wtg3clDTykZNnOx/V15sp9qvo4sMVQTQUdxm0xDsskgxrxiZBBZfhOPK2twrAenBnBtA4DEgccRmYlpSkaSB58AsOjiMZzErz5EXICHTdScSh7+6eyN0d7ve0u+j5dPBW6rHSxuGW47Vzn6jpKIKMmIkogoyaiSiCAZUZIROWOPmOTRpx37H8qLgSkTjsZVtXi/GycHsKsh8zzpLuZu+FLy4BPJP/xL2uegvzSDNjqqM2RGmZgJYsw3RgS69EbwAFDiQp0ffUH0TmFNsUY24MEnVJlm4PB4/4qiahQlHhn8n3L/giBoRYlGQz/zeB4OvHxk8P7mKbrc9/vHCEWfcSAZQVJE7xRYajxQDDGfAgWwsw4f9OCDXuxco5lsz93wH/n3n0n+4Z/ZXV8gPSXqQTk6KZw/QLiK51yyWTEyjYkoyr0ILOUZKnen5p3zj1iW7AVKMWqNhmVyIK+sQV8Qpwawplh37h/t9vwXiqpRFCEa+Zksa2TPSGIb7zjNJrau+eB477W7+Dv/vig5THAewuEhODfh8IDzEJwn8r/vnhnfZ+A86JyArCiNpWGRJJBWcj7XuDlsqcKpQZwdSlW4WAjBubmbvpZ49X8lDz3lvPM76kGh9UVIArPjswZjhPUVt0kLYnQz1l0hIVuBsiX1THEdAEnG4PSSb6ylAgcu4dII9reA86RrlPP4HskIm3jhlDoEE3ft8Kz/HYDQIzsyb2QfehjPtAbapieagqGWz5RrlWLl9nwprYfm9jygTkDjjeXqNo258XAuwTUNODWIY92aAgXA7vpC8ujT/PvPcHseIP1VMGn+xKLhS5lUF6G6CJKM0yNIiAujSC1Gdu1iSxtU17CC5XIsaRKbqyApODeky/n7+oVUEfjbN8xGPWvfSJL41BaCpZr+cDYaFnitpZKGN2/fn6NjHAQxVV2KvE5AZylxYX0ZpuKz5avSIGjWccvXIQmJg08AEDuPyePdVOPVVFmjkcd1TSDKo6FE/9BAkSh1QVIssdX0Ypj64Sxjnpgp3rS88/cPHSnn054mbJuLSlz0Rp8Td2xko4n69y4s5lVK9+b1BZEUUecPKQyy32fMIOoK6f3uxc4zO+4iA41C6wvSWKfZ7tNQ8boKNwCMWNjMZCrlYxnzRMCDah8GQxgIOvY/tOiy/cP+VNnibTXY3ZR2ctEbWyqkrZPFpweiJ/uVG2qX35OpbQyA1FwWF0GTcOXKw7k0Vb75i8XM8wRJOW77y9gvH448didkCYA01mnkQYKEy6OgyfkpN3rgaPgcCCUQjMO/8glIGpjqQZc3T8yrgKfNpRG8cREA1pfj9o3ZPX3/+qTfXX3scmRQxyKsbQxAON8GpkyubQCAP3Yvdl4aaQeAmUAF/u2fGanI1TYGQcK6MrBZ9zgW70RNCXR588SGCnA0Lo5oW9V7p/DbswBQ58cnt2T9eIZKfuIKAOyrZyAsaWwai2A6gTJPkHMity74ZWkOoMyDzon55dLnk5uKXDo3l9HCy8HFIMJn7jlgCbITKD/RrYbhqEkwy5snGAqbKiHKqQXmfEbD+PVJSArKPLh7m47KnBp4azyDV6/npqLSQe3M9BRtowCwtmx5C24+uLYeWHwmar4iV4xH1yScDBpLsm4bgJmOxpqdaJYCneyJdr4zmwSjCzUA72T/goPBOJ79ELwEnwP3XWW4Fj9BgLiqdmpNOXVqAJcWr97RNg4g0RgQZDjolG+/cGysQJEDF0bSdk1OYT4B48IwFAUbK43sPwkAKHGCITEVX2YcWhHMlV/UQ4UXlV6MRjA0Y5SK8Xj2BKI8nAzu227SYh5woee6jbzbgdcuaCsgnMTwNDxsqNiHwnefAEgSV6+BouBYugMWOUnAMF18Xq10qVgyasRguF12XFmD4Ys4NYCqIvAinvsQU3EwFO69CiVmdzbmaLi8TOeeLS1vHCdePoPP70w3wbePASs3vqtsrcE7nTg9gN1NaTHSqo0iefRpJCPgPC1uPzwAAAWhSURBVNyeB7IIcT/agWO9ECQQQOc4qn2GG1jmxlAYY1FUefPvwsiGvO9zAwCbKvHmJZwawKkBEAQUBSSBz25FVW5cbGUudJb7p7Y3lbR24mgnblwYKdw+BkBeWxbhQSBVc6vQsBS21+HdLpzoy8KUtjRqwpaKgtTfRjc2oEmUujAew0QsVTfYIhTEw3WsZy7GS02DXRuYDWc2j98BmkT3pia5rhjvdaFncu4cL6JnEgwVrSyRFbgN7ROeG3bUgSbR2peziV7mNoTmNiasKOAmlPopyNeV+cH16Cm9qheCQKkTCjB+yxY4Gbxyds5k0jUBSUFj6bREYqXGdxUXiyuqERdwJkdbW+vII80KB4MiDgkxLzurGKYgAs31R5mJGmY/Cg6f2IwIj9+dT51oGweAdYGVnIDOcs0aEMCxXiPFJzLJdJOY3pjQgp1oQQSa/z0eHTQ8LJISwrUB7KhDxziO90JW0DEOAmJjICaAymqbhHzgd6GlAqH4UhYxnRzt0HA0m96YsMgBB43ppPEaWDmnIAItyB6Pc8Wbbl6Hci8OXsY/vK0mXQjH+rDi3aeKarT/o4a9KQtml0d1/pxvTGi1TrQgq/j5KbkcjZ11+dhFr9iJvhCm4qjzkXStD6PhVFKoAuexrqoE2BsLsXXfMlQWob4EPZPonkCDoWXirDp3N2FPukHAPCUuDIQxEUO1N285W9lQEIFiJiU3n5AESl0YjWIihopz6Z7Vigt90q0WECiAa+vRM4k/9hgRaJ7VCYAkUObCUATjMVR58/GELNuz0g3IJXOjvFZJkuwDffJDYykqvOiexHCWe+rkX50qZW4QwGg0N2s5k6wqgToZuBkkRCgZYpStIk8AwDX1ADQ9n4tSKHUCYCiUOCHKRgoJ5pxVJVDM2JtCW9IXYfxVuV+WGWdDBXxOXBxBUF+yRQHVqVLuAbCgJt5KsdoEWuIERaBzc7N8faO6wpUYenBrI2OFFdIsJIFr1kABjunY+qPg6gTgYuBlERfnVbxfIaw08OUCkkCJE2MxTGxvLruhOZzE5Ql4WFRb7Zd4RTWOduLMIPY0wbW4eXYl1KlS7kF4EiORwsZ3Z2C17y0HBObtkbxUDamVhaGwow6ivNie3sBKqhOA3wGOQiiJRI69ftlhsPyilXExcDGICYjyOoqgrCDb6/DHbpzow7UNGkHUK6pOlXIP+kIYjWCNf0WeDxQoHrTgBFzoDWE0iqgAiihUDme2OBlsrUFrH04PYOeaBacsoE4ApU4MTqeqsRpKyckBq3CIB1KlQyfjgFoCM7yyzVmca+pBEPigd/42pxZRJwCKRMANWVm+2GX+WJ0CTbOPmN9oPl8UObCxAtMJXJgJH7GMOlXKZ1zzGtvZFITVtopX0dxo3qIlsnY14PwwXj2HV87NVUa0hjoBsBSKHZhKYEpfSeucszp70JxvNJ9H1NC72X3fAdT5LaJOlYoVNdqvToHmdqP5/JKZbjBqAQfOPNws3AxiAiIrUdlhdQo0txvN55f8pxuYZwU70dUp0MydgC06AUUh0g3M43eApRBMrMBvx3KfRa5Qa7R+BNhZN5c9PHvEYhAEyt3on8ZoFHXGk++NsDp70I8Se5qxuzHnmRs5J+ACSWA8Bil976r8smp70I8S+U83MA9FIuDCaBTjsdSUtDDYArXRS7kbo1H0T6N/unB7KNpDvI1e5peyV/dQLIB/zhaojV40/XP5xhaojV5WxD+3CuNBbfLEiuyhSCjZhKkYL2Nr89GHLalnSxvmH+EnuvlJI1VS9Hd29ireRi+qFhl/LUHRiiQKwX5j6swOJXsOHTpk4C779j/x2429gr1IsrE0tkBtLI0tUBtLk90q3samwNg9qI2lsQVqY2lsgdpYGlugNpbGFqiNpbEFamNpbIHaWBpboDaWxhaojaX5/7hcyVIn2bvhAAAAAElFTkSuQmCC)

### # 柱状图

``` <template> <chart type="bar" options="{{barOpts}}" datasets="{{barData}}"></chart> </template> <script> export default { data: { barData: [ { fillColor: '#f07826', data: [763, 550, 551, 554, 731, 654, 525] }, { fillColor: '#cce5ff', data: [535, 776, 615, 444, 694, 785, 677] } ], barOpts: { xAxis: { min: 0, max: 7, display: false, axisTick: 7 }, yAxis: { min: 0, max: 800, display: false, } } } } </script> ```

![](../../data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANYAAACuCAIAAADF8GTVAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADSUlEQVR4nO3bMWocZxiA4VFiGwwhcW2T0lUa30BVupwoB/Bd3LsIpJoTuDI+gMGQxshuFBTEpggkzrIRWbEz78zO85SjZfhB7/47+vXtxW63G6DzVb0Atk6CxCRITILEJEhMgsQkSEyCxCRITILEJEhsP8FxHMdxTJbCNtkFiUmQ2IN6AUzr6np4/3m4uf3nyqOvh++/HZ487tb0b3bBM7fX3zAMN7fD+8/Rag5ZxC64/Hfqeu31d8fFyiJ2weW/U5nO/i743W9vnr179emXj39fuXjy9PFPPz/84cfpFrH8dyrT2d8Fn7179ej3j19e2V19uH79csYlsS37Ce7195fd1YdZFsMWLeJZkC2TIDEJElvEueBG/PH21+vXL798sJ7htGH57ILz2etvcNowDIME53TwYMFpgwSJSZCYBIlJkJhDmaXY7MSaXXApNjuxJsGl2OzEmg9i7uOEjw12Qe7jhI8NEuQ+TvjYIEFingVXb+0DOHbB1Vv7AI4EV2/tAzgSJCZBYhIkJkFi53wos9nZk3U5511ws7Mn63LOCW529mRdzjlBVkGCxCRITILEJEhMgsQkSEyCxM75H3T3tvY55HWZKcGJfqkT3fa/5pAlOIWZPognGi6f6LZrn0Nel5kSnOiXqpUzcNwHsfEnTu64XdD4Eyd33C5o/Gk7ZjsWcC7IYbN9PVmCHDbbn3oSJCZBYhIkJkFiEiQmQWISJCZBYhIkJkFiEiTmuyNHMzR5WnbBoxmaPC0JHs3Q5GlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiUmQmASJSZCYBIlJkJgEiT34n68bx3EYhm+eX97x0zu8cNtt3/by8vDrB7sguYvdblevgU2zCxKTIDEJEpMgMQkSkyAxCRKTIDEJEpMgMQkS+xO8s1S2aJOZ4AAAAABJRU5ErkJggg==)

← [ marquee ](</vela/quickapp/zh/components/basic/marquee.html>) [ qrcode ](</vela/quickapp/zh/components/basic/qrcode.html>) → 

快速导航

概述

子组件

属性

ChartOptions 说明

ChartDataset 说明

ChartAxis 说明

ChartSeries 说明

ChartLineStyle 说明

ChartLoop 说明

样式

事件

示例代码

线形图

柱状图
