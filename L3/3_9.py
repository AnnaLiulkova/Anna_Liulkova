def mask_card_number(number_str):
    """Маскує 16-значний рядок цифр, залишаючи лише останні 4"""
    if len(number_str) == 16 and number_str.isdigit():
        last_four = number_str[-4:]
        return f"**** **** **** {last_four}"
    else:
        return "Помилка: рядок має містити рівно 16 цифр"

card = "1111222233334444"
masked = mask_card_number(card)
print(f"Оригінал: {card}")
print(f"Замасковано: {masked}")