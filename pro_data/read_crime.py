import pandas as pd
import csv
import numpy as np

class Input(object):
    path = r"src\crime.csv"
    def __init__(self, path):
        # Primary Type
        '''
        DECEPTIVE PRACTICE         
        THEFT                     
        NARCOTICS                    
        OFFENSE INVOLVING CHILDREN    
        OTHER OFFENSE                  
        CRIM SEXUAL ASSAULT           
        SEX OFFENSE                  
        BATTERY                      
        CRIMINAL DAMAGE              
        BURGLARY                   
        MOTOR VEHICLE THEFT            
        ASSAULT                        
        CRIMINAL TRESPASS               
        ROBBERY                         
        WEAPONS VIOLATION               
        OBSCENITY                      
        NON-CRIMINAL                   
        '''
        # Year
        '''
        2001
        ...
        2018
        '''
        self.path = path
        print("调用数据")

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
        if col_name is 0:
            col_name = ['Date', 'Block', 'Primary Type','Description', 'Location Description', 'Arrest', 'Domestic','Beat', 'District', 'Ward', 'Community Area', 'FBI Code', 'Year', 'Latitude', 'Longitude', 'Location']
        data = pd.read_csv(self.path, header = 0, nrows = row_num)
        if not row_num: 
            data = pd.read_csv(self.path, header = 0)

        if primary_type: 
            data = data[(data['Primary Type'] == primary_type)]

        if year:
            data = data[(data['Year'] == year)]

        data['idx'] = pd.to_datetime(data['Date']) #将Date数据类型转换为日期类型
        data = data.set_index('idx') # 设置日期作为索引
        if time_range: 
            data = data[time_range[0]:time_range[1]]

        if nan_not_allowed: 
            data = data.dropna(axis=0, how='all')

        if arrest == 1: 
            data = data[(data['Arrest'] == 'True')]
        elif arrest == -1: 
            data = data[(data['Arrest'] == 'False')]

        data = data[col_name]
        data = data.fillna(0)
        print('shape')
        print(data.shape)
        print('statistics')
        print(data.describe())
        print('data samples 10 rows')
        print(data.head(10))
        return data