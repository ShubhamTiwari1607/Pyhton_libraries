# 3) Replicating, joining, or mutating existing arrays

# When you assign an array or its elements to a new variable, you have to explicitly numpy.copy the array, otherwise the variable is a view into the original array. Consider the following example:

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
print('a =', a, '; b =', b)
# a = [2 3 3 4 5 6] ; b = [2 3]

# In this example, you did not create a new array. You created a variable, b that viewed the first 2 elements of a. When you added 1 to b you would get the same result by adding 1 to a[:2]. If you want to create a new array, use the numpy.copy array creation routine as such:

a = np.array([1, 2, 3, 4])
b = a[:2].copy()
b += 1
print('a = ', a, 'b = ', b)
# a =  [1 2 3 4] b =  [2 3]