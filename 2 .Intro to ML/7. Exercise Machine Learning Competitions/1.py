import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# Path of the file to read. We changed the directory structure to simplify submitting to a competition
iowa_file_path = '../melb_data.csv'

home_data = pd.read_csv(iowa_file_path)
features = ['Rooms', 'Type']
print(home_data[features])
