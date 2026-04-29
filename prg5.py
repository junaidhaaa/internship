import pandas as pd
data=pd.read_csv("data1.csv")
df=pd.DataFrame(data)
# print(df)
# print(df.info())
# print(df.head(10))
#print(df[['Last','First']])
#print(df[df['Salary']==52000])
#print(df.sort_index(axis=1,ascending=True))
print(df.sort_values(by="Salary"))

