import pandas as pd
data_z = {
    'marks': [45, 50, 52, 48, 49, 51, 47, 46, 53, 54,
              50, 49, 48, 47, 46, 52, 51, 50, 49, 95]
}
df=pd.DataFrame(data_z)
q1=df["marks"].quantile(.25)
q3=df["marks"].quantile(.75)
iqr=q3-q1
lowerbound=q1-1.5*iqr
upperbound=q3+1.5*iqr
# print(q1)
# print(q3)
# print(iqr)
# print(lowerbound)
# print(upperbound)
outliers=df[(df["marks"]<lowerbound)|(df["marks"]>upperbound)]
print(outliers)