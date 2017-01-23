import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        print(0)
    else:
        print(1)
print("AND게이트")
AND(0, 0)
AND(1, 0)
AND(0, 1)
AND(1, 1)

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b

    if(tmp <= 0):
        print(0)
    else:
        print(1)
print("NAND게이트")
NAND(0, 0)
NAND(1, 0)
NAND(0, 1)
NAND(1, 1)


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        print(0)
    else:
        print(1)
print("OR게이트")
OR(0, 0)
OR(1, 0)
OR(0, 1)
OR(1, 1)