import numpy as np
import pandas as pd
data = {
    'X': [2, 4, 6, 8],
    'Y': [4, 2, 4, 6]
}

df = pd.DataFrame(data)
print(df)
X = df.values
mean = np.mean(X, axis=0)
X_centered = X - mean

print("Mean:\n", mean)
print("Centered Data:\n", X_centered)
cov_matrix = np.cov(X_centered.T)

print("Covariance Matrix:\n", cov_matrix)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
# Sort in descending order
idx = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Sorted Eigenvalues:\n", eigenvalues)
print("Sorted Eigenvectors:\n", eigenvectors)
# Take first eigenvector (PC1)
PC1 = eigenvectors[:, 0]
import numpy as np
print("Principal Component (PC1):\n", PC1)
import pandas as pd

# Data
df = pd.DataFrame({
    'X': [2, 4, 6, 8],
    'Y': [4, 2, 4, 6]
})

# Convert
X = df.values

# Mean center
X_centered = X - np.mean(X, axis=0)

# Covariance
cov_matrix = np.cov(X_centered.T)

# Eigen
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort
idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]

# Projection
Z = X_centered.dot(eigenvectors[:, 0])

print("Reduced Data:\n", Z)
Z = X_centered.dot(PC1)

print("Projected Data (1D):\n", Z)