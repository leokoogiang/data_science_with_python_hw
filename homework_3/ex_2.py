import numpy as np
N = int(input('Please enter the number: '))
arr = np.random.uniform(0,10.1, N*N*N).reshape(N,N,N)
print(arr)

# Find min, max, and sum of depth
d_sum = np.sum(arr, axis=0)
print('Sum by heigh or column', d_sum)
d_min = np.min(arr, axis = 0)
print('Min by heigh or column: \n', d_min)
d_max = np.max(arr, axis = 0)
print('Max by column: \n', d_max)

print('****************************')

# Find min, max, and sum by column
c_sum = np.sum(arr, axis=1)
print('Sum by row: \n', c_sum)
c_min = np.min(arr, axis = 1)
print('Min by row: \n', c_min)
c_max = np.max(arr, axis = 1)
print('Max by row: \n', c_max)

print('*****************************')

# Find min, max, sum by row
r_sum = np.sum(arr, axis = 2)
print('Sum by deep: \n', r_sum)
r_min = np.min(arr, axis = 2)
print('Min by deep: \n', r_min)
r_max = np.max(arr, axis = 2)
print('Max by deep: \n', r_max)


