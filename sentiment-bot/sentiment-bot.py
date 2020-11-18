#!/usr/bin/env python
# coding: utf-8

# In[1]:

#     User Input: Keyword -->
# Generates (1) number of tweets since start of previous day
#           (2) average sentiment scores
#           (3) timer


# In[26]:


import pandas as pd
import numpy as np
import csv
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime as dt
import time



# In[27]:


# Timing our app
from timeit import default_timer as timer

# START MY TIMER
start = timer()


# In[28]:


# Generating datetime objects
from datetime import datetime, timedelta
now = datetime.now()
now = now.strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(days = 1)
yesterday = yesterday.strftime('%Y-%m-%d')


# In[29]:


# Using Python 3.8
from platform import python_version
#print(python_version())


# In[30]:


keyword = input('Enter a topic or keyword, please:')


# In[31]:


maxTweets = 80000


#Open/create a file to append data to
csvFile = open(keyword +'-sentiment-' + now + '.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet',])


for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:' +  yesterday + ' until:' + now + ' -filter:links -filter:replies').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()



df = pd.read_csv('/Users/Graham/data-works/sentiment-bot/'+ keyword +'-sentiment-' + now + '.csv', parse_dates=True, index_col=0)


# In[34]:


analyzer = SentimentIntensityAnalyzer()


# In[35]:


df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['tweet']]
df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['tweet']]
df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['tweet']]
df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['tweet']]


# In[55]:


avg_compound = np.average(df['compound'])
avg_neg = np.average(df['neg']) * -1  # Change neg value to negative number for clarity
avg_neu = np.average(df['neu'])
avg_pos = np.average(df['pos'])


# In[56]:


count = len(df.index)


# In[57]:


print("Since yesterday there has been", count ,  "tweets on " + keyword, end='\n*')
print("Positive Sentiment:", '%.2f' % avg_pos, end='\n*')
print("Neutral Sentiment:", '%.2f' % avg_neu, end='\n*')
print("Negative Sentiment:", '%.2f' % avg_neg, end='\n*')
print("Compound Sentiment:", '%.2f' % avg_compound, end='\n')


# In[44]:


# STOP MY TIMER
elapsed_time = (timer() - start) / 60 # in seconds
print("Program Executed in", '%.2f' % elapsed_time, "minutes")


# In[ ]:





# In[ ]:
