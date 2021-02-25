#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytrends.request import TrendReq
import pandas as pd
import time
from talib import BBANDS, MACD
from pandas_ml_quant import pd, np
from sklearn.model_selection import train_test_split


# In[2]:


startTime = time.time()
pytrend = TrendReq(hl='en-GB', tz=360)

# https://www.honchosearch.com/blog/seo/how-to-use-python-pytrends-to-automate-google-trends-data/

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("Keywords")

dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2017-11-01 2020-11-01',
     geo='GB')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_trends.csv')

executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))


# In[3]:


result.resample('D').ffill()


# In[4]:


google = result['Bitcoin'].resample('D').ffill()
google = google.to_frame()
google.head()


# In[5]:


date_from = '2017-11-04'
date_until = '2020-11-01'


# In[6]:


raw = pd.fetch_yahoo("BTC-USD").loc[date_from:date_until]
close = raw['Close']


# In[7]:


# Bollinger Bands Initialization
up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)


# In[8]:


# MACD Initialization
macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)


# In[ ]:





# In[9]:


cols = [['Close','Trends', 'BB:UpBand', 'BB:mid', 'BB:LowBand', 'MACD', 'MACD-Signal', 'MACD-Hist']]
df = pd.concat([close, google, up, mid, low, macd, macdsignal, macdhist ],join='inner', axis=1).dropna()
df.columns = cols
df.index.names = ['Date']


# In[10]:


# Create Month, Day Column -- Year isnt helpful as a feature
df['Day'] = df.index.day


# In[11]:


df['Month'] = df.index.month


# In[12]:


df['Year'] = df.index.year


# In[ ]:





# In[13]:


# Create targets (labels)
labels = raw['Close'].loc['2017-12-07':'2020-11-01']


# In[14]:


# Dropping labels from features
df= df.drop('Close', axis = 1)


# In[15]:


feature_list = list(df.columns)


# In[16]:


features = np.array(df)


# In[17]:


# Split data into training and testing sets
# https://towardsdatascience.com/machine-learning-with-datetime-feature-engineering-predicting-healthcare-appointment-no-shows-5e4ca3a85f96
#
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)


# In[18]:


print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)


# In[19]:


# The baseline predictions based off 10-day rolling average
baseline_preds = raw['Close'].loc['2017-12-07':'2020-11-01'].rolling(window=10).mean()
# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))


# In[20]:


from sklearn.ensemble import RandomForestRegressor
# Instantiate Model with 1000 trees
rf = RandomForestRegressor(n_estimators = 1000, random_state=42)


# In[21]:


# Train Model on Training Data
rf.fit(train_features, train_labels);


# In[22]:


# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')


# In[23]:


# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


# In[24]:


# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot


# In[25]:


# Visualizing a Decision Tree
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Pull out one tree from the forest
tree = rf.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)


# In[26]:


# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree.dot')
# Write graph to a png file
graph.write_png('tree.png')


# In[27]:


# FEATURE IMPORTANCE 


# In[28]:


# Get numerical feature importances
importances = list(rf.feature_importances_)


# In[29]:


# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]


# In[30]:


# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)


# In[31]:


print(feature_importances)


# In[32]:


# Create a new forest with only most important variables
rf_most_important = RandomForestRegressor(n_estimators=1000, random_state=42)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




