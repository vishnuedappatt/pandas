# Load data from excel file
# Load data from csv file
# Load data from list of tuple ,dictionary


import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
print(excel_file)

print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")


csv_file=pd.read_csv("/home/vishnupe@genproresearch.net/Downloads/cities.csv")
print(csv_file)

dataframe=pd.DataFrame(csv_file)
print(dataframe)

print("--------------------")


# using dictionary
dict={"name":["anu","aa","vv","vishnu"],"age":[11,23,4,55]}
dataframe=pd.DataFrame(dict)
print(dataframe)
