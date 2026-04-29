import pandas as pd
data={
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35]
}
df=pd.DataFrame(data,index=["a","b","c"])
print(df)


