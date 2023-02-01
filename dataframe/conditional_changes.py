import pandas as pd

excel_file=pd.read_excel("/home/vishnupe@genproresearch.net/Downloads/sample.xls")

print("--------------------")

dataframe=pd.DataFrame(excel_file)
print(dataframe)

print("--------------------")


dataframe["score"]=None
print(dataframe)



# data=dataframe["Id"]/dataframe["Age"]
# print(dataframe)
dataframe["score"]=dataframe["Id"]/dataframe["Age"]
dataframe["score"]=dataframe["score"].astype(int)
print(dataframe)

# l1=list(data)
# l2=[int(x) for x in l1]

# dataframe["score"]=l2
dataframe["Grade"]=None
print(dataframe)
print("-----------------------")
dataframe.loc[dataframe["score"]<50 ,["Grade"]]="Potty"
print(dataframe["score"].astype(int))


print("--------------------------------------------")

dataframe.loc[(dataframe["score"]>50) & (dataframe["score"]<75),["Grade"]]="Pass ayiii mone"
print(dataframe)


print("--------------------------------------------")

dataframe.loc[(dataframe["score"]>75) & (dataframe["score"]<150),["Grade"]]="Nee mass adaa"
print(dataframe)

print("--------------------------------------------")

dataframe.loc[(dataframe["score"]>150) ,["Grade"]]="nee killadi thane"
print(dataframe)