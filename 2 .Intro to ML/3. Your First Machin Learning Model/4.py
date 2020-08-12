
#! Build Your Model
# * you will use the scikit-learn library to create your models.
# * When coding, this library is written as 'sklearn', as you will see in the
# * sample code.


# * The steps to building and using a model are:
# ? Define: What type of model will it be? A decision tree? Some other type
# ? of model? Some other parameters of the model type are specified too.

# ? Fit: Capture patterns from provided data. This is the heart of modeling

# ? Predict:Just what it sounds like

# ? Evaluate:Determine how accurate the model's predictions are.


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


# //===================================

# * many machine learning models allow some randomness in model training.
# * specifying a number for "random_state" eunsures you get the same results in each run.
# * This is considerd a good practice. You use any number, and model quality won't depend meaningfully on exactly what value you choose

# ? Now we can use to make predictions.

print(model.predict(X.head()))f
