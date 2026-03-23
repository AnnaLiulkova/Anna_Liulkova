def remove_element_loop(lst, n):
    result = []
    for item in lst:
        if item != n:
            result.append(item)
    return result

def remove_element_comp(lst, n):
    return [item for item in lst if item != n]

try:
    user_input = input("Введіть числа списку через пробіл: ")
    my_list = [int(x) for x in user_input.split()]
    number_to_remove = int(input("Введіть число n, яке потрібно видалити: "))
    
    print(f"Початковий список: {my_list}")
    print("Варіант 1 (цикл):", remove_element_loop(my_list, number_to_remove))
    print("Варіант 2 (генератор):", remove_element_comp(my_list, number_to_remove))
except ValueError:
    print("Помилка: будь ласка, вводьте лише цілі числа через пробіл")