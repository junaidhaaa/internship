import pandas as pd
data={"sales":[118,119,120,121,122,125,127,128,129,130,131,132,134,135,136,138,140,500,520,600]}
df=pd.DataFrame(data,columns=['sales'])
# print(df)
y=df['sales'].mean()
# print(y)
sd=df['sales'].std()
# print(sd)
df['zscore']=(df['sales']-y)/sd
# print(df)
outliers=df[df['zscore'].abs()>2]
print(outliers)