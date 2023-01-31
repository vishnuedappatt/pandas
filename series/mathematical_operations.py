import pandas as pd

series1=pd.Series([1,2,3,4,5])
series2=pd.Series([2,4,6,8,10])

# addition
add=series1+series2
print(add)
print("---------------")
add=series1.add(series2)
print(add)
print("---------------")


# substract

sub=series1-series2
print(sub)
print("-----------------")

mul=series1*series2
print(mul)
print("-----------------")

power=series1 ** series2
print(power)
print("-----------------")

mod=series1 %series2
print(mod)
print("-----------------")

 # get true or false for conditional operators
less_than=series1 <series2  
print(less_than)

greater=series1 >series2 
print(greater)


# get true or false for conditional operators

print("---------------3--")

equal=series1==series2
print(equal,'eq')

equal=series1.equals(series2)
print(equal,'eq')