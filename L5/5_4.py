import pandas as pd
try:
    df_csv = pd.read_csv('L5/education.csv')
    rows, cols = df_csv.shape
    
    print(f"Дані успішно завантажено.")
    print(f"Кількість рядків: {rows}")
    print(f"Кількість стовпців: {cols}")
except FileNotFoundError:
    print("Помилка: Файл 'education.csv' не знайдено. Перевірте шлях до файлу.")