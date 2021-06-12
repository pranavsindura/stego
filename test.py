from stego import find_embedding
import numpy as np

A = np.array([[1, 1], [1, 1]])
B = np.array([[3, 3], [3, 3]])

if A.dtype != (np.float32 or np.float64):
    A = A.astype(np.float32)
if B.dtype != (np.float32 or np.float64):
    B = B.astype(np.float32)

print(A)
print(B)
print(np.mean((A - B) ** 2))