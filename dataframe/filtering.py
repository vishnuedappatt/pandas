import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
# print(excel_file)
dataframe=pd.DataFrame(excel_file)
print(f"-------{dataframe}-------------")

print(dataframe[dataframe['Age']<25])

print("----------------------")
print(dataframe.loc[dataframe["Age"]<25])


print("------------------")
print(dataframe.loc[(dataframe["Age"]>25) & (dataframe["Country"] =="United States")])


print("------------------")
print(dataframe.loc[(dataframe["Age"]>25) |  (dataframe["Country"] !="United States")])



print("-------------------------")
print(dataframe["First Name"].str.contains("Mara"))   # get true or false



print(dataframe.loc[dataframe["First Name"].str.contains("Mara")])

print("----------------df-----")


print(dataframe.loc[~dataframe["First Name"].str.contains("Mara")].head(2))    #not name mara using ~

print("0-----------33333")

print(dataframe.loc[dataframe["First Name"].str.startswith("Mara")])

# str.endswith
