#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from pyecharts.charts import Scatter
from pyecharts import options as opts
import seaborn as sns
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# In[74]:


X = pd.read_csv('NARCOTICS.csv')
X = X[['Latitude','Longitude']]
X.columns = ['x','y']


# In[75]:


data = X[:10000].copy()
data['x'] = data['x'].map(lambda x:x-41)
data['y'] = data['y'].map(lambda y:y+87)
data = data[(data.x>-1)]
sns.relplot(x="x",y="y",data=data)


# In[66]:


db = DBSCAN(eps=0.017, min_samples=1000).fit(data) #DBSCAN and parameter 
data['labels'] = db.labels_  #In the same dimension as X, the value of the index number corresponding to labels is the number of her cluster
labels = db.labels_
raito = data.loc[data['labels']==-1].x.count()/data.x.count() #the proportion of the number of noise points in the total number
print('Noise ratio:', format(raito, '.2%'))
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # Get the number of clusters
print('Number of clusters: %d' % n_clusters_)
print("contour coefficient: %0.3f" % metrics.silhouette_score(data, labels)) #Evaluation of clustering by contour coefficient
plt.xlim(0.5, 1.2)
plt.ylim(-1, -0.5)
plt.scatter(data['x'], data['y'], c=data['labels'], marker='.')
plt.show()


# In[76]:


n = 1000;
while n > 5:
    db = DBSCAN(eps=0.017, min_samples=int(n)).fit(data)
    data['labels'] = db.labels_
    labels = db.labels_
    raito = data.loc[data['labels']==-1].x.count()/data.x.count()
    print('Noise ratio:', format(raito, '.2%'))
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # Get the number of clusters
    print('Number of clusters: %d' % n_clusters_)
    print("contour coefficient: %0.3f" % metrics.silhouette_score(data, labels))  # Evaluation of clustering by contour coefficient
    n = n/1.5


# In[77]:


db = DBSCAN(eps=0.017, min_samples=5).fit(data)
data['labels'] = db.labels_
labels = db.labels_
raito = data.loc[data['labels']==-1].x.count()/data.x.count()
print('Noise ratio:', format(raito, '.2%'))
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # Get the number of clusters
print('Number of clusters: %d' % n_clusters_)
print("contour coefficient: %0.3f" % metrics.silhouette_score(data, labels)) #Evaluation of clustering by contour coefficient
plt.xlim(0.5, 1.2)
plt.ylim(-1, -0.5)
plt.scatter(data['x'], data['y'], c=data['labels'], marker='.')
plt.show()
metrics.calinski_harabasz_score(data,labels)


# In[57]:


plt.xlim(0.5, 1.2)
plt.ylim(-1, -0.5)
plt.scatter(data['x'], data['y'], c=data['labels'], marker='.')
plt.show()
metrics.calinski_harabasz_score(data,labels)


# In[100]:


rs= []#Storage evaluation score and noise ratio
eps = np.arange(0.015,0.025,0.001) #eps from 0.2 to 4
min_samples=np.arange(2,10,1)#min_samples from 2 to 20
best_score=0
best_score_eps=0
best_score_min_samples=0
for i in eps:
    for j in min_samples:
        try:
            db = DBSCAN(eps=i, min_samples=j).fit(data)
            labels= db.labels_
            k=metrics.silhouette_score(data,labels)
            raito = len(labels[labels[:] == -1]) / len(labels)
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            rs.append([i,j,k,raito,n_clusters_])
            if k>best_score:
                best_score=k
                best_score_eps=i
                best_score_min_samples=j
        except:
            db=''
        else:
            db=''
rs= pd.DataFrame(rs)
rs.columns=['eps','min_samples','score','raito','n_clusters']


# In[1]:


sns.relplot(x="eps",y="min_samples", size='score',data=rs)
sns.relplot(x="eps",y="min_samples", size='raito',data=rs)


# In[78]:


data
data.to_csv('dbscanNARCOTICS.csv',index=False)

