import pandas as pd
from sklearn.linear_model import LinearRegression

# Data
data = {
    'Age':[25,30,35,40,45,50,28,38,42,33],
    'BMI':[22,25,28,30,32,35,24,29,31,27],
    'BP':[80,85,88,92,95,100,82,90,94,87],
    'Glucose':[90,100,110,120,130,140,95,115,125,105],
    'Disease':[0,0,0,1,1,1,0,1,1,0]
}

df = pd.DataFrame(data)

X = df[['Age','BMI','BP','Glucose']]
y = df['Disease']

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coe")
prediction = model.predict([[42,31,94,125]])
print("Predicted Disease Value:", prediction)