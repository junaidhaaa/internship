import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("university.csv")

# clean column names
df.columns = df.columns.str.strip()

print(df.head())  # debug

X = df[["Score"]]
Y = df["Point"]

model = LinearRegression()
model.fit(X, Y)

# prediction
new_data = pd.DataFrame([[15]], columns=["Score"])
prediction = model.predict(new_data)

print("Predicted points:", prediction)