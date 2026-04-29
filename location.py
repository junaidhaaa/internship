import pandas as pd

data = {
    "order_id": [101,102,103,104,105,106,107,108,109,110],
    "date": ["01-01-2026","02-01-2026","03-01-2026","04-01-2026","05-01-2026",
             "06-01-2026","07-01-2026","08-01-2026","09-01-2026","10-01-2026"],
    "customer": ["A","B","C","A","B","C","A","B","C","A"],
    "product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Mobile","Laptop","Tablet","Mobile"],
    "category": ["Electronics","Electronics","Electronics","Electronics","Electronics",
                 "Electronics","Electronics","Electronics","Electronics","Electronics"],
    "price": [50000,20000,15000,52000,21000,16000,22000,51000,15500,23000],
    "quantity": [1,2,1,1,1,2,1,1,2,1],
    "city": ["Chennai","Bangalore","Chennai","Delhi","Delhi","Chennai","Bangalore","Delhi","Chennai","Bangalore"]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
# print(df)
df["total_amount"]=df["price"]*df["quantity"]
# print(df["total_amount"])
# print(df["total_amount"].sum())
# print(df.groupby("product")["total_amount"].sum())
# print(df.groupby("city")["total_amount"].sum())
# print(df.groupby("product")["quantity"].sum().sort_values(ascending=False))
# print(df.groupby("date")["total_amount"].sum())
# print(df.groupby("customer")["total_amount"].sum())
# print(df.sort_values(by="total_amount",ascending=False).head(1))
# print(df[df["total_amount"]>30000])
    

