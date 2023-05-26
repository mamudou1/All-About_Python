import numpy as np
import pandas as pd 

#print(pd.__version__)

my_label= ["x", "y","z"]
my_data=[100,200,300]
#print(pd.Series(data=my_data))
#print(pd.Series(data=my_data, index=mylabel))
"""
# Let's create NumPy array from my_data and then Series from that array 
my_array = np.array(my_data) # creating numpy's array from list 
series = pd.Series(data = my_array) # creating Series from numpy's array
print(series)
"""

# Let's pass my_labels (which is a list of strings) as data now! 
print(pd.Series(data = my_label)) # passing list for strings as data

# We can pass a list of built-in functions!
print(pd.Series([min, max, sum, print]))