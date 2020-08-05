
#! Choosing "Features"
# *The columns that are inputted into our model are called
# * "Features". In our case, those would be the columns used to
# * determin the home price

import pandas as pd
path = '../melb_data.csv'
m_data = pd.read_csv(path)
m_data = m_data.dropna(axis=0)
Y = m_data.Price
m_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# ? By convention, 'm_features' is called 'X'
X = m_data[m_features]

print(X.describe())
print(X.head())
