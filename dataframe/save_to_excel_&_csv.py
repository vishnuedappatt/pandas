import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")

dataframe["age_id"]=dataframe["Age"]+dataframe["Id"]

print(dataframe)


# for saving the updated excel use to_excel


dataframe.to_excel("/home/vishnupe@genproresearch.net/Downloads/updated_sample.xls")    # in this index is presented


dataframe.to_excel("/home/vishnupe@genproresearch.net/Downloads/updated_sample.xls",index=False)   # we can avoid index using index=False


# also covert to csv file 


dataframe.to_csv("/home/vishnupe@genproresearch.net/Downloads/updated_sample.csv") 


# also convert to text formate

dataframe.to_csv("/home/vishnupe@genproresearch.net/Downloads/updated_sample.txt",sep="\t") 