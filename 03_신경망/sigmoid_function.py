import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x)) #넘파이 배열을 반환

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)