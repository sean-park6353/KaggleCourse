
#! The Problem with "In-Sample" Scores

# ? Since models' practical value come from making
# ? predictions on new data, we measure performance
# ? on data that wasn't used to build the model.
# ? The most straightforward way to do this is to exclude
# ? some data from the model-building process,
# ? and then use those to test the model's accuracy
# ? on data it hasn't seen before.
# ? This data is called validation data.

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
path = '../melb_data.csv'
m_data = pd.read_csv(path)
m_data = m_data.dropna(axis=0)
m_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = m_data[m_features]
y = m_data.Price
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


# ? Your mean absolute error for the in-sample data was about 1100 dollars.
# ?  Out-of-sample it is more than 250,000 dollars.
# ? This is the difference between a model that is
# ? almost exactly right,
# ? and one that is unusable for most practical purposes.
# ? As a point of reference,
# ? the average home value in the validation data is
# ? 1.1 million dollars. So the error in new data
# ? is about a quarter of the average home value.
