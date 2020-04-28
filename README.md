# Crime Analysis

This is a course project :sparkles:

## Data Fetch
put crime.csv in the src file

**if not at the same path**
```python
import sys
import os 
import read_crime

sys.path.append(os.path.abspath("ca/pro_data"))
print(sys.path)
i = read_crime.Input(r'crime.csv')
print(i.data_extract(0,0))
```

**if at the path**
```python
import read_crime
path = r"src\crime.csv"
i = read_crime.Input(path)
print(i.data_extract())
```

```python
class Input(object):
    path = r"src\crime.csv"
    def __init__(self, path):
    def data_extract(self, row_num = 0, col_name = 0, year = 0, nan_not_allowed = 0, primary_type = 0, time_range = 0, arrest = 0):
        ''' 
        path: 路径，默认为相对路径
        col_name：列选择， 默认为所有有用列
        year：年份选择2001-2018，默认为所有时间
        nan_not_allowed：是否允许空值，默认允许，如果不允许则设为 1
        row_num：行数，默认全部行
        primary_type：犯罪类型，一共26种，默认全部
        time_range：时间范围，格式如['2017-03-20', '2017-12-01']，默认全部
        arrest：是否抓捕-1 没有， 1 有， 默认全部
        '''
```

## **Data Collection** :floppy_disk:

## **Data Preprocessing** :thermometer: 
use spark to pre-precrossing data and get some statistical results. :fire::fire::fire:
 - [x] Spark Code: 
spark-submit --class pre_process.execute target/lsu018-1.0-SNAPSHOT.jar /data/data/crime.csv THEFT /data/output/ward /data/output/block /data/output/district /data/output/month /data/output/day /data/output/location /data/output/community
 - [x] ~~Data Cleansing, got from database, do not need cleansing~~
 - [x] Data Reduction 
 - [x] Data Transformation
 - [x] Data Integration
 
## Algorithms :desktop_computer:
Problem Solver is Good Algorithm
- [x] DFT
- [ ] kNN
- [x] DBscan
- [x] K-means
- [ ] Random Forest
- [x] RNN
- [ ] Sentiment Analysis
- [ ] A* Search

## Visualization :bar_chart:
Good-looking
- [x] Map Visualization :world_map:
- [x] WordCloud Visualization :cloud: 
- [x] Time Series Visualization :hourglass:
- [ ] Correlation Visualization :butterfly:
- [ ] TreeMap Visualization :palm_tree:
