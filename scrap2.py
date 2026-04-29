import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Arun", "Meera", "John", "Sara", "Rahul", "Anu", "David", "Neha"],
    "Course": ["Python", "Java", "Python", "C++", "Java", "C++", "Python", "Java"],
    "City": ["Kochi", "Calicut", "Kochi", "Trivandrum", "Calicut", "Kochi", "Trivandrum", "Calicut"]
}

df = pd.DataFrame(data)
print(df)
# encoded_df=pd.get_dummies(df,columns=["Course"],dtype=int)
# print(encoded_df)