import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, None, 85]
})
print(df.fillna(25))
# print(df.dropna())