import numpy as np
def chao_permutation(x0, a, limit):
    # f(n + 1) = a * f(n) * (1 - f(n))
    arr = []
    arr.append(x0)
    ptr = 1
    while ptr < limit:
        newx = x0 * a * (1 - x0)
        arr.append(newx)
        x0 = newx
        ptr += 1
    arr = np.array(arr)
    perm = arr.argsort().argsort()
    return perm