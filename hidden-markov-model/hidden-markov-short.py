import pandas as pd
import numpy as np
from hmmlearn.hmm import GaussianHMM
from hmmlearn import hmm
from pandas_ml_quant import pd, np
from sklearn.model_selection import train_test_split
import yfinance as yf
from sklearn.model_selection import train_test_split
import seaborn as sns
from matplotlib import cm, pyplot as plt
import talib
from talib import MA_Type




_asml = yf.Ticker("ASML")
info = _asml.info
# for key in info:
#     print(key, '->',  info[key])

# Data Download
raw = yf.download(tickers="ASML", period="2mo",interval="60m",)


raw['Returns'] = raw['Adj Close'].pct_change()
raw = raw.dropna()
raw = raw.drop(columns=['Open', 'High','Low','Close'])
# print(raw.head())

# partitioning data into training and test set
x_train, x_test = train_test_split(raw, test_size=0.2, train_size=0.8)


# HMM model with Gaussian emissions
model = hmm.GaussianHMM(n_components=2, covariance_type="full",
                        init_params="cm", params="cmt")
model.fit(x_train)

# Find the most likely state sequence corresponding to x
states = model.predict(x_train)

# Compute the log probability under the model
score = model.score(x_train)

# print(states.shape)
# print(x_train.shape)




# matrix of transition probabilities between hidden states
# for i in range(model.n_components):
#     print(model.transmat_[i])



# New Dataframe with Hidden States as an additional feature
df = x_train
df['States'] = states


# Bollinger Bands
upper, middle, lower = talib.BBANDS(df['Adj Close'], matype=MA_Type.T3)

# MACD
macd, macdsignal, macdhist = talib.MACD(df['Adj Close'], fastperiod=12, slowperiod=26, signalperiod=9)

df['MACD'] = macd
df['MACD Signal'] = macdsignal
df['BBands Middle'] = middle
df.rename(columns={"Adj Close" : "Close"}, inplace=True)


df = df.dropna()
print(df.index)



strat_returns = []
# for i in df:
#     if df['States'][i] == 0:   # 0th hidden state
#         if df['MACD'][i] > df['MACD Signal'][i]:
#             strat_returns.append(df['Close'][i])
#         else:
#             strat_returns.append(0)
#     if df['States'][i] == 1:  # 1th hidden state
#         if df['Close'][i] < df['BBands Middle'][i]:
#             strat_returns.append(df['Close'][i])
#         else:
#             strat_returns.append(0)
#     else:
#         strat_returns.append(0)
# print(strat_returns)


































