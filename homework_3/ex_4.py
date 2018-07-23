import numpy as np
arr = np.random.uniform(-100,100.01,10*8).reshape(10,8)
print(arr)

n = float(input('Please enter a float number: '))

# Min value by column
min_1 = np.argmin(arr, axis = 0)
print('Min value by column', min_1)

min_2 = np.argmin(arr, axis = 1)
print('Min value by row', min_2)

