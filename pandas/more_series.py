import pandas as pd
# Creating three dictionaries dict_1, dict_2, dict_3
dict_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_2 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_3 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700, 'Jasper':1000}

# Creating Pandas Series from the dictionaries
ser1 = pd.Series(dict_1)
ser2 = pd.Series(dict_2)
ser3 = pd.Series(dict_3)

#print(ser1["Calgary"])
#print(ser1+ser2)
ser4 = ser1 + ser2 
# pd.isnull(ser4) is same as ser4.isnull()
print(ser4.isnull())


print("Head : ",ser1.head(1)) # head(1) will return the first row only
print("Tail : ",ser1.tail(1)) # tail(1) will return the last row only

# row axis labels (index) list can be obtained
print("Axis : ", ser1.axes)

# returns the values/data
print("Values : ", ser1.values)

print("Size : ", ser1.size)

# True for empty Series
print("Is Empty ? ",ser1.empty)