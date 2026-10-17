import numpy as np

# 1. Creation
arr = np.array([10, 20, 30, 40, 50])

# 2. Arithmetic
print("Add 5:", arr + 5)
print("Double:", arr * 2)

# 3. Statistics
print("Total Sum:", np.sum(arr))
print("Average:", np.mean(arr))

# 4. Filtering & Slicing
print("First 3 elements:", arr[:3])
print("Filter values > 25:", arr[arr > 25])

# 5. Reshaping
grid = np.array([1, 2, 3, 4, 5, 6])
print("2D Matrix (2x3):\n", grid.reshape(2, 3))
