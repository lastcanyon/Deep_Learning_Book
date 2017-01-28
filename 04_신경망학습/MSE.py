import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 정답은 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# Ex1 : '2'일 확률이 가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))

# Ex2 : '7'일 확률이 가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))