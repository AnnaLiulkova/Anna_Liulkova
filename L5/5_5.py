import pandas as pd
grades_dict = {
    'Нейронні мережі': [90, 85, 88, 92, 78, 95, 82],
    'СШІ': [95, 80, 89, 90, 85, 98, 88]
}
df_grades = pd.DataFrame(grades_dict, index=[f'Студент_{i}' for i in range(1, 8)])

K = 3 
L = 2 

print(f"Перші {K} рядки (head):")
print(df_grades.head(K))

print(f"\nОстанні {L} рядки (tail):")
print(df_grades.tail(L))