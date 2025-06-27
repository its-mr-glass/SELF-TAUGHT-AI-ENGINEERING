import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
print("Numpy array:", a)

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print("DataFRame:\n", df)

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")
plt.show()
