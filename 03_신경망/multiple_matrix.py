import numpy as np

print('-----Basic-----')
A = np.array([[1,2], [3,4]])
print('A행렬 모양', A.shape)
B = np.array([[5,6], [7,8]])
print('B행렬 모양', B.shape)
print('AB의 곱', np.dot(A, B))


print('-----Advance-----')
A = np.array([[1,2,3], [4,5,6]])
print('A행렬 모양', A.shape)
B = np.array([[1,2,], [3,4], [5,6]])
print('B행렬 모양', B.shape)
print('AB의 곱', np.dot(A, B))


print('----대응 차원 일치----')
A = np.array([[1,2], [3,4], [5,6]])
print('A행렬 모양', A.shape)
B = np.array([7,8])
print('B행렬 모양', B.shape)
print('AB의 곱', np.dot(A, B))