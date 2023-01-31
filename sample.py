import pandas as pd

list=[1,2,3,5,6]

series=pd.Series(list)
print(series)

print("--------------------------------")


# default index is starting with 0-etc
# we can also change the index using index keyword


series=pd.Series(list,index=[1,1,1,1,1])
print(series)


print("--------------------------------")

# DATAFRAME

dict={"name":["anu","viz","child1","child2"],"age":[29,35,4,1]}

dataFrame=pd.DataFrame(dict)
print(dataFrame)

dataFrame=pd.DataFrame(list)
print(dataFrame)