#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from pandas_ml_utils.ml.summary import ClassificationSummary
from pandas_ml_utils import FeaturesAndLabels, Model, SkModel
from pandas_ml_quant import pd, np
import seaborn as sns
import scipy.stats as scs


# In[3]:


date_since = "2019-12-30"
date_until = "2020-09-30"


# In[4]:


_nvda = pd.fetch_yahoo("NVDA").loc[date_since:date_until]
_asml = pd.fetch_yahoo("ASML").loc[date_since:date_until]
_unp = pd.fetch_yahoo("UNP").loc[date_since:date_until]
_sedg = pd.fetch_yahoo("SEDG").loc[date_since:date_until]
_nice = pd.fetch_yahoo("NICE").loc[date_since:date_until]
_band = pd.fetch_yahoo("BAND").loc[date_since:date_until]
_zm = pd.fetch_yahoo("ZM").loc[date_since:date_until]
_work = pd.fetch_yahoo("WORK").loc[date_since:date_until]
_now = pd.fetch_yahoo("NOW").loc[date_since:date_until]
_zs = pd.fetch_yahoo("ZS").loc[date_since:date_until]
_fvrr = pd.fetch_yahoo("FVRR").loc[date_since:date_until]
# other stonks
_sny = pd.fetch_yahoo("SNY").loc[date_since:]


# In[5]:


nvda = _nvda["Close"]
asml = _asml["Close"]
unp = _unp["Close"]
sedg = _sedg["Close"]
nice = _nice["Close"]
band = _band["Close"]
zm = _zm["Close"]
work = _work["Close"]
now = _now["Close"]
zs = _zs["Close"]
fvrr = _fvrr["Close"]
sny = _sny["Close"]


# In[ ]:





# In[ ]:





# In[6]:


df = pd.concat([nvda,asml,unp,sedg,nice,band,zm,work,now,zs,fvrr,sny], join='inner', axis=1)


# In[7]:


# df.plot(subplots=True,figsize=(10,6))


# In[8]:


df.columns = ['NVDA','ASML','UNP','SEDG','NICE','BAND','ZM','WORK','NOW','ZS','FVRR','SNY']


# In[9]:


df.head()


# In[10]:


def statistics(array):
    sta = scs.describe(array)
    
    print('%14s %15s' % ('statistic', 'value'))
    print(30 * "-")
    print('%14s %15.5f' % ('size', sta[0]))
    print('%14s %15.5f' % ('min', sta[1][0]))
    print('%14s %15.5f' % ('max', sta[1][1]))
    print('%14s %15.5f' % ('mean', sta[2]))
    print('%14s %15.5f' % ('std', np.sqrt(sta[3])))
    print('%14s %15.5f' % ('skew', sta[4]))
    print('%14s %15.5f' % ('kurtosis', sta[5]))
    print(30 * "=")


# In[11]:


def _returns(df):
    return np.log(df / df.shift(1))

# All stocks returns since around 2019 (latest available data)
returns = df.apply(_returns)


# In[12]:


# Returns for whole horizon (date_since:date_until), not just since data is available for all stocks
nvda_r = np.log(_nvda["Close"] / _nvda["Close"].shift(1))
asml_r = np.log(_asml["Close"] / _asml["Close"].shift(1))
unp_r = np.log(_unp["Close"] / _unp["Close"].shift(1))
sedg_r = np.log(_sedg["Close"] / _sedg["Close"].shift(1))
nice_r = np.log(_nice["Close"] / _nice["Close"].shift(1))
band_r = np.log(_band["Close"] / _band["Close"].shift(1))
zm_r = np.log(_zm["Close"] / _zm["Close"].shift(1))
work_r = np.log(_work["Close"] / _work["Close"].shift(1))
now_r = np.log(_now["Close"] / _now["Close"].shift(1))
zs_r = np.log(_zs["Close"] / _zs["Close"].shift(1))
fvrr_r = np.log(_fvrr["Close"] / _fvrr["Close"].shift(1))
sny_r = np.log(_sny["Close"] / _sny["Close"].shift(1))


# In[13]:


for ticker in returns:
    print('\nResults for {}'.format(ticker))
    print(30 * '-')
    log_data = np.array(returns[ticker].dropna())
    statistics(log_data)


# In[14]:


plt.figure(figsize=(20,10))
plt.hist(unp_r, bins=70, range=(-0.12,0.12), label='observed')
plt.xlabel('returns')
plt.ylabel('frequency')
x = np.linspace(plt.axis()[0], plt.axis()[1])
plt.plot(x, scs.norm.pdf(x, unp_r.mean(), unp_r.std()), 'r',lw=2.0,label='pdf')
plt.legend()


# In[15]:


returns.hist(bins=50,figsize=(30,20))


# In[16]:


df.plot(figsize=(20,20))


# In[17]:


corrMatrix = df.corr()

fig, ax = plt.subplots(figsize=(20,15))
sns.heatmap(corrMatrix, annot=True, vmin=0, vmax=1, cmap='magma_r', ax=ax)


# In[ ]:





# In[18]:


for i in df:
    print(min(df[i]))


# In[19]:


# is not iterating over whole array for some reason
def find_min_date(df):
        for i in df:
            return df[i].loc[df[i] == df[i].min()]
print(find_min_date(df))


# In[20]:


df.head()


# In[29]:


# iterates here no problem to find lowest stock value after COVID and its date
for i in df:
    print(df[i].loc[df[i] >= df[i].min()])


# In[22]:


# Finds previous max stock value, before crash
df2 = df.loc[:"2020-04-01"]
for i in df2:
    print(df2[i].loc[df2[i] == df2[i].max()])


# In[51]:


# Returns the the number of periods before returning to previous high
df3 = df.loc["2020-04-01":]
for i in df3:
    print(np.count_nonzero(df3[i].loc[df3[i] <= df2[i].max()]))


# In[ ]:





# In[ ]:





# In[ ]:




