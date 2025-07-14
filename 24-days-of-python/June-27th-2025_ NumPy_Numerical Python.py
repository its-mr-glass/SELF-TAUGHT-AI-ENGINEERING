# NumPy gives you arrays: fast, memory-efficient and great for math.

import numpy as np

a = np.array([1, 2, 3])
print(a * 2) # output: [2 4 6]

# why use NumPy arrays?
# 1. way faster than python list for math
# 2. Easy operations: add, multiply, matrix ops
# 3. Foundation for ML frameworks like TensorFlow

# common NumPy Ops
print("Common NumPy Ops")

a = np.array([[1, 2], [3, 4]])
print(a.shape)      # (2, 2)
print(np.sum(a))    # 10
print(np.mean(a))   # 2.5
print(a.T)          # Transpose