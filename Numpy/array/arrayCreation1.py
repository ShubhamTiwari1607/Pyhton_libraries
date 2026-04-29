import numpy as np
# 1. creating array from list
a1D = np.array([1, 2, 3, 4])
# print("1-D array",a1D)

a2D = np.array([[1, 2], [3, 4]])
# print("2-D array",a2D)

a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("3-D array", a3D, a3D.dtype)

# When you use numpy.array to define a new array, you should consider the dtype of the elements in the array, which can be specified explicitly. This feature gives you more control over the underlying data structures and how the elements are handled in C/C++ functions

import numpy as np
a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b
print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
c_signed32 = a - b.astype(np.int32)
print('signed c:', c_signed32, c_signed32.dtype)


# When you perform operations with different dtype, NumPy will assign a new type that satisfies all of the array elements involved in the computation, here uint32 and int32 can both be represented in as int64.
# The default NumPy behavior is to create arrays in either 32 or 64-bit signed integers (platform dependent and matches C long size) or double precision floating point numbers. If you expect your integer arrays to be a specific type, then you need to specify the dtype while you create the array.

print(np.array([3]*10,dtype=float))