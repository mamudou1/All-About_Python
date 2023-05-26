import numpy as np 
array_2d = np.zeros((5,5)) # Create a zero matrix
array_2d.shape[1] # Using shape attribute, get the number to run the loop
for i in range(array_2d.shape[1]): # Using range() in the loop
  array_2d[i] = i
print( array_2d ) # Print/output the matrix

print(array_2d[[1,2,3]]) 