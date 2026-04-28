import numpy as np 

numbers = np.arange(11)

# for i in range(10):
#     if numbers[i] % 2 == 0:
#         numbers[i] *= 2

new_array = np.where(numbers % 2 == 0 , numbers*2, numbers )
print(new_array)