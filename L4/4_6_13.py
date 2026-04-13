import numpy as np
N = 13

matrix_6 = np.zeros((7, 7), dtype=int)
rows, cols = np.indices((7, 7))

mask = np.abs(rows - 3) + np.abs(cols - 3) == 3

matrix_6[mask] = N

print("\nМатриця:")
print(matrix_6)