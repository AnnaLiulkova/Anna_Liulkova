def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

my_string = "У 2025 році мені виповнилося 20 років"
result = count_digits(my_string)
print(f"Кількість цифр у рядку: {result}")