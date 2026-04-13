import numpy as np
import matplotlib.pyplot as plt

n = 10 

x = np.linspace(0.1, 5, 1000)
y = np.zeros_like(x)

for i in range(1, n + 1):
    sign = -1 if i % 3 == 0 else 1
    numerator = n - i
    
    if i % 2 != 0:
        denominator = np.cos(i * x)
    else:
        denominator = np.sin(i * x)
        
    y += sign * (numerator / denominator)

y_clipped = np.clip(y, -1000, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x, y_clipped, color='crimson', label=f'Сума ряду (n={n})')
plt.title('Графік складної функції (Варіант 13)')
plt.xlabel('x (радіани)')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.show()