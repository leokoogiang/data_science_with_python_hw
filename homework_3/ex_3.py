import numpy as np
print('Now you will create 3D array M*N*K')
M = int(input('M: '))
N = int(input('N: '))
K = int(input('K: '))

arr = np.random.randint(-100,101, (M,N,K))
print(arr)

def find_min_max_sum(array,k):
    print('Min = ', np.min(array,axis=k))
    print('Max = ', np.max(array,axis=k))
    print('Sum = ', np.sum(array, axis=k))

print('**************')
print('Min, max, sum by depth')
find_min_max_sum(arr,0)

print('***************')
print('Min, max, sum by height')
find_min_max_sum(arr,1)

print('***************')
print('Min, max, sum by width')
find_min_max_sum(arr,2)