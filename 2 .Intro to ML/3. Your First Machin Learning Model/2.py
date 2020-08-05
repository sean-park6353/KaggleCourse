
#! Selecting The Prediction Target
# * single column i stored in a 'Series', which is broadly
# * like a 'DataFrame' with only a single column of data

# * We will use the dot notation to select the column we want to predict,
# * which is called the 'prediction target'

# * prediction target is called 'y'
import pandas as pd
path = '../melb_data.csv'
m_data = pd.read_csv(path)
m_data = m_data.dropna(axis=0)
y = m_data.Price
print(y)
