# Importing data with genfromtxt

#  genfromtxt runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. This mechanism is slower than a single loop, but gives more flexibility. In particular, genfromtxt is able to take missing data into account, when other faster and simpler functions like loadtxt cannot.

# The only mandatory argument of genfromtxt is the source of the data. It can be a string, a list of strings, a generator or an open file-like object with a read method, for example, a file or io.StringIO object. If a single string is provided, it is assumed to be the name of a local or remote file. If a list of strings or a generator returning strings is provided, each string is treated as one line in a file. When the URL of a remote file is passed, the file is automatically downloaded to the current directory and opened.

import numpy as np
from io import StringIO

data = "1; 2; 3\n4; 5; 6"
print(np.genfromtxt(StringIO(data), delimiter=";"))

# Alternatively, we may be dealing with a fixed-width file, where columns are defined as a given number of characters. In that case, we need to set delimiter to a single integer (if all the columns have the same size) or to a sequence of integers (if columns can have different sizes):(spaces are also counted as characters)

data = "  1  2  3\n  4  5 67\n890123  4"
print("\n",np.genfromtxt(StringIO(data), delimiter=3))

data = "123456789\n   4  7 9\n   4567 9"
print("\n",np.genfromtxt(StringIO(data), delimiter=(4, 3, 2)))

# By default, when a line is decomposed into a series of strings, the individual entries are not stripped of leading nor trailing white spaces. This behavior can be overwritten by setting the optional argument autostrip to a value of True:

data = "1, abc , 2\n 3, xxx, 4"
# Without autostrip
print("\nWithout autostrip\n",np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5"))
# With autostrip
print("\nWith autostrip\n",np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True))

# The skip_header and skip_footer arguments.The values of this argument must be an integer which corresponds to the number of lines to skip at the beginning of the file, before any other action is performed. 

data = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(data),))
print(np.genfromtxt(StringIO(data),  skip_header=3, skip_footer=5))

# The usecols argument
# In some cases, we are not interested in all the columns of the data but only a few of them. We can select which columns to import with the usecols argument.
data = "1 2 3\n4 5 6"
print("\n usecol argument\n",np.genfromtxt(StringIO(data), usecols=(0, -1)))

# if the columns have names, we can also select which columns to import by giving their name to the usecols argument, either as a sequence of strings or a comma-separated string:

data = "1 2 3\n4 5 6"
print(np.genfromtxt(StringIO(data),names="a, b, c", usecols=("a", "c")))
print(np.genfromtxt(StringIO(data),names="a, b, c", usecols=("a, c")))