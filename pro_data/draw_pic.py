plot_path = "../output/all type/"
plot_file = "/part-00000"
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
import random
number_of_colors = 30

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(color)
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index
all_type = ["NARCOTICS", "NON-CRIMINAL", "DECEPTIVE PRACTICE", "THEFT", "SEX OFFENSE", "BURGLARY", "ASSAULT", "BATTERY", "ROBBERY", "WEAPONS VIOLATION"]
def bar_base(rand, month, type) -> Bar:
    c = (
        Bar()
        .add_xaxis(month[0].tolist())
        .add_yaxis("Month", month[1].tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title=type + "Crime Frequency Total Year", subtitle="For Month"))
    )
    return c
def bar_day(rand, day, type) -> Bar:
    c = (
        Bar()
        .add_xaxis(day[0].tolist())
        .add_yaxis("Day", day[1].tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title=type + "Crime Frequency Total Month", subtitle="For Day"))
    )
    return c
def bar_hour(rand, hour, type) -> Bar:
    c = (
        Bar()
        .add_xaxis(hour[0].tolist())
        .add_yaxis("Hour", hour[2].tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title=type + "Crime Frequency One Day", subtitle="For Hour"))
    )
    return c

for idx, type in enumerate(all_type): 
    day = pd.read_table(plot_path+'/day/'+type+'/'+plot_file,header=None,delim_whitespace=True)
    month = pd.read_table(plot_path+'/month/'+type+'/'+plot_file,header=None,delim_whitespace=True)
    hour = pd.read_table(plot_path+'/hour/'+type+'/'+plot_file,header=None,delim_whitespace=True)
    # monthday = pd.read_table(plot_path+'/monthday'+plot_file,header=None,delim_whitespace=True)
    # col1 = monthday[0].astype(str) 
    # col2 = monthday[1].astype(str)
    # monthday['Rank'] = (col1+col2).astype(int).rank(method='dense', ascending=True).astype(int)
    # monthday = monthday.sort_values(by=[0,1])
    # monthday[0] = monthday[0].astype(str) 
    # monthday[1] = monthday[1].astype(str) 
    # monthday[0] = '2040-' + monthday[0].str.cat(monthday[1], sep = '-')
    # monthday[0] = pd.to_datetime(monthday[0]).apply(lambda x: x.date())
    # monthday = monthday.drop(columns = [1], axis=1)
    # mi = monthday[2].min()
    # ma = monthday[2].max()
    # print(mi)
    # calendar = tuple(monthday.itertuples(index=False, name=None))
    # calendar = [[str(x[0]), x[1]] for x in calendar]
    # print(calendar)

    hour = hour.sort_values(by=[1,0])
    hour[0] = hour[0].astype(str) 
    hour[0] = hour[0].str.cat(hour[1], sep = ' ')
    hour = hour.drop(columns = [1], axis=1)
    print(hour)

    month = month.sort_values(by=[0])
    print(month)

    day = day.sort_values(by=[0])
    print(day)

    # month day
    # calendar
    # import datetime

    # from pyecharts import options as opts
    # from pyecharts.charts import Calendar


    # def calendar_base() -> Calendar:
    #     data = a

    #     c = (
    #         Calendar()
    #         .add("", data, calendar_opts=opts.CalendarOpts(range_="2040"))
    #         .set_global_opts(
    #             title_opts=opts.TitleOpts(title="Crime Frequency from 2001-2018"),
    #             visualmap_opts=opts.VisualMapOpts(
    #                 max_=ma,
    #                 min_=mi,
    #                 orient="horizontal",
    #                 is_piecewise=True,
    #                 pos_top="230px",
    #                 pos_left="100px",
    #             ),
    #         )
    #     )
    #     return c
    # # calendar_base().render(path='./01.png')
    # calendar_base().render_notebook()




    bar_base(color[idx], month, type).render_notebook()


    bar_day(color[idx+10], day, type).render_notebook()


    bar_hour(color[idx+20], hour, type).render_notebook()