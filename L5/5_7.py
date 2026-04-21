import pandas as pd

products_data = {
    'Товар': ['Ноутбук', 'Мишка', 'Клавіатура', 'Монітор', 'Флешка'],
    'Ціна': [35000, 800, 1500, 7000, 300]
}
df_products = pd.DataFrame(products_data)

df_sorted = df_products.sort_values(by='Ціна', ascending=True)
df_sorted = df_sorted.reset_index(drop=True)

print("Відсортована таблиця товарів:")
print(df_sorted)