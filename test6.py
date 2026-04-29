import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Model
model = LogisticRegression()
model.fit(df[["hours"]], df["result"])

# Prediction
print(model.predict([[3]]))  # Output: 0 (Fail)
print(model.predict([[5]]))  # Output: 1 (Pass)

# Probability
print(model.predict_proba([[3]]))