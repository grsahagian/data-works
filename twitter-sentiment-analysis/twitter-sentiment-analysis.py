#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import math
from itertools import product
import datetime as dt


# In[3]:


from platform import python_version

print(python_version())


# In[ ]:





# In[4]:


#maxTweets = 100000

#keyword = 'Pfizer'

#Open/create a file to append data to
#csvFile = open('pfe_tweets_result.csv', 'a', newline='', encoding='utf8')

#Use csv writer
#csvWriter = csv.writer(csvFile)
#csvWriter.writerow(['id','date','tweet',]) 


#for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:2020-01-01 until:2020-10-30 -filter:links -filter:replies').get_items()):
#        if i > maxTweets :
#            break  
#        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
#csvFile.close()


# In[5]:


analyzer = SentimentIntensityAnalyzer()


# In[6]:


def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    # return(score['compound']) #prints only compound score
    return("{:-<40} {}".format(sentence, str(score)))


print(sentiment_analyzer_scores("PFE sucks!"))


# In[7]:


df = pd.read_csv('/Users/Graham/data-works/twitter-sentiment-analysis/pfe_tweets_result.csv')
df = df.set_index('date')


# In[ ]:





# In[8]:


df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['tweet']] 
df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['tweet']]
df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['tweet']]
df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['tweet']]
# df['c_SMA'] = df['compound'].rolling(100).mean()


# In[9]:


df.tail()


# In[10]:


print(np.average(df['compound']))
print(np.average(df['neg']))
print(np.average(df['neu']))
print(np.average(df['pos']))


# In[11]:


#plt.figure(figsize=(20,20))
#plt.xlabel('Date')
#plt.ylabel('Compound Simple MA')
#plt.plot(df['c_SMA'])


# In[12]:


df.index = pd.to_datetime(df.index, errors='coerce',format='%Y-%m-%d %H:%M:%S')


# In[13]:


df = df.resample('D').mean()


# In[14]:


# Make data index timezone naive
df.tz_localize(None)


# In[15]:


# Removing Weekends from daily tweet sentiment dataframe
df = df.loc[df.index.to_series().dt.weekday < 5]


# In[16]:


# No weekends sentiment data to CSV file
df.to_csv('tweets_resampled_mean_no_weekends.csv')


# In[17]:


# Combining the PFE ticker frame and the tweet sentiment resampled frame

# ** had to manually alter the date column title to --> 'Date' and remove hour/s/m data 
corrected_df = pd.read_csv("/Users/Graham/data-works/twitter-sentiment-analysis/tweets_no_wks_corrected.csv", parse_dates=True, index_col=0)
_pfe = pd.read_csv("/Users/Graham/data-works/twitter-sentiment-analysis/PFE.csv", parse_dates=True, index_col=0)
combined_df = corrected_df.merge(_pfe, on='Date',how='outer').dropna()


# In[18]:


combined_df.head()


# In[ ]:





# In[19]:


#_pfe['Returns'] = np.log(_pfe['Close'] / _pfe['Close'].shift(1))
#_pfe = _pfe.dropna()
#_pfe.tz_localize(None)
#pfe = _pfe['Close']
#pfe.to_frame()



# In[20]:


# Calculating Log Returns Column
combined_df['returns'] = np.log(combined_df['Close'] / combined_df['Close'].shift(1))
# Long when the sentiment[pos > neg] and short otherwise
combined_df['position'] = np.where(combined_df['pos'] > combined_df['neg'], 1, -1)
# Create Strategy column & by multiplying SHIFTED position to avoid hindsight bias
combined_df['strategy'] = combined_df['position'].shift(1) * combined_df['returns']
combined_df.dropna(inplace=True)


# In[21]:


combined_df.head()


# In[22]:


# checking to see if the strategy outperforms the returns benchmark over the period
np.exp(combined_df[['returns','strategy']].sum())


# In[23]:


combined_df.head()


# In[24]:


import matplotlib.dates as mdates


# In[29]:


retl = combined_df['returns'].cumsum()
stratl = combined_df['strategy'].cumsum()
pnn = combined_df['pos'] - combined_df['neg']
plt.figure(figsize=(20,16))
plt.style.use('seaborn')
plt.plot(retl, linestyle=':', label='Return Benchmark')
plt.plot(stratl, label='Strategy')
plt.plot(pnn, linestyle='-',label='Sentiment Line')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='upper right')

# plt.savefig('strategy-v-benchmark.png')


# In[ ]:





# In[ ]:





# In[ ]:




