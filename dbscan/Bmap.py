#!/usr/bin/env python
# coding: utf-8

# In[300]:


import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import ThemeType,BMapType
import os
import json


# In[348]:


name = 'Crimes_todo'
csv = pd.read_csv(name+'.csv')
csv.columns = ['x','y','labels']
csv


# In[302]:


X = csv[:10000].copy()
X['x'] = X['x'].map(lambda x:x+41)
X['y'] = X['y'].map(lambda x:x-87)
X


# In[303]:


X.groupby('labels')
for i in X.groupby('labels'):
    print(i[0])


# In[304]:


BAIDU_AK = "K82VhnFNsV6cOFxG5wL84i3gGm23LbhG"
# with open(
#     os.path.join("custom_map_config.json"), "r", encoding="utf-8"
# ) as f:
#     mapstylejson = json.load(f)
c = (BMap(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
     .add_schema(
         baidu_ak=BAIDU_AK,
         center=[-87.65005,41.85003],
         zoom=11,
         map_style={
                "styleJson": [{
                    'featureType': 'water',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'land',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#f3f3f3'
                    }
                }, {
                    'featureType': 'railway',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'highway',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#fdfdfd'
                    }
                }, {
                    'featureType': 'highway',
                    'elementType': 'labels',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'geometry',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'geometry.fill',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'poi',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'green',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'subway',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'manmade',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'local',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'labels',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'boundary',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'building',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'label',
                    'elementType': 'labels.text.fill',
                    'stylers': {
                        'visibility': 'off'
                    }
                }]
            }
         
    
     ))
for index, row in X.iterrows():
    c = c.add_coordinate(index, row['y'], row['x'])
for group in X.groupby('labels'):
    c =c.add(
        series_name = group[0],
        type_= "scatter",
        is_large = True,
        large_threshold = 2000,
        symbol_size = 5,
        label_opts = opts.LabelOpts(is_show = False),
        tooltip_opts = opts.TooltipOpts(formatter = '{c}'),
        data_pair = [list(z) for z in zip(list(group[1].index), group[1]['labels'])]
         )
c = (c.add_control_panel(
    navigation_control_opts = opts.BMapNavigationControlOpts(position = BMapType.ANCHOR_TOP_LEFT),
    maptype_control_opts = opts.BMapTypeControlOpts()))
c = c.set_global_opts(title_opts=opts.TitleOpts(title="Clusters of Crime"))
c.render(name+'scatter.html')


# In[393]:


map_c = pd.read_csv('dbscanoutput.csv')[:10000]
map_c.columns = ['x','y','labels']
gp_col = 'labels'
x = -87.65005
y = 41.85003
a = map_c.groupby(gp_col).count()
a = a.rename(columns={'labels':'labels','x':'count','y':'a'}).drop(columns =['a'], axis = 1)['count'].tolist()
mx = map_c.groupby(gp_col)['x'].mean()
my = map_c.groupby(gp_col)['y'].mean()
cc = pd.concat([mx,my],axis=1)
c1 = cc['x'].tolist()
c2 = cc['y'].tolist() 
cc['x'] = cc['x'].map(lambda x:x+41)
cc['y'] = cc['y'].map(lambda x:x-87)
cc['values'] = a
cc


# 

# In[401]:


from pyecharts.faker import Collector, Faker
c = (BMap().add_schema(baidu_ak=BAIDU_AK, center=[-87.65005,41.85003],zoom=11,
         map_style={
                "styleJson": [{
                    'featureType': 'water',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'land',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#f3f3f3'
                    }
                }, {
                    'featureType': 'railway',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'highway',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#fdfdfd'
                    }
                }, {
                    'featureType': 'highway',
                    'elementType': 'labels',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'geometry',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'geometry.fill',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'poi',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'green',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'subway',
                    'elementType': 'all',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'manmade',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'local',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'arterial',
                    'elementType': 'labels',
                    'stylers': {
                        'visibility': 'off'
                    }
                }, {
                    'featureType': 'boundary',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#fefefe'
                    }
                }, {
                    'featureType': 'building',
                    'elementType': 'all',
                    'stylers': {
                        'color': '#d1d1d1'
                    }
                }, {
                    'featureType': 'label',
                    'elementType': 'labels.text.fill',
                    'stylers': {
                        'visibility': 'off'
                    }
                }]
            }))
for index, row in cc.iterrows():
    c = c.add_coordinate(index, row['y'], row['x'])
c = (c.add(
            "crimes",
            [list(z) for z in zip(list(cc.index), cc['values'])],
            type_="heatmap",
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
     .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-crimes"),
            visualmap_opts=opts.VisualMapOpts(min_ = 0,max_=1,type_ = "size"
                                             )
        ))
c.render_notebook()
# c.render(name+'_heatmap.html')

