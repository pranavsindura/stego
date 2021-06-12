def makePermutation(x0, a, limit):
    # f(n + 1) = a * f(n) * (1 - f(n))
    arr = []
    arr.append(x0)
    ptr = 1
    while ptr < limit:
        newx = x0 * a * (1 - x0)
        arr.append(newx)
        x0 = newx
        ptr += 1
    return arr

# arr = makePermutation(0.492, 3.57, 10)
# for x in arr:
#     print(x)