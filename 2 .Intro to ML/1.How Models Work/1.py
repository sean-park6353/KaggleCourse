import pandas as pd

m_data = pd.read_csv('./melb_data.csv')
print(m_data.describe())
# ? 'count' shows how many rows have non-missing values.
# ? 'mean' is the average
# ? 'std' is standard deviation, which measure how numerically spread out the value are.
# ? 'min','25%','50%','75%','max'
# ?  imagine sorting each column from lowest to highest value
