# adding new row and col
import numpy as np
import numpy as np

# Original array
original = np.array([[1, 2],
                     [3, 4]])

# Add a new row
new_row = np.array([[5, 6]])
with_new_row = np.vstack((original, new_row))

print("Original array:\n", original)
print("After adding new row:\n", with_new_row)

# Add a new column
new_col = np.array([[7],[8]])
with_new_col = np.hstack((original, new_col))

print("With new column:\n", with_new_col)

np.delete()