# coding: utf-8
import pandas as pd
import numpy as np
pd.read_excel('pyplot.xlsx', sheet_name='Canada by Citizenship' , skiprows=range(0,20) , skip_footer=2)
df_can=pd.read_excel('pyplot.xlsx', sheet_name='Canada by Citizenship' , skiprows=range(0,20) , skip_footer=2)
df_can.head
df_can.head(2)
df_can.shape
df_can.drop(['AREA','REG','DEV','Type','Coverage'],axis=1)
#help(df_can.drop)
df_can.drop(['AREA','REG','DEV','Type','Coverage'],axis=1,inplace=True)
df_can.head(2)
#help(df_can.rename)
df_can.rename(columns={'OdName':'Country','AreaName':'Continent','RegName':'Region'},inplace=True)
df_can.head(2)
df_can.columns
df_can.columns
#help(map)
df_can['Country']
df_can['Country'] == 'Zimbawe'
df_can['Country']
df_can['Country'] == 'Yemen'
df_can.set_index('Country')
df_can['Country'] == 'Yemen'
df_can['Total'] = df_can.sum()
df_can.head(2)
#help(df_can.sum)
df_can['Total'] = df_can.sum(axis=1)
df_can.head(2)
years = range(1984,2013)
years
print(years)
for x in years:
    print (x)
    
