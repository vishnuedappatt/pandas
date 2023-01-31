import pandas as pd
import numpy as np

# empty series
s=pd.Series()
print(s)

# give array
array=np.array([1,2,3,4])
s=pd.Series(array)
print(s)

print("---------------")

#give list
list=[1,3,4,5]
s=pd.Series(list)
print(s)

print("---------------")

# Dictionary                        # here no index value is came because the key act as a index and unable to given the index argunment there
dict={'a':1,"b":2,"c":3}
s=pd.Series(dict)
print(s)

print("----------------")

# List of tuples
tuple=[("a",10),("b",3),("c",7)]
s=pd.Series(tuple)
print(s)