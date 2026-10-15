#pandas

import numpy as np
import pandas as pd

#Creating a Series in pandas

ser = pd.Series([10,20,30,40,50])

print(ser)
print()

# Ten random floats between 0 and 1
s = pd.Series(np.random.rand(10))
print(s)
print()

#Creating custom indexes for a series of ten numbers

ser_custom = pd.Series([10,20,30,40,50], index = ['a','b','c','d','e'])

print(ser_custom)
print()

#DataFrames

data = {'name':['Alice','Bob','Charlie'], 'Age':[24,27,22]}
df = pd.DataFrame(data)
print(df)
print()

#Handling Missing Values:

df.isnull()

df.dropna()

df.drop_duplicates()

print(df)
print()

#Merging


df1 = pd.DataFrame ({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame ({'ID':[3,4,5],'Age':[24,27,22]})


merged_df = pd.merge(df1,df2,on='ID',how='inner')

left_join = pd.merge(df1,df2,on='ID',how='left')
rt_join = pd.merge(df1,df2,on='ID',how='right')
out_join = pd.merge(df1,df2,on='ID',how='outer')


print(merged_df)
print()
print(left_join)
print()
print(rt_join)
print()
print(out_join)
print()