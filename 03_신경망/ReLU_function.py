import numpy as np

def relu(x):
    return np.maximum(0, x) # 두 입력 중 큰 값을 선택해 반환

print(relu(1))