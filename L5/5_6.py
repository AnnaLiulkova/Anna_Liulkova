import pandas as pd

grades_data = {
    'Нейронні мережі': [90, 100, 98, 92, 95],
    'СШІ': [95, 80, 89, 90, 85]
}
df = pd.DataFrame(grades_data, index=['Олег', 'Марія', 'Іван', 'Катя', 'Петро'])

mean_grades = df.mean()

print("Таблиця оцінок:")
print(df)
print("\nСередній бал за дисциплінами:")
print(mean_grades)