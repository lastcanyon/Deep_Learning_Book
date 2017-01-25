import numpy as np

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) +B1

print('W1.shape', W1.shape)
print('X.shape', X.shape)
print('B1.shape', B1.shape)

def sigmoid(x):
    return 1/(1+np.exp(-x)) #넘파이 배열을 반환

Z1 = sigmoid(A1)

print('A1', A1)
print('Z1', Z1)