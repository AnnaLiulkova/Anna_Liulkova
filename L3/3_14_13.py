def transform_case(text):
    print("Оберіть дію:")
    print("1 - Все у великі літери")
    print("2 - Все у маленькі літери")
    print("3 - Змінити регістр (Swap case)")
    
    choice = input("Ваш вибір: ")
    
    if choice == '1':
        return text.upper()
    elif choice == '2':
        return text.lower()
    elif choice == '3':
        return text.swapcase()
    else:
        return "Неправильний вибір"

user_text = "Програмувати на Python це круто! Тест РЕГІСТРУ"
result = transform_case(user_text)
print(f"Результат: {result}")