from flask import Flask, render_template, request
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Bar, Page, Pie, Timeline
import csv
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

cf.set_config_file(offline=True, theme="ggplot")
app = Flask(__name__)
df = pd.read_csv("API_SL.UEM.TOTL.FE.ZS_DS2_en_csv_v2_620050.csv", encoding='utf-8')
失业_国家 = df.CountryName
世界失学儿童数量 = pd.read_csv('Number of out of school children.csv', encoding='utf-8',index_col = 'IndicatorName')
青春生育率 = pd.read_csv('API_SP.ADO.TFRT_DS2_en_csv_v2_615863.csv', encoding='utf-8')
入学率 = pd.read_csv('Middle school and higher education.csv', encoding='utf-8',index_col = 'Name')
maternity_leave = pd.read_csv('maternity leave.csv', encoding='utf-8',index_col='国家')
世界女性失业率 = df.loc[257]
regions_available_loaded = ['失学儿童数据','入学率数据','青春生育率数据','产假数据','失业率数据']


@app.route('/',methods=['GET'])
def entry():
	return render_template('entry.html',
							content_2 = '''随着社会的发展，
	越来越多的女性开始走向独立，
	女性的权益得到更多的保障，
	男女平权问题也一直是我们讨论的焦点。
	我通过收集女性受教育情况、青春生育情况、失业比率、产假长度及其假期等数据，
	分析近年来女性的权益是否逐渐得到了保障，
	她们的生存状况是否得到了好转。看图请点击按钮''',
							title = '主题：女性权益是否是否得到了更好的保障',
							content = '''数据来源：
世界女性失业率;
世界5岁以下男童失学人数;
世界5岁以下女童失学人数;
世界15-19岁女性生育率;
世界女性高等教育入学率（占总入学人口）;
世界女性中学入学率（占总入学人口）;
世界各国女性产假周数与产假期间工资情况;
''')
	
@app.route('/data',methods=['post'])
def data() -> 'html':
	
	data_str = df.to_html()
	return render_template('Unemployment.html',
							the_res = data_str,)

							
							

@app.route('/世界女性失业率（地图）',methods=['POST'])
def Unemployment():
    return render_template('Unemployment.html',
							the_plot_all = timeline_map(),
							story = '''与青春生育率的地图相似，
							女性失业率的地图在经济发展不那么的地区呈现橙红，
							说明这些地区的女性失业率比其他的地要高。
							甚至在2010到2019年间，这些颜色偏红的地区，颜色更加偏红了，
							说明这些地区女性的就业情况在今年来并没有得到好转。''',
							)
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2010,2020):
        map0 = (
            Map()
            .add(
                "世界女性失业率", list(zip(list(失业_国家),list(df["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="世界女性失业率".format(i),
                                         subtitle_textstyle_opts=opts.TextStyleOpts(color="red",font_size=10,font_style="italic")),
                
                visualmap_opts=opts.VisualMapOpts(series_index=0,max_=30),
            
            )
        )
        tl.add(map0, "{}".format(i))
    return tl.render_embed()

@app.route('/15-19岁女性生育率（地图）',methods=['POST'])
def Birth():
    return render_template('Unemployment.html',
							the_plot_all = Birth_map(),
							story = '''以下是世界范围内，
							每千名15-19岁女性生育数图，
							可以看出在经济不发达地区如非洲和南美洲女性的青春生育率相比其他地区的女性青春生育率来说仍然较高，
							但是及时是不发达的地区，从2010年到2019年，
							它的颜色也逐渐从橙红色向青黄色过渡，
							说明即使说是在经济不发达地区，
							女性的权益也在一点一点地得到保护。'''
							)
def Birth_map() -> Timeline:
    a = Timeline()
    for i in range(2010,2018):
        map0 = (
            Map()
            .add(
                "世界青春期女性生育率", list(zip(list(青春生育率.CountryName),list(青春生育率["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="世界青春期女性生育率".format(i),
                                         subtitle_textstyle_opts=opts.TextStyleOpts(color="red",font_size=10,font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(series_index=0,max_=187),
            
            )
        )
        a.add(map0, "{}".format(i))
    return a.render_embed()
	
@app.route('/世界儿童失学儿童数量（折线图）',methods=['POST'])	
def Drop_out_of_school():
	fig = 世界失学儿童数量.T.iplot(kind="scatter",xTitle="年份",yTitle="5岁以下失学儿童数量（单位：百万）", title="世界5岁以下失学儿童数量折线图" , asFigure=True)
	py.offline.plot(fig, filename="世界失学儿童数量.html",auto_open=False)
	with open("世界失学儿童数量.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())
	return render_template('Unemployment.html',
							story = '''首先我们先来看看从2010年到2018年5岁以下儿童失学数量的变化，
							从图中我们可以看到，从2010年到2018年女童的失学人数就一直远远超过男童，
							而男童失学的数量一直呈现着下降的趋势，但是女童失学在2010年到2014年呈现下降的趋势，
							但是从2014年以后数量又逐渐地上涨，表明在2014年以后又有大批的女童的受教育权得到了侵犯。
							从图中我们可以了解到，男童女童之间失学率的差距问题，一定程度上反映出女童受教育的权益仍然没有得到很好的保护。''',
							the_plot_all = plot_all)
							

							
							
@app.route('/世界女性失业率（折线图）',methods=['POST'])	
def Umemployment_rate():
	fig = 世界女性失业率.iplot(kind="scatter",xTitle="年份",yTitle="女性失业率", title="女性失业率" , asFigure=True)
	py.offline.plot(fig, filename="employment.html",auto_open=False)
	with open("employment.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())
	return render_template('Unemployment.html',
							story = '''女性从好不容易获得了受教育的机会，
							躲过了早婚早育的传统习俗的迫害，
							从高等教育学院毕业以后，
							她们的就业情况如何呢，我们来看一下。
							从全球女性失业率的折线图看，
							在2010年到2019年间，
							全球的女性失业率总体呈下降趋势。
							但是从纵坐标看，其实全球女系失业率（占女性劳动总人口），
							一直维持在5.0几的一个水平。''',
							the_plot_all = plot_all)
							
							
							
@app.route('/女性高等教育入学率与中学入学率',methods=['POST'])	
def Enrolment_rate():
	fig = 入学率.T.iplot(kind="scatter",xTitle="年份",yTitle="入学率", title="女性高等教育入学率与中学入学率" , asFigure=True)
	py.offline.plot(fig, filename="Enrolment.html",auto_open=False)
	with open("Enrolment.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())
	return render_template('Unemployment.html',
							story = '''接下来我们看看女性中学的入学率和高等教育的入学率，
							该图是世界女性在中学与高等教育入学率所占的总人数的百分比图，
							我们可以清楚看到，在近20十年来，世界女性的中学入学率和高等教育入学率到处于一个上升阶段，
							尤其是高等教育的入学率，在近20年来，
							女性的入学率一直占总人数的50%以上，在2016年，女性进入高等教育的比例占人数的75%，而男性只有25%，
							由此我们可以出越不越多的女性受到了更好的教育，
							而且在本图中我们也可以从侧面得出一个小小结论：在学业上，女性可能比男性更加努力，至于有更多的女性被高等教育学校所录取。
							虽然女性在中学的入学率仍然没有超过男性，
							但是我们也非常欣慰地看到，入学率在逐年地上升，我们也可以侧面推断出，越来越多的家长支持女孩子上学获取知识。
							在近年来女性受教育权比之间得到了更进一步的保障''',
							the_plot_all = plot_all)

@app.route('/世界女性产假周数与报酬情况',methods=['POST'])	
def Maternity_leave():
	fig = maternity_leave.T.iplot(kind="bar", xTitle="国家",yTitle="产假周数/可获工资比例", title="世界女性产假周数与报酬情况" , asFigure=True)
	py.offline.plot(fig, filename="maternity.html",auto_open=False)
	with open("maternity.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())
	return render_template('Unemployment.html',
							story = '''产假的周数反映了一个国家对待女性生育权益的一个态度，
							最后我们来看看世界范围内，
							女性的产假周数如何，
							从地图上看，我们可以注意到，
							其实在全球范围内，
							女性产假的时长都是比较平均的一个值，维持在15-16周左右，
							而我们可以主要到在北欧地区的国家产假的长度要比世界上大部分国家都要长，
							例如产假最长的国家是挪威长达68周，可以表明在北欧地区的国家比较重视女性的生育权利，
							而巴布亚新几内亚的产假最短，
							只有短短的6周时间。从条形图上看，
							我们可以观察到世界上大部分的国家女性在产假期间都能拿到和工作期间一样的工资，
							只有少数地方拿到的工资比工作前还要少。
							虽然全球产假长度有15-16周，但是它仍然只是一个平均数，在部分不甚发达的国家，女性的生育期权益
							并没有得到很好的保障，就比如说产假只有6周的巴布亚新几内亚，这就意味着在女性很有可能在怀孕8-9月时仍然在工作岗位上，
							这是不利于女性生育健康的行为。同样部分国家在产假期间女性就只能拿到平时的一半的工资（如：乍得），
							我们也会认为这个国家也没有很好地保护了女性的权益。
							''',
							the_plot_all = plot_all)

if __name__ == '__main__':
    app.run(debug=True)
	
	
	




	
	
	
	
	
