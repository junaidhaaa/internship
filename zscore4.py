import pandas as pd
data_z = {
    'marks': [45, 50, 52, 48, 49, 51, 47, 46, 53, 54,
              50, 49, 48, 47, 46, 52, 51, 50, 49, 95]
}
df=pd.DataFrame(data_z,columns=['marks'])
# print(df)
y=df['marks'].mean()
# print(y)
sd=df['marks'].std()
# print(sd)
df['zscore']=(df['marks']-y)/sd
# print(df)
outliers=df[df['zscore'].abs()>2]
print(outliers)