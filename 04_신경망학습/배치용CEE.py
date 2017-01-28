import numpy as np

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y[np.arrange(batch_size), t])) / batch_size
    # 원-핫 인코딩이 아니라 2나 7 등의 숫자 레이블이 주어졌을 때 교차 엔트로피 오차