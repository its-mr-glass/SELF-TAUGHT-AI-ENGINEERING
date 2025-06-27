import pandas as pd

data = {
    "Name": ["Lamar", "Ada", "Elon"], 
    "Age": [23, 36, 52],
    "Sex": ["Male", "Female", "Male"]
}

df = pd.DataFrame(data)
print(df)

df["Country"] = ["Kenya", "United-Kingdom", "United-States-of-America"] # Add column
print(df["Name"]) # Access column
print(df.loc[0]) # Access row by index
print(df.describe()) # summary stats
