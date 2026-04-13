import numpy as np

K = 5 
N = 13 

matrix_5 = np.zeros((K, K), dtype=int)
np.fill_diagonal(np.fliplr(matrix_5), N)

print("Матриця KxK (побічна діагональ):")
print(matrix_5)