import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")
print(excel_file)

# print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")

print(dataframe.sort_values("First Name",ascending=False))

print("--------------------")

print(dataframe.sort_values(["First Name","Age"],ascending=False))
