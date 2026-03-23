def insert_custom(lst, num, index):
    return lst[:index] + [num] + lst[index:]

try:
    user_input = input("Введіть числа списку через пробіл: ")
    initial_list = [int(x) for x in user_input.split()]
    
    number_to_insert = int(input("Введіть число для вставки: "))
    insert_index = int(input("Введіть індекс, перед яким вставити число: "))
    
    new_list = insert_custom(initial_list, number_to_insert, insert_index)
    print(f"Список після вставки: {new_list}")
except ValueError:
    print("Помилка: будь ласка, вводьте лише цілі числа через пробіл")