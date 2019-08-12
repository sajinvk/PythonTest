# coding: utf-8
import pandas as pd
pd.read_csv('drivers_data.csv')
df = pd.read_csv('drivers_data.csv')

import numpy as np 
from  sklearn.cluster import KMeans
df = pd.read_csv('drivers_data.csv',sep='\t')
df.columns
f1=df['Distance_Feature'].values
f1
f2=df['Speeding_Feature'].values
X = np.array(list(zip(f1, f2)))
kmeans = KMeans(n_clusters=2).fit(X)
kmeans.labels_
kmeans.cluster_centers_
