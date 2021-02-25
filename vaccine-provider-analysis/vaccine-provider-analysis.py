#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_ml_quant import pd, np


# In[2]:


date_from = "2019-12-30"
date_until = "2020-11-30"


# In[9]:


# Moderna
_mrna = pd.fetch_yahoo("MRNA").loc[date_from:date_until]
# Johnson & Johnson
_jnj = pd.fetch_yahoo("JNJ").loc[date_from:date_until]
# Astrazeneca
_azn = pd.fetch_yahoo("AZN").loc[date_from:date_until]
# Merck
_mrk = pd.fetch_yahoo("MRK").loc[date_from:date_until]
# Novavax
_nvax = pd.fetch_yahoo("NVAX").loc[date_from:date_until]


# In[15]:


mrna = _mrna["Close"]
jnj = _jnj["Close"]
azn = _azn["Close"]
mrk = _mrk["Close"]
nvax = _nvax["Close"]


# In[16]:


df = pd.concat([mrna, jnj, azn, mrk, nvax], join='inner',axis=1)
df.columns = ['MRNA','JNJ','AZN','MRK', 'NVAX']


# In[17]:


df.plot(figsize=(20,20))


# In[ ]:




