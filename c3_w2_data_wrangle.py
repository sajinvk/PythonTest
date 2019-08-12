# coding: utf-8
get_ipython().run_line_magic('load', 'c3_w2_data_wrangle.py')
# %load c3_w2_data_wrangle.py
import pandas as pd
FileName= 'imports-85.data'
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
         
df = pd.read_csv(FileName, names = headers)
df.head
df.head(3)
df.columns
get_ipython().system('cat imports-85.data |grep Nan')
get_ipython().system('cat imports-85.data |grep -i Nan')
get_ipython().system('cat imports-85.data |grep -i nan')
import numpy as np
df.replace('?', np.nan ) 
df.replace('?', np.nan ).head
df.replace('?', np.nan ).head(5)
df.replace('?', np.nan,inplace = True )
df["normalized-losses"]
avg_normloss = df["normalized-losses"].mean()
avg_normloss = df["normalized-losses"].mean(axis =0)
avg_normloss = df["normalized-losses"].astype('float').mean(axis =0)
avg_normloss
df["normalized-losses"].replace(np.nan , avg_normloss , inplace = True)
df["normalized-losses"].head()
avg_bore = df["bore"].astype("float").mean()
avg_bore
avg_bore = df["bore"].astype("float").mean(axis=0)
avg_bore
df.columns
df["bore"].replace(np.nan, avg_bore , inplace = True)
avg_stroke= df["stroke"].astype("float").mean()
df["stroke"].replace(np.nan,avg_stroke , inplace = True)
avg_4=df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_4, inplace= True)
avg_5=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_5, inplace= True)
df['num-of-doors'].value_counts
df['num-of-doors'].value_counts()
df['num-of-doors'].value_counts().idmax()
df['num-of-doors'].value_counts().idmax
df['num-of-doors'].value_counts().idxmax()
df['num-of-doors'].value_counts().idxmax
df['num-of-doors'].value_counts().idxmax()
df["num-of-doors"].replace(np.nan, "four", inplace = True)
df["price"].dropna(axis = 0 )
df["price"].dropna(axis = 0 ,inplace = True)
df.head9)
df.head()
df.dtypes
