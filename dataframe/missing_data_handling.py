import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/missing.xls")
# print(excel_file)

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")
print(dataframe.dropna())

# its not effected by original

# print(dataframe)  




# ************ this 2 way we can effected by original dataframe **********

dataframe=dataframe.dropna()
print(dataframe)

# OR

print(dataframe.dropna(inplace=True))

print("------------------------")

# print(dataframe[dataframe["Age"]==36])


#/--------------------------------

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/missing.xls")
# print(excel_file)

dataframe=pd.DataFrame(excel_file)

# we can also get the column with no null value
print(dataframe["Age"])  # original [ with null ]
print(dataframe["Age"].dropna())   #copy [ withou null ]


print("------------------------------------")


print(dataframe.fillna("nill"))


print(dataframe["Age"].mean())
import math
math.floor

print(dataframe["Age"].fillna(dataframe["Age"].mean()))

print(dataframe["Age"].fillna(math.floor(dataframe["Age"].mean()),inplace=True))


print(dataframe)