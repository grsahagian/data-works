import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn import preprocessing

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = pd.read_csv("housing-data-project/housing.csv", header=None, delimiter=r"\s+", names=column_names)

# CRIM - per capita crime rate by town
# ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
# INDUS - proportion of non-retail business acres per town.
# CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
# NOX - nitric oxides concentration (parts per 10 million)
# RM - average number of rooms per dwelling
# AGE - proportion of owner-occupied units built prior to 1940
# DIS - weighted distances to five Boston employment centres
# RAD - index of accessibility to radial highways
# TAX - full-value property-tax rate per $10,000
# PTRATIO - pupil-teacher ratio by town
# B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# LSTAT - % lower status of the population
# MEDV - Median value of owner-occupied homes in $1000's

#for x in column_names:
#    print(data[x].describe())

# Visualizing Data Distribution of Individual Features
# fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 12))
# index = 0
# axs = axs.flatten()
# for k,v in data.items():
#     sns.boxplot(v, ax=axs[index])
#     index += 1
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
# plt.show()

# Scaling columns before plotting them against MEDV (Median Home Value)
scaler = preprocessing.MinMaxScaler()
column_sels = ['LSTAT', 'INDUS', 'NOX', 'PTRATIO', 'RM', 'TAX', 'DIS', 'AGE', 'B']
# selecting values of all columns except MEDV
x = data.loc[:, column_sels]
# setting MEDV as Y to plot columns against
y = data['MEDV']
# Normalizing features (x-values)
x = pd.DataFrame(data=scaler.fit_transform(x), columns=column_sels)



# Plotting the relationship between each feature and MEDV
# fig, axs = plt.subplots(ncols= 5, nrows= 2, figsize=(10,6))
# axs = axs.flatten()
# for i, k in enumerate(column_sels):
#     sns.regplot(y=y, x=x[k], ax=axs[i], color='slateblue')
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
# plt.show()

# Removing skewness of data through log transformation
#  using log1p because normalized data falls between 0 and 1
y = np.log1p(y)

# if skew is greater than 0.3 then log transform
for col in x.columns:
    if np.abs(x[col].skew()) > 0.3:
        x[col] =  np.log1p(x[col])

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

x_scaled = scaler.fit_transform(x)
kf = KFold(n_splits=10)

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
# grid_sv = GridSearchCV(svr_rbf, cv=kf, param_grid={"C": [1e0, 1e1, 1e2, 1e3], "gamma": np.logspace(-2, 2, 5)}, scoring='neg_mean_squared_error')
# grid_sv.fit(x_scaled, y)
# print("Best classifier :", grid_sv.best_estimator_)


scores = cross_val_score(svr_rbf, x_scaled, y, cv=kf, scoring='neg_mean_squared_error')
scores_map = {}
scores_map['SVR'] = scores
print("MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))

# Gradient Boosting Regressor
from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor(alpha=0.9,learning_rate=0.05, max_depth=2, min_samples_leaf=3, min_samples_split=2, n_estimators=200, random_state=42)
# param_grid={'n_estimators':[100, 200], 'learning_rate': [0.1,0.05,0.02], 'max_depth':[2, 4,6], 'min_samples_leaf':[3,5,9]}
# grid_sv = GridSearchCV(gbr, cv=kf, param_grid=param_grid, scoring='neg_mean_squared_error')
# grid_sv.fit(x_scaled, y)
# print("Best classifier :", grid_sv.best_estimator_)

scores = cross_val_score(gbr, x_scaled, y, cv=kf, scoring='neg_mean_squared_error')
scores_map['GradientBoostingRegressor'] = scores
print("MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))



# Decision Tree
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(max_depth=2, random_state=42)
# grid_sv = GridSearchCV(dtr, cv=kf, param_grid={"max_depth" : [1, 2, 3, 4, 5, 6, 7]}, scoring='neg_mean_squared_error')
# grid_sv.fit(x_scaled, y)
# print("Best classifier :", grid_sv.best_estimator_)

scores = cross_val_score(dtr, x_scaled, y, cv=kf, scoring='neg_mean_squared_error')
scores_map['DecisionTreeRegressor'] = scores
print("MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))


# XB Boost --> https://www.kaggle.com/jayatou/xgbregressor-with-gridsearchcv
from xgboost.sklearn import XGBRegressor

xgb = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=0.7, gamma=0, gpu_id=-1,
             importance_type='gain', interaction_constraints='',
             learning_rate=0.03, max_delta_step=0, max_depth=7,
             min_child_weight=4, monotone_constraints='()',
             n_estimators=500, n_jobs=4, nthread=4, num_parallel_tree=1,
             random_state=0, reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
             subsample=0.7, tree_method='exact', validate_parameters=1,
             verbosity=None)

params = {'nthread':[4], #when use hyperthread, xgboost may become slower
              'objective':['reg:squarederror'],
              'learning_rate': [.03, 0.05, .07], #so called `eta` value
              'max_depth': [5, 6, 7],
              'min_child_weight': [4],
              'subsample': [0.7],
              'colsample_bytree': [0.7],
              'n_estimators': [500]}

# grid_sv = GridSearchCV(xgb,
#                         params,
#                         cv = kf,
#                         n_jobs = 5,
#                         verbose=True)
# grid_sv.fit(x_scaled, y)
# print("Best classifier :", grid_sv.best_estimator_)

scores = cross_val_score(xgb, x_scaled, y, cv=kf, scoring='neg_mean_squared_error')
scores_map['XGB Regressor'] = scores
print("MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))


# Box Plots Visualizing ML Results

# plt.figure(figsize=(10,8))
# scores_map = pd.DataFrame(scores_map)
# sns.boxplot(data=scores_map)
# plt.show()


# Visualizing ML results with Shapley
import shap

# load JS visualization code to notebook
shap.initjs()

# Fit Model
xgb.fit(x_scaled, y)


explainer = shap.TreeExplainer(xgb)
shap_values = explainer.shap_values(x_scaled)

x_scaled = pd.DataFrame(x_scaled)

# Weird output makes it impossible to read the graph
i = 5
shapforce = shap.force_plot(explainer.expected_value,
                            shap_values[i], features=x_scaled.iloc[i], feature_names=column_sels, matplotlib=True)

# Summary plot
# x-axis shows the magnitude of the impact on the model (median house price)
# y-axis ranks the features by importance --> importance is measured as average absolute Shapley value
# color shows the magnitude of the feature
#
# https://poseidon01.ssrn.com/delivery.php?ID=930086105106028113016014066005099029046084048036031020026004116111020030024096112023032062030033112029051075101024004104089017110061008028038089116117112114102010030058087084094000089121111111029001120081000118089080126005087096067005098011003002082&EXT=pdf&INDEX=TRUE
#
# shap.summary_plot(shap_values, features=x_scaled, feature_names=column_sels)























