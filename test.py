import numpy as np
bit_planes = 3
mask = np.unpackbits(np.array([bit_planes], dtype='uint8'))[4:]
print(mask)
idx = np.argwhere(mask == True)
idx = 3 - idx
idx = idx[::-1]
print(idx)