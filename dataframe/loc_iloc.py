import pandas as pd



# LOC

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
print(excel_file)

print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")

print(dataframe.loc[2])   # get the 2 index row

print("----------------")
print(dataframe.loc[2,"First Name"])    #then get the 2 index first name only


print("----------------")
print(dataframe.loc[0:4,["First Name","Age"]])    #then get the 0-4 index first name only



print("----------------")
print(dataframe.loc[0:4,"First Name":"Gender"])    #then get the 0-4 index first name only




# ILOC

# it is index selecting column  method and loc is label based column selection


print("--------------------------")
print(dataframe.iloc[2,4])


# in iloc consider as indexes then get [1:3] in iloc then 1-2 indexes only and in the same think in loc then get 1-3 indexes

print(dataframe.loc[1:3])  
print(dataframe.iloc[1:3])

print("------------------------")
print(dataframe.loc[[1,7]])


