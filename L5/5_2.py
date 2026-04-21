import pandas as pd

K = 5
grades_dict = {
    'Нейронні мережі': [90, 100, 98, 92, 95],
    'СШІ': [95, 80, 89, 90, 85]
}

df_grades = pd.DataFrame(grades_dict, index=[f'Студент_{i}' for i in range(1, K + 1)])

print("Таблиця оцінок студентів:")
print(df_grades)