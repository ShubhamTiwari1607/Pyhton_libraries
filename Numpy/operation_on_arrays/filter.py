import numpy as np
numbers = np.arange(0,11)

mask = numbers % 2 == 0
even_numbers = numbers[mask]

print(even_numbers)

