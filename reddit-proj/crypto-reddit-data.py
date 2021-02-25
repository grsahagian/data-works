#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[30]:


df = pd.read_csv('/Users/Graham/data-works/reddit-proj/subreddit_data.csv')
df.head()


# In[ ]:





# In[34]:


btc = df.loc[df['label'] == 'bitcoin']
eth = df.loc[df['label'] == 'ethereum']
xrp = df.loc[df['label'] == 'xrp']


# In[ ]:





# In[33]:





# In[ ]:




