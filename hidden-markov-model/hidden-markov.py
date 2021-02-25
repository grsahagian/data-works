import pandas as pd
import numpy as np
from pandas_ml_quant import pd, np
import warnings
import pickle
from hmmlearn.hmm import GaussianHMM
from hmmlearn import hmm
from sklearn.model_selection import train_test_split
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import seaborn as sns

date_since = '1995-01-01'
date_until = '2020-12-30'

raw = pd.fetch_yahoo('SPY').loc[date_since:date_until]
# print(raw.tail())

df = pd.DataFrame()
df['Returns'] = raw['Close'].pct_change().dropna()
df['Close'] = raw['Close']
df.set_index(df.columns[0]).dropna()

# print(df.head())

# https://www.quantstart.com/articles/market-regime-detection-using-hidden-markov-models-in-qstrader/#:~:text=Hidden%20Markov%20Models%20are%20a,that%20are%20not%20directly%20observable.&text=Fitting%20a%20Hidden%20Markov%20Model,risk%20management%20trading%20filter%20mechanis


# https://towardsdatascience.com/when-to-buy-the-dip-e2e128d737a7

x_train, x_test = train_test_split(df, test_size=0.2, train_size=0.8)
# x_train.set_index(x_train.columns[0])
x_train.index.names = ['Date']
# x_test.set_index(x_test.columns[0])
x_test.index.names = ['Date']
# print(x_train.head())


# Hidden Markov Model with Gaussian emissions.
model = hmm.GaussianHMM(n_components=3, covariance_type="full",
                        init_params="cm", params="cmt").fit(x_train)

# Find most probable state sequence corresponding to x
hidden_states = model.predict(x_test)


# print("Means and vars of each hidden state")
# for i in range(model.n_components):
#     print("{0}th hidden state".format(i))
#     print("mean = ", model.means_[i])
#     print("var = ", np.diag(model.covars_[i]))
#     print()


model2 = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=100)
model2.fit(x_train)


# hidden_states2 = model2.predict(x_test)


model3 = hmm.GaussianHMM(n_components=2, covariance_type="spherical", n_iter=100)
model3.fit(x_train)


# hidden_states3 = model3.predict(x_test)

model4 = hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=100)
model4.fit(x_train)

model5 = hmm.GaussianHMM(n_components=2, covariance_type="tied", n_iter=100)
model5.fit(x_train)


# .decode produces 1) logprob of the produced state-sequence and 2) said state-sequence
print(model.decode(x_test))
print(model2.decode(x_test))
print(model3.decode(x_test))
print(model4.decode(x_test))
print(model5.decode(x_test))



# sns.set(font_scale=0.1)
# states = (pd.DataFrame(hidden_states, columns=['states'], index=x_test.index)
#           .join(x_test, how='inner')
#           .reset_index(drop=False)
#           .rename(columns={'index':'Date'}))
# # print(states.head())
#
# colors = cm.rainbow(np.linspace(0, 1, model.n_components))
# order = [0, 1, 2]
# fg = sns.FacetGrid(data=states, hue='states', hue_order=order,
#                    palette=colors, aspect=1.5, height=12)
# fg.map(plt.scatter, 'Date', 'Close', alpha=0.5).add_legend()
# sns.despine(offset=10)
# fg.fig.suptitle('Historical SPY Regimes', fontsize=24, fontweight='demi')
# plt.show()






