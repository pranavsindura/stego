import numpy as np
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

def get_direction(dir_mask, sX, sY, img, need):
    N, M = img.shape
    assert need <= N * M, "not enough pixels"
    val = []
    X = sX
    Y = sY
    while need > 0:
        val.append(img[X][Y])
        if dir_mask % 2: # X first, then Y
            X += dx[dir_mask >> 1]
            if X >= N or X < 0:
                X = (X + N) % N
                Y += dy[dir_mask >> 1]
                Y = (Y + M) % M
        else: # Y first, then X
            Y += dy[dir_mask >> 1]
            if Y >= M or Y < 0:
                Y = (Y + M) % M
                X += dx[dir_mask >> 1]
                X = (X + N) % N
        need -= 1
    return val


if __name__ == '__main__':
    arr = [[i * 4 + j + 1 for j in range(4)] for i in range(4)]
    arr = np.array(arr)

    for dir_mask in range(8):
        print("dir_mask:", dir_mask, ",", *get_direction(dir_mask, 1, 1, arr, 16))