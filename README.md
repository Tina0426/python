# python_期末项目说明文档
### 交互功能：  
点击页面按钮跳转至对应的图表页面  
### pythonanywhere部署可用
http://biubiubiu.pythonanywhere.com/  
### 一共2个页面
- 页面一：entry.html 
- 页面二：Unemployment.html
### 数据传递描述：
- “/”：用户通过输入url点击搜索 → 页面的请求方式为“GET” → 返回页面1  
- “/data”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → data_str = df.to_html() 将dataframe呈现为HTML表格 → the_res = data_str → 在名为“Unemployment.html”的文档中，有{{the_res}}jinjia可传递python文档中data_str数据的语法 → 为用户返回含有df的表格数据的“/data”  

- “/世界女性失业率（地图）”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → 调用python文档里面Unemployment()函数和timeline_map()函数，timeline_map()为制作图表的函数，the_plot_all = timeline_map()  → 在名为“Unemployment.html”的文档中，有{{the_plot_all}}jinjia可传递python文档中timeline_map()数据的语法 → 返回含有地图的“/data”

- “/女性高等教育入学率与中学入学率” ：用户点击“/”页面的按钮 → 页面请求方式为“POST” → 调用python文档里面Enrolment_rate()函数，Enrolment_rate()为制作图表的函数，the_plot_all = plot_all  → 在名为“Unemployment.html”的文档中，有{{the_plot_all}}jinjia可传递python文档中plot_all数据的语法 → 返回含有地图的“/世界女性产假周数与报酬情况”

- 数据故事的传递：在python文档中，为数据故事设置一个参数“story”=‘数字故事的内容’，同时在跳转的页面“Unemployment.html”中设置{{story}}，在执行“POST”的请求方式时，story的内容可返回到请求的页面上。
