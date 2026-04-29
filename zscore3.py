import pandas as pd
data = {
    'Student': ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10',
                'S11','S12','S13','S14','S15','S16','S17','S18','S19','S20'],
    'Study_Hours': [2,3,4,2,5,3,4,2,3,4,5,6,2,3,4,5,3,2,4,3],
    'Marks': [40,45,50,42,55,48,52,41,47,53,
              56,60,43,46,51,54,49,44,52,95]}
df=pd.DataFrame(data,columns=['Marks'])
# print(df)
y=df['Marks'].mean()
# print(y)
sd=df['Marks'].std()
# print(sd)
df['zscore']=(df['Marks']-y)/sd
# print(df)
outliers=df[df['zscore'].abs()>2]
print(outliers)