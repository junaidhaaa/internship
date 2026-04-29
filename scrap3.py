import pandas as pd

data = {
    "Student": ["Arun", "Meera", "John", "Sara", "Rahul"],
    "Level": ["Beginner", "Intermediate", "Advanced", "Beginner", "Advanced"]
}

df = pd.DataFrame(data)
print(df)

mapping = {
    "Beginner": 0,
    "Intermediate": 1,
    "Advanced": 2
}

df["Level_Encoded"] = df["Level"].map(mapping)
print(df)