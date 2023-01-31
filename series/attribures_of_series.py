import pandas as pd

s=pd.Series([1,3,4,5,6],name="integers")

print(s)
print("--------------------")
print(s.index)   # get the indexs
print("--------------------")
print(s.array)   # get array
print("--------------------")
print(s.values)  # get values of series
print("--------------------")
print(s.dtype)   # get the type of series
print("--------------------")
print(s.shape)    # get the shape of the series
print("--------------------")
print(s.ndim)     # get the diamentions of the series
print("--------------------")
print(s.memory_usage())  # get the memory usage of the index and values
print("--------------------")
print(s.nbytes)     # get the memory usage of values
