# Pandas is like Excel for python, on steroids ofcourse.

import pandas as pd

data = {
    "Name": ["Lamar", "Ada", "Elon"], 
    "Age": [23, 36, 52],
    "Sex": ["Male", "Female", "Male"]
}

df = pd.DataFrame(data)
print(df)