# coding: utf-8
import pandas as pd
pd.read_excel('pyplot.xlsx' ,sheet_name='Canada by Citizenship',skiprows=range(20), skip_footer=2)
df_can=pd.read_excel('pyplot.xlsx' ,sheet_name='Canada by Citizenship',skiprows=range(20), skip_footer=2)
df_can.head
df_can.head(2)
df_can.set_index('OdName',inplace=True)
df_can.index.values
print(df_can.loc['Japan'])
import matplotlib as mpl
import matplotlib.pyplot as plt
haiti =df_can.loc['Haiti' , range(1983,2003)]
haiti.plot()
plt.show()
