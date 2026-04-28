# 2.1 - general ndarray creation functions
# numpy.zeros will create an array filled with 0 values with the specified shape. The default dtype is float64:

import numpy as np
from numpy.random import default_rng
default_rng(42).random((2,3))

np.zeros((2, 3))

# array([[0., 0., 0.],
#        [0., 0., 0.]])

np.zeros((2, 3, 2))

# array([[[0., 0.],
#         [0., 0.],
#         [0., 0.]],

#        [[0., 0.],
#         [0., 0.],
#         [0., 0.]]])

# numpy.ones will create an array filled with 1 values. It is identical to zeros in all other respects as such:

np.ones((2, 3))
# array([[1., 1., 1.],
#        [1., 1., 1.]])

np.ones((2, 3, 2))
# array([[[1., 1.],
#         [1., 1.],
#         [1., 1.]],

#        [[1., 1.],
#         [1., 1.],
#         [1., 1.]]])


# array([[0.77395605, 0.43887844, 0.85859792],
#        [0.69736803, 0.09417735, 0.97562235]])

default_rng(42).random((2,3,2))
# array([[[0.77395605, 0.43887844],
#         [0.85859792, 0.69736803],
#         [0.09417735, 0.97562235]],
#        [[0.7611397 , 0.78606431],
#         [0.12811363, 0.45038594],
#         [0.37079802, 0.92676499]]])

print(np.full((2,2),7))

array = np.arange(0,11,2) 
print("original array\n",array)

reshaped = array.reshape((2,3));
print("\nReshaped array\n",reshaped)

flattened = reshaped.flatten();
print("\nflattened array\n",flattened)

transpose = reshaped.T 
print("\nTranspose\n",transpose)