#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# In[2]:


warnings.filterwarnings('ignore')


# In[34]:


read=pd.read_csv("C:/Users/HP/Desktop/ml-100k/u.data",sep="\t",names=columns)


# In[35]:


read.head(5)


# In[33]:


columns=['user_id','name_id','rating','timestamp']


# In[26]:


read2=pd.read_csv("C:/Users/HP/Desktop/ml-100k/u.item",sep="\|",header=None)


# In[27]:


read2.head(5)


# In[28]:


read2=read2[[0,1]]


# In[29]:


read2.head()


# In[30]:


read2.columns=['name_id','title']


# In[32]:


read2.head()


# In[38]:


read.head()


# In[39]:


read2.head()


# In[41]:


dg=pd.merge(read,read2,on='name_id')


# In[45]:


dg.tail()


# In[49]:


dg.groupby('title').mean()['rating'].sort_values(ascending=False)


# In[50]:


dg.groupby('title').count()['rating'].sort_values(ascending=False)


# In[51]:


read3=pd.DataFrame(dg.groupby('title').mean()['rating'].sort_values(ascending=False))


# In[52]:


read3


# In[55]:


read4=pd.DataFrame(dg.groupby('title').count()['rating'].sort_values(ascending=False))


# In[56]:


read4


# In[59]:


plt.hist(read4['rating'],bins=50)
plt.show()


# In[81]:


plt.hist(read3['rating'],bins=50)
plt.show()


# In[82]:


read4['mean']=pd.DataFrame(dg.groupby('title').mean()['rating'].sort_values(ascending=False))


# In[83]:


read4


# In[84]:


sns.jointplot(x='mean',y='rating',data=read4)


# In[85]:


dg


# In[87]:


movirate1=dg.pivot_table(index='user_id',values='rating',columns='title')


# In[88]:


movirate1


# In[89]:


read4


# In[92]:


x1=movirate1['Star Wars (1977)']


# In[93]:


x1.head()


# In[95]:


similar_to_star_war=movirate1.corrwith(x1)


# In[96]:


similar_to_star_war


# In[ ]:





# In[102]:


similar_to_star_war2=pd.DataFrame(similar_to_star_war,columns=['Correalation'])


# In[104]:


similar_to_star_war2.dropna(inplace=True)


# In[124]:


cv=similar_to_star_war2.join(read5)


# In[125]:


cv


# In[107]:


read4


# In[108]:


read3


# In[109]:


read2


# In[110]:


read


# In[117]:


read5=pd.DataFrame(dg.groupby('title').count()['rating'])


# In[119]:


read5.columns=['count']


# In[120]:


read5


# In[132]:


prediction=cv[cv['count']>100].sort_values("Correalation",ascending=False)


# In[133]:


prediction


# In[134]:


def moviename(movie_name):
    movie_user_rating=movirate[movie_name]
    similar_to_movie=movirate1.corrwith(movie_user_rating)
    similar_to_movie=pd.DataFrame(similar_to_movie,columns=['Correalation'])
    similar_to_movie.dropna(inplace=True)
    cv=similar_to_movie.join(read5['count'])
    prediction=cv[cv['count']>100].sort_values("Correalation",ascending=False)
    
    
    return prediction


# In[135]:


moviename("Titanic (1997)")


# In[ ]:




