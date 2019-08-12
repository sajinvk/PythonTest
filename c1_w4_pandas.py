# coding: utf-8
import pandas as pd 
new_dict = {"c1" : [1,2,3,4,5],
            "c2" : ['a','b','c','d','e'],
            "c3" : [True , False , True , True , False ],
            "c4" : [.2, .5 , 44.44 , 999.99 , 11.0 ]
           }    
           
new_dataframe = pd.DataFrame(new_dict)
pd.read_csv('database.csv')
data = pd.read_csv('database.csv', encoding='utf-8')
data = pd.read_csv('database.csv', encoding= "ISO-8859-1")
data.shape
data.ndim
data.head()
data.tail(2)
data.dtypes
data.describe()
data['Y2013'].describe()
#using a dot notation, e.g. data.column_name,
#using square braces and the name of the column as a string, e.g. data['column_name']
#or using numeric indexing and the iloc selector data.iloc[:, <column_number>]
data.Area.head()
data[Area].head()
data['Area'].head()
data.iloca[:,25].head()
data.iloca[i,25].head()
data.iloc[:,25].head()
data['Area', 'Y2013'].max()
data['Area'].max()
data['Y2013'].min()
data['Y2013'],'Area'].min()
data['Y2013','Area'].min()
data['Y2013'].sum()
vlist = [data['Y2013'].sum(),data['Y2013'].min()]
vlistdata['Y2013'].sum()
vlist = [data['Y2013'].sum(),data['Y2013'].min()]
vlist
