import numpy as np

array_id= np.array([-10,-2,0,17,107,200])
#this is a different way of calling an arrays/splicing
#print(array_id[0])
#print(array_id[-2])
#print(array_id[:3])

#now to replace a value 
array_id[2]=200
#print(array_id)

# to get array size 
#print(array_id.size)


array_2d= np.arange(24) # creating 1D array using arange() 
array_2d.shape = (6,4) # converting into 2D
print(array_2d) # How the 2D array look like!
print(array_2d[5,2])
print(array_2d[5][2])



# array_2d[0:2,0:2] is same as array_2d[:2,:2]
print(array_2d[:2,:2])

# getting inner slice
print(array_2d[2:4,2:4])