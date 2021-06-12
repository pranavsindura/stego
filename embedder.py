import numpy as np

def embed_the_bit(stego, secret, idx):
    """Embed the secret bits in stego[idx]"""
    np.put(stego, idx, secret)

def embed(stego, secret, chromosome):
    """Embed secret bits into stego bits according to the chromosome"""

    """The chromosome has the following gene representation:
    [dir, xoffset, yoffset, bit-planes, sb-pole, sb-dire, bp-dire]"""

    """
    Args:
    stego: Stego pixel sequence
    secret: Secret pixel sequence
    chromosome: Chromosome of the GA

    Return:
    numpy.array: stego bit sequence with embedded bits
    """
    stego_shape = stego.shape
    secret_shape = secret.shape
    direction =  (chromosome >> 25) & 7
    X_off =      (chromosome >> 16) & 511
    Y_off =      (chromosome >>  7) & 511
    bit_planes = (chromosome >>  3) & 15
    sb_pole =    (chromosome >>  2) & 1
    sb_dir =     (chromosome >>  1) & 1
    bp_dir =     (chromosome >>  0) & 1
    # Bit-Planes: Extract the bit mask
    mask = np.unpackbits(np.array([bit_planes], dtype='uint8'))[4:]
    idx = np.argwhere(mask == True)

    if len(idx) == 0:
        return None
        
    idx = np.concatenate(idx)
    capacity = round(8 / len(idx)) * len(secret)

    if capacity > stego_shape[0]:
        return None

    # Flatten the secret bits
    secret = np.concatenate(secret)

    # Convert data to uint8
    stego = stego.astype('uint8')
    secret = secret.astype('uint8')

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
    # perm = np.random.permutation(secret.shape[0])
    # secret = secret[perm]

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