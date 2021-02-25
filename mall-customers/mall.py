import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib as plt

data = pd.read_csv("Mall_Customers.csv")
data.rename(columns={'Genre': 'Gender'}, inplace=True)

# Encoding Gender column
data['Gender'] = data['Gender'].astype('category')
data['Gender_cat'] = data['Gender'].cat.codes # 1 = male, 0 = female
gender = data['Gender_cat']
gender = pd.DataFrame(gender)

normed = preprocessing.normalize(data[['Annual Income (k$)', 'Age', 'Spending Score (1-100)']])
normed = pd.DataFrame(normed)
normed.columns = ['income', 'age', 'spending']

df = normed.merge(gender, how='inner', left_index=True, right_index=True)

