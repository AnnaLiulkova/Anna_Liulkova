import numpy as np
import matplotlib.pyplot as plt

K = 17
L = 13
N = 50

arr = np.random.randint(L, N, K)

x_min = arr.min()
x_max = arr.max()

arr_norm = (arr - x_min) / (x_max - x_min)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(range(K), arr, color='royalblue', edgecolor='black')
ax1.set_title('Початковий масив')
ax1.set_xlabel('Індекс')
ax1.set_ylabel('Значення')

ax2.bar(range(K), arr_norm, color='seagreen', edgecolor='black')
ax2.set_title('Нормалізований масив [0, 1]')
ax2.set_xlabel('Індекс')
ax2.set_ylabel('Нормалізоване значення')

plt.tight_layout()
plt.show()