import pandas as pd
data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
# print(df)
# print(df.info())
# print(df.head(10))
print(df[['Student_Name','Department']])

