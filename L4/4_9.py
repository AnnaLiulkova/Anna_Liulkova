import numpy as np
import matplotlib.pyplot as plt

K, L = 10, 10 

image = np.random.randint(0, 256, (K, L))
smoothed_image = image.copy().astype(float)

smoothed_image[1:-1, 1:-1] = (
    image[:-2, :-2] + image[:-2, 1:-1] + image[:-2, 2:] +  
    image[1:-1, :-2] + image[1:-1, 1:-1] + image[1:-1, 2:] + 
    image[2:, :-2]  + image[2:, 1:-1]  + image[2:, 2:]     
) / 9.0

print("Фрагмент оригінальної матриці (3x3):")
print(image[:3, :3])
print("\nЗначення згладженого центрального елемента (1,1):")
print(smoothed_image[1, 1])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Оригінал (з шумом)')
ax2.imshow(smoothed_image, cmap='gray', vmin=0, vmax=255)
ax2.set_title('Після згладжування')
plt.show()