
import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/duplicate.xls")
# print(excel_file)
# print(excel_file)
print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print(dataframe.duplicated())  #find the duplicates

print(dataframe.drop_duplicates())   # remove the duplicate not effect original
print(dataframe)
print(dataframe.drop_duplicates(inplace=True))
print(dataframe)

