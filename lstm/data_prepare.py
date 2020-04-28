#!usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time
import sys

# python data_prepare.py <level> (level1, level2 or level3)


RAW_DATA = 'data/Crimes_-_2001_to_present.csv'
PROCESS_LEVEL1 = 'data/date_format.csv'
PROCESS_LEVEL2 = 'data/crime_D.csv'
PROCESS_LEVEL3 = 'data/crime_H.csv'


if len(sys.argv) <= 1:
	print('python data_prepare.py <level>')
	sys.exit()

flag = sys.argv[1]


if flag == 'level2' or 'level3':
	
	start = time.time()

	print("READ DATE DATA..")
	raw_data = pd.read_csv(PROCESS_LEVEL1, index_col = ['Date'], parse_dates = ['Date'])

	end = time.time()
	print(end-start)

	print("RESAMPLE..")
	'''
	print(raw_data.shape)
	for i in range(9):
		raw_data.drop(pd.to_datetime('1/1/200'+str(i+1)+' 0:00'), inplace = True)
	for i in range(10):
		raw_data.drop(pd.to_datetime('1/1/201'+str(i)+' 0:00'), inplace = True)
	print(raw_data.shape)
	'''
	# Attribute for resample
	f = {'Type': 'count', 'Type_property': 'sum', 'Type_violent': 'sum', \
	'Loc_public': 'sum', 'Loc_private': 'sum', 'Arrest': 'sum', 'Domestic': 'sum'}

	# Resample by one day 
	if flag == 'level2':
		raw_data = raw_data.resample('1D').agg(f)
		raw_data.to_csv(PROCESS_LEVEL2)

	# Resample by one hour 
	elif flag == 'level3':
		raw_data = raw_data.resample('1H').agg(f)
		raw_data.to_csv(PROCESS_LEVEL3)
	
	print("SAVE")
	

if flag == 'level1':

	print("READ RAW DATA..")
	raw_data = pd.read_csv(RAW_DATA, usecols=['Date', 'Primary Type', 'Location Description', 'Arrest', 'Domestic'], \
		dtype = {'Date':object, 'Primary Type': object, 'Location Description': object, 'Arrest': bool, 'Domestic': bool})
	raw_data.rename(columns={'Primary Type': 'Type', 'Location Description': 'Location'}, inplace = True)

	# Category raw data to create time series data
	# Divid crime type and location into two classes, repectively
	raw_data['Type_property'] = False
	raw_data['Type_violent'] = False
	raw_data['Loc_public'] = False
	raw_data['Loc_private']= False

	Type_property = ['THEFT', 'BURGLARY', 'ROBBERY', 'MOTOR VEHICLE THEFT']
	Type_violent = ['BATTERY', 'ASSAULT', 'CRIM SEXUAL ASSAULT', 'CRIMINAL DAMAGE', 'SEX OFFENSE']
	Loc_public = ['STREET', 'SIDEWALK', 'PARKING LOT/GARAGE(NON.RESID.)', 'ALLEY', 'SCHOOL, PUBLIC, BUILDING']
	Loc_private = ['RESIDENCE', 'APARTMENT', 'RESIDENCE-GARAGE', 'SMALL RETAIL STORE', 'RESIDENCE PORCH/HALLWAY']

	print("CATEGORY..")

	mask = raw_data['Type'].isin(Type_property)
	raw_data['Type_property'] = np.where(mask, 1, 0)
	mask = raw_data['Type'].isin(Type_violent)
	raw_data['Type_violent'] = np.where(mask, 1, 0)
	mask = raw_data['Location'].isin(Loc_public)
	raw_data['Loc_public'] = np.where(mask, 1, 0)
	mask = raw_data['Location'].isin(Loc_private)
	raw_data['Loc_private'] = np.where(mask, 1, 0)

	'''
	# version below is slower
	for row in raw_data.itertuples():
		if row.Type in Type_property:
			raw_data.set_value(row.Index, 'Type_property', 1)
		elif row.Type in Type_violent:
			raw_data.set_value(row.Index, 'Type_violent', 1)
		if row.Location in Loc_public:
			raw_data.set_value(row.Index, 'Loc_public', 1)
		elif row.Location in Loc_private:
			raw_data.set_value(row.Index, 'Loc_private', 1)
	'''

	# Save datetime data as process level1, for it is time consuming 
	print('TO_datetime..')
	start = time.time()

	date_cache = {k: pd.to_datetime(k) for k in raw_data['Date'].unique()}
	raw_data['Date'] = raw_data['Date'].map(date_cache)
	raw_data.set_index(['Date'], inplace=True)

	end = time.time()
	print(end-start)

	raw_data.to_csv(PROCESS_LEVEL1)
	print('SAVE')