import random

def generate_random_list(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

try:
    n = int(input("Введіть кількість елементів списку (n): "))
    a = int(input("Введіть початок інтервалу (a): "))
    b = int(input("Введіть кінець інтервалу (b): "))
    
    if n <= 0:
        print("Помилка: кількість елементів має бути більшою за нуль")
    else:
        if a > b:
            print("Помилка: a більше за b. Міняємо їх місцями для коректної роботи")
            a, b = b, a
        random_list = generate_random_list(n, a, b)
        print(f"Згенерований список: {random_list}")

except ValueError:
    print("Помилка: потрібно вводити лише цілі числа")