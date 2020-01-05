# python_期末项目说明文档
## 使用python搭建flask网站：
### 交互功能：  
点击页面按钮跳转至对应的图表页面  
### 部署至pythonanywhere
http://biubiubiu.pythonanywhere.com/  
### 一共2个页面
- 页面一：entry.html: 该页面是首页，用到的页面请求方法是GET，主要的页面功能是：点击页面上的按钮能够跳转回到对应的图表页面  
- 页面二：Unemployment.html：该页面是二级页面，通过点击entry.html页面的按钮，使用POST方法，跳转到该页面。此页面主要的功能是接受到用户的post指令之后，返回对应的数据和图表内容。

## github文档：（templates、static、app.py、数据文档）
- [templates](https://github.com/Tina0426/python/tree/master/webapp/templates)  
- [static](https://github.com/Tina0426/python/tree/master/webapp/static)  
- [app](https://github.com/Tina0426/python/blob/master/webapp/app.py)  
- [数据文档](https://github.com/Tina0426/python/tree/master/webapp)  
## 技术文档书写
- entry.html、Unemployment.html、base.html文档放置于templates文件夹中。  
- entry.html、Unemployment.html的CSS样式继承于base.html  
- 首先安装flask、pyecharts、cufflinks、plotly等模块  
- 通过import调用上述模块
- 使用pandas模块读取数据文件

### HTML档描述
- 调用def entry(): 可跳转至 entry.html  
- 调用Unemployment()： 可跳转至 Unemployment.html，展示图表“世界女性失业率（地图）”  
- 调用def Unemployment() 可跳转至 Unemployment.html，展示图表“15-19岁女性生育率（地图）”  
- 调用def Drop_out_of_school(): 可跳转至 Unemployment.html，展示图表“世界儿童失学儿童数量（折线图）”  
- 调用def Umemployment_rate(): 可跳转至 Unemployment.html，展示图表“世界女性失业率（折线图）”  
- 调用Enrolment_rate(): 可跳转至 Unemployment.html，展示图表“女性高等教育入学率与中学入学率”  
- 调用Maternity_leave(): 可跳转至 Unemployment.html，展示图表“世界女性产假周数与报酬情况”    



### 数据传递描述：
- “/”：用户通过输入url点击搜索 → 页面的请求方式为“GET” → 返回页面1  
- “/data”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → data_str = df.to_html() 将dataframe呈现为HTML表格 → the_res = data_str → 在名为“Unemployment.html”的文档中，有{{the_res}}jinjia可传递python文档中data_str数据的语法 → 为用户返回含有df的表格数据的“/data”  

- “/世界女性失业率（地图）”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → 调用app.py文档里面Unemployment()函数和timeline_map()函数，timeline_map()为制作图表的函数，the_plot_all = timeline_map()  → 在名为“Unemployment.html”的文档中，有{{the_plot_all}}jinjia可传递python文档中timeline_map()数据的语法 → 返回含有地图的“/data”

- “/女性高等教育入学率与中学入学率” ：用户点击“/”页面的按钮 → 页面请求方式为“POST” → 调用app.py文档里面Enrolment_rate()函数，Enrolment_rate()为制作图表的函数，the_plot_all = plot_all  → 在名为“Unemployment.html”的文档中，有{{the_plot_all}}jinjia可传递python文档中plot_all数据的语法 → 返回含有地图的“/女性高等教育入学率与中学入学率”

- 数据故事的传递：在python文档中，为数据故事设置一个参数“story”=‘数字故事的内容’，同时在跳转的页面“Unemployment.html”中设置{{story}}，在执行“POST”的请求方式时，story的内容可返回到请求的页面上。

- “/世界女性产假周数与报酬情况”：用户点击“/”页面的按钮 → 页面请求方式为“post” →调用app.py文档中Maternity_leave()函数，Maternity_leave():产生所需图表，并用以“maternity.html”文件打开 → the_plot_all = plot_all  → 在名为“Unemployment.html”的文档中，有{{the_plot_all}}jinjia可传递python文档中plot_all数据的语法 → 返回含有图表的的“/世界女性产假周数与报酬情况”

