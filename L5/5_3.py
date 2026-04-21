import pandas as pd

prices = pd.Series({'Ноутбук': 35000, 'Мишка': 800, 'Клавіатура': 1500, 'Монітор': 7000})

price_by_label = prices.loc['Мишка']
price_by_index = prices.iloc[1]

print(prices, "\n")
print(f"Ціна за текстовою міткою 'Мишка': {price_by_label}")
print(f"Ціна за числовим індексом 1: {price_by_index}")