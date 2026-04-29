import pandas as pd
data={"sales":[118,119,120,121,122,125,127,128,129,130,131,132,134,135,136,138,140,500,520,600]}
df=pd.DataFrame(data)
q1=df["sales"].quantile(.25)
q3=df["sales"].quantile(.75)
iqr=q3-q1
lowerbound=q1-1.5*iqr
upperbound=q3+1.5*iqr
# print(q1)
# print(q3)
# print(iqr)
# print(lowerbound)
# print(upperbound)
outliers=df[(df["sales"]<lowerbound)|(df["sales"]>upperbound)]
print(outliers)