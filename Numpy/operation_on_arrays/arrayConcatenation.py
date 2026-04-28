import numpy as  np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

combined = np.concatenate((arr1,arr2))

print("combined array ",combined)

print("if arr1 and arr2 are compatible: ", arr1.shape == arr2.shape)