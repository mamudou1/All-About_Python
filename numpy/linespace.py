import numpy as np

#give you the interval you need 
print(np.arange(0,10,4))

#give actual spacing
print(np.linspace(1,4,5))

# Creating 2-D array, (no_row, no_col) passing a tuple
print( np.zeros((4,6)) )

#Creating 2-D array, (no_row, no_col) passing a tuple
print( np.ones((4,6)) )

#diagonal matrix with ones
print(np.eye(5))

# row, col, note we are not passing a tuple here
# each dimension (num_of_rows, num_of_columns) is a separate argument 
print(np.random.rand(3,2))

# 1-D array of two elements.
print( np.random.randn(2) )

# 2-D array (4x4), 16 elements.
# no tuple, each dimension as a separate argument
print( np.random.randn(4,4) )

#returns ten random int,
print( np.random.randint(1,100,10) )
