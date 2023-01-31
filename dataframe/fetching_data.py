
import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
# print(excel_file)

print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe.head())   # get first 5 row inlyy

print("--------------------")

print(dataframe.head(2))    # get  first 2 row only 



dataframe=pd.DataFrame(excel_file)
print(dataframe.tail())   # get last 5 row inlyy

print("--------------------")

print(dataframe.tail(2))    # get last 2 row only 



# describe
print("======================")
describe=dataframe.describe()
print(describe)

print("-----------------")

# getting column
column=dataframe.columns
print(column)


# shape
print(dataframe.shape)


# geting some column
print(dataframe[["Age","Gender"]].head())

print("_--------------")
# slicing
print(dataframe[2:4])




# get single row


print("----------------------")
print(dataframe.loc[1])



# searching
print("------------------------------")
search_data=dataframe.loc[dataframe["Age"]==36]
print(search_data)


print('-----------:7:-----------')
search_data=dataframe.loc[dataframe["Age"]==90]
print(search_data)

