import numpy as np

M, N = 4, 5
matrix = np.full((M, N), 0.5)
np.fill_diagonal(matrix, -1)

print("Матриця M x N:")
print(matrix)

# Зріз робимо [0:2, 1:3], бо верхня межа не включається
sub_matrix = matrix[0:2, 1:3]

print("Підматриця:")
print(sub_matrix)