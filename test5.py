import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
Y = np.array([42,50,55,61,68,72,78,85,90,96])

# Create model
model = LinearRegression()

# Train model
model.fit(X, Y)

# Get slope (m) and intercept (c)
m = model.coef_[0]
c = model.intercept_

print("Slope (m):", m)
print("Intercept (c):", c)

# Predict for 12 hours
pred = model.predict([[12]])
print(pred)

