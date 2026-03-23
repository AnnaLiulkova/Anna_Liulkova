def get_negatives_loop(lst):
    negatives = []
    for num in lst:
        if num < 0:
            negatives.append(num)
    return negatives

def get_negatives_comp(lst):
    return [num for num in lst if num < 0]

try:
    user_input = input("Введіть числа списку через пробіл (наприклад: 5 -3 12 -7 0): ")
    original_list = [int(x) for x in user_input.split()]
    
    print(f"Початковий список: {original_list}")
    print("Варіант 1 (цикл):", get_negatives_loop(original_list))
    print("Варіант 2 (генератор):", get_negatives_comp(original_list))
except ValueError:
    print("Помилка: будь ласка, вводьте лише цілі числа через пробіл")