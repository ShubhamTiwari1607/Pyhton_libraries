# 2. Intrinsic NumPy array creation functions
# 1 - 1D array creation functions
# The 1D array creation functions e.g. numpy.linspace and numpy.arange generally need at least two inputs, start and stop.

import numpy as np

np.arange(10)
np.arange(2, 10, dtype=float)
 
np.arange(2, 3, 0.1)
#  best practice for numpy.arange is to use integer start, end, and step values

# numpy.arange creates arrays with regularly incrementing values.

# numpy.linspace will create arrays with a specified number of elements, and spaced equally between the specified beginning and end values.

np.linspace(1., 4., 6)

# 2 - 2D array creation functions

# he 2D array creation functions e.g. numpy.eye, numpy.diag, and numpy.vander define properties of special matrices represented as 2D arrays.

# np.eye(n, m) defines a 2D identity matrix. The elements where i=j (row index and column index are equal) are 1 and the rest are 0, as such:

np.eye(3)
np.eye(3, 5)


# numpy.diag can define either a square 2D array with given values along the diagonal or if given a 2D array returns a 1D array that is only the diagonal elements. The two array creation functions can be helpful while doing linear algebra, as such:

np.diag([1, 2, 3])
# array([[1, 0, 0],
#        [0, 2, 0],
#        [0, 0, 3]])
np.diag([1, 2, 3], 1)
# array([[0, 1, 0, 0],
#        [0, 0, 2, 0],
#        [0, 0, 0, 3],
#        [0, 0, 0, 0]])

a = np.array([[1, 2], [3, 4]])
np.diag(a)
# array([1, 4])