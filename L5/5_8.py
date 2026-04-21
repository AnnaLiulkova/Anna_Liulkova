import pandas as pd

index = pd.MultiIndex.from_tuples([
    ('Червень', 'Дніпро'), ('Червень', 'Рось'),
    ('Липень', 'Дніпро'), ('Липень', 'Рось'),
    ('Серпень', 'Дніпро'), ('Серпень', 'Десна')
], names=['Місяць', 'Водойма'])

data = [15, 8, 22, 12, 5, 18]

df_fishing = pd.DataFrame(data, index=index, columns=['Кількість риби'])

K = 4 
target_month = 'Липень'

print("--- Повний журнал риболовлі ---")
print(df_fishing)

print(f"\n1) Перші {K} записів таблиці:")
print(df_fishing.head(K))

print("\n2) Загальні статистичні показники за все літо:")
print(df_fishing.describe().loc[['mean', 'min', 'max']])

print(f"\n3) Сумарна кількість риби за {target_month}:")
total_fish = df_fishing.xs(target_month, level='Місяць')['Кількість риби'].sum()
print(f"Разом: {total_fish} шт.")