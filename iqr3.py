import pandas as pd
data = {'Student': ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10',
                'S11','S12','S13','S14','S15','S16','S17','S18','S19','S20'],
    'Study_Hours': [2,3,4,2,5,3,4,2,3,4, 5,6,2,3,4,5,3,2,4,3],
    'Marks': [40,45,50,42,55,48,52,41,47,53,
              56,60,43,46,51,54,49,44,52,95]}
df=pd.DataFrame(data)
q1=df["Marks"].quantile(0.25)
q3=df["Marks"].quantile(0.75)
iqr=q3-q1
lowerbound=q1-1.5*iqr
upperbound=q3+1.5*iqr
print(q1)
print(q3)
print(iqr)
print(lowerbound)
print(upperbound)
outliers=df[(df["Marks"]<lowerbound)|(df["Marks"]>upperbound)]
print(outliers)