import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
print(excel_file)

# print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")



# adding a column to existing table
dataframe["unknown_id"]=dataframe['Age']+dataframe["Id"]
print(dataframe)
print("----------------b-----")
print(dataframe[1:5])



# then the original dataframe was updated by one column

# we can drop the column


print(dataframe.drop(columns="unknown_id"))
print(dataframe)
print("----------------b-----")

# then its give the deleted column but its not effected by origin 


# we can effect this change in original then assign to original dataframe


dataframe=dataframe.drop(columns="unknown_id")
print(dataframe)



print(dataframe["Age"])