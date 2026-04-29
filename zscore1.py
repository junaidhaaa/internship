import pandas as pd
Data={'Sales':[120,130,125,140,135,128,132,500,520,118,]}
df=pd.DataFrame(Data,columns=['x'])
# print(df)
mean=df['x'].mean()
# print(mean)
sd=df['x'].std()
# print(sd)
df['zscore']=(df['x']-mean)/sd
# print(df)
outliers=df[df['zscore'].abs()>2]
print(outliers)