
#! What is Model Validation

# *  if a house cost $150,000 and you predicted
# * it would cost $100,000 the error is $50,000.

# * There are many metrics for summarizing model quality,
# * but we'll start with one called
# * Mean Absolute Error(also called MAE)

# ?To calculate MAE, we first need a model.
# ?That is built in a hidden cell below, which you can review
# ?by clicking the code button.

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
path = '../melb_data.csv'
m_data = pd.read_csv(path)
m_data = m_data.dropna(axis=0)
y = m_data.Price
m_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# ? By convention, 'm_features' is called 'X'
X = m_data[m_features]

# ? Define model.
model = DecisionTreeRegressor()

# ?Fit(Training) model
print(model.fit(X, y))

predicted_home_prices = model.predict(X)
a = mean_absolute_error(y, predicted_home_prices)

print(a)
