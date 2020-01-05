# python_期末项目说明文档
### 交互功能：  
点击页面按钮跳转至对应的图表页面  
### pythonanywhere部署可用
http://biubiubiu.pythonanywhere.com/  
### 一共8个页面
- http://biubiubiu.pythonanywhere.com/世界儿童失学儿童数量（折线图）  
- http://biubiubiu.pythonanywhere.com/15-19岁女性生育率（地图）  
- http://biubiubiu.pythonanywhere.com/女性高等教育入学率与中学入学率  
- http://biubiubiu.pythonanywhere.com/世界女性失业率（地图）  
- http://biubiubiu.pythonanywhere.com/世界女性失业率（折线图）  
- http://biubiubiu.pythonanywhere.com/世界女性产假周数与报酬情况  
- http://biubiubiu.pythonanywhere.com/data  
- http://biubiubiu.pythonanywhere.com
### 数据传递描述：
- “/”：“http://biubiubiu.pythonanywhere.com” 用户通过输入url点击搜索 → 页面的请求方式为“GET” → 返回页面1  
- “/data”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → data_str = df.to_html() 将dataframe呈现为HTML表格 → the_res = data_str → 在名为“Unemployment.html”的文档中，有{{the_res}}jinjia可传递python文档中data_str数据的语法 → 为用户返回含有df的表格数据的“/data”  

- “/世界女性失业率（地图）”：用户点击“/”页面的按钮 → 页面请求方式为“POST” → 调用里面的

