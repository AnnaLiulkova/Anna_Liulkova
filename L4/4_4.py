import numpy as np
data = np.array([12, 5, 20, 8, 15, 3])
threshold = 10

filtered = data[data > threshold]

print(f"Елементи більші за {threshold}:")
print(filtered)