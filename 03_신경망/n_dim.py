import numpy as np

print('----A----')
A = np.array([1, 2, 3, 4])
print(A)

np.ndim(A)

print(A.shape)
print(A.shape[0])

print('----B----')
B = np.array([[1,2], [3,4], [5,6]])
print(B)

print(np.ndim(B))
print(B.shape)