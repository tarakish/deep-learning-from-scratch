import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


print("-"*10)
print("AND method")
print("AND(0, 0): ", AND(0, 0))
print("AND(1, 0): ", AND(1, 0))
print("AND(0, 1): ", AND(0, 1))
print("AND(1, 1): ", AND(1, 1))


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # ANDと符号逆転
    b = 0.7  # ANDと符号逆転
    tmp = sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


print("-"*10)
print("NAND method")
print("NAND(0, 0): ", NAND(0, 0))
print("NAND(1, 0): ", NAND(1, 0))
print("NAND(0, 1): ", NAND(0, 1))
print("NAND(1, 1): ", NAND(1, 1))
