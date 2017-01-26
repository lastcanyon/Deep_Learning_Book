import numpy as np

def softmax(a):
    exp_a = np.exp(a) # 지수 함수
    sum_exp_a = np.sum(exp_a) # 지수 함수의 합
    y = exp_a / sum_exp_a
    return y