import pandas as pd
df=pd.DataFrame({
    "Fruits":["banana","strawberry","grapes","mango"],
    "Stock":[12,15,22,17],
    "Price":[100,200,150,120]
})
#print(df)
#print(df["Price"].min())
#print(df["Price"].max())

print(df.describe())
