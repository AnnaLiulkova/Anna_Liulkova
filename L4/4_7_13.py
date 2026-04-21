import numpy as np
K = 8
N = 13

matrix_7 = np.zeros((K, K), dtype=int)

matrix_7[0::2, 1::2] = N
matrix_7[1::2, 0::2] = N

print(f"\nМатриця {K}x{K} (шаховий порядок):")
print(matrix_7)