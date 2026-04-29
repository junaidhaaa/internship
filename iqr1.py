import pandas as pd
data={"age":[15,15,13,10,16,17,17,18,18,20,30]}
df=pd.DataFrame(data) #converting to data frame
q1=df["age"].quantile(0.25)
q3=df["age"].quantile(0.75)
iqr=q3-q1
lowerbound=q1-1.5*iqr
upperbound=q3+1.5*iqr
# print(q1)
# print(q3)
# print(iqr)
# print(lowerbound)
# print(upperbound)
outliers=df[(df["age"]<lowerbound)|(df["age"]>upperbound)]
# print(outliers)
