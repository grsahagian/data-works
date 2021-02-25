#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# deleted summary data included in CSV report via Excel
raw = pd.read_csv("/Users/Graham/data-works/google-analytics-analysis/dailyuserdata.csv", parse_dates=True)


# In[3]:


# removing excess "unnamed rows" that were read from the CSV file for some reason
data = raw[["Day Index","Users","New Users"]]


# In[4]:


# setting index
data = data.set_index("Day Index")


# In[28]:


plt.figure(figsize=(30,20))

plt.plot(data["Users"], label="Users")
plt.plot(data["New Users"], label="New Users")
plt.legend(loc=0)
# loc=0 == best location


# In[ ]:




