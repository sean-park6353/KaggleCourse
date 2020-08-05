
#! Selecting Data for Modeling
# * Your dataset had too many variables to wrap your head around, or even to print out nicely. How can you pare down this overwhelming amount of data to something you can understand?
# * We'll start by picking a few variables using our intuition. Later courses will show you statistical techniques to automatically prioritize variables.
# * To choose variables/columns, we'll need to see a list of all columns in the dataset. That is done with the columns property of the DataFrame(the bottom line of code below).

import pandas as pd
path = '../melb_data.csv'
m_data = pd.read_csv(path)

print(m_data)
