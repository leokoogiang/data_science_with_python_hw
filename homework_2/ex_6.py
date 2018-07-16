import numpy as np
M = np.array([[1,2,3,4,5],[3,4,2,5,6],[1,6,3,2,5]])
print(M)
output = [sum(M[:,i]) for i in range(5)]

print(output)
