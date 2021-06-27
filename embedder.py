import numpy as np
from chao import chao_permutation

def embed(stego, secret, chromosome):
    # Convert data to uint8
    stego = stego.astype('uint8')
    secret = secret.astype('uint8')
    # stego = _stego.copy()
    # secret = _secret.copy()
    # chromosome = _chromosome
    """Embed secret bits into stego bits according to the chromosome"""

    """The chromosome has the following gene representation:
    [x0, xoffset, yoffset, bit-planes, sb-pole, sb-dire, bp-dire]"""
    stego_shape = stego.shape
    secret_shape = secret.shape
    x0 =         ((chromosome >> 25) & 1023) / 1024
    a =          3.57
    X_off =      (chromosome >> 16) & 511
    Y_off =      (chromosome >>  7) & 511
    bit_planes = (chromosome >>  3) & 15
    sb_pole =    (chromosome >>  2) & 1
    sb_dir =     (chromosome >>  1) & 1
    bp_dir =     (chromosome >>  0) & 1

    # Bit-Planes: Extract the bit mask
    mask = np.unpackbits(np.array([bit_planes], dtype='uint8'))[4:]
    idx = np.argwhere(mask == True)
    idx = 3 - idx
    idx = idx[::-1]

    if len(idx) == 0:
        return None

    # Flatten the secret bits
    secret = np.concatenate(secret)
    idx = np.concatenate(idx)

    if len(secret) * 8 > stego_shape[0] * stego_shape[1] * len(idx):
        return None

    # SB-Pole: Compliment secret bits
    if sb_pole:
        np.invert(secret, secret)

    # SB-Dire: reverse the secret sequence
    if sb_dir:
        secret = secret[::-1]

    # BP-Dire: Use LSB or MSB
    if bp_dir:
        idx += 4

    # Generate permutation and reorder the secret bits
    perm = chao_permutation(x0, a, len(secret))
    secret = secret[perm]

    # Secret bitarray
    secret = np.unpackbits(secret)

    # Embed the secret bits into stego
    pos = 0
    for i in range(stego.shape[0]):
        for j in range(stego.shape[1]):
            for k in idx:
                if pos >= len(secret):
                    break
                # embed secret[pos] at bit k of stego[(X_off + i) % stego.shape[0]][(Y_off + j) % stego.shape[1]] 
                x = (X_off + i) % stego.shape[0]
                y = (Y_off + j) % stego.shape[1]
                stego[x][y] &= ~(1 << k)
                stego[x][y] |= (secret[pos] << k)
                pos += 1

    return stego