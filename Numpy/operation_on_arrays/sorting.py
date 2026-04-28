import numpy as np

unsorted_array = np.array([1,4,3,5,2])

print("Unsorted array",unsorted_array)

sorted_array = np.sort(unsorted_array)
print("Sorted array",sorted_array)

unsorted_2Darray =  np.array([[1,8,4],[3,6,5]])

sorted_2Darray = np.sort(unsorted_2Darray,axis=0)
# axis = 1 -> left to right axis = 0 -> top to bottom
print("Sorted 2D array\n",sorted_2Darray)