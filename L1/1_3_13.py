import math

def get_term(i, n, x):
    if i % 3 == 0:
        sign = -1
    else:
        sign = 1
        
    numerator = n - i
    
    if i % 2 != 0:
        denominator = math.cos(i * x)
    else:
        denominator = math.sin(i * x)
        
    #якщо знаменник дуже близький до нуля, вважаємо це діленням на нуль
    if abs(denominator) < 1e-9:
        raise ZeroDivisionError(f"Ділення на нуль (або майже нуль) в елементі i={i}")
        
    return sign * (numerator / denominator)

#FOR
def calc_for(n, x):
    total_sum = 0
    try:
        for i in range(1, n + 1):
            total_sum += get_term(i, n, x)
        return True, total_sum
    except ZeroDivisionError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Непередбачена помилка: {e}"

#WHILE
def calc_while(n, x):
    total_sum = 0
    i = 1
    try:
        while i <= n:
            total_sum += get_term(i, n, x)
            i += 1
        return True, total_sum
    except ZeroDivisionError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Непередбачена помилка: {e}"

#РЕКУРСІЯ
def calc_recursive(i, n, x):
    if i > n:
        return True, 0
    
    try:
        current_term = get_term(i, n, x)
        success, next_sum = calc_recursive(i + 1, n, x)
        
        if not success:
            return False, next_sum 
            
        return True, current_term + next_sum
        
    except ZeroDivisionError as e:
        return False, str(e)
    except RecursionError:
        return False, "Перевищено максимальну глибину рекурсії"
    except Exception as e:
        return False, f"Непередбачена помилка: {e}"



def main():
    print("Третє завдання")
    
    while True:
        try:
            n = int(input("Введіть кількість елементів n (натуральне число): "))
            if n <= 0:
                print("n має бути натуральним числом (1, 2, 3...). Спробуйте ще раз\n")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число\n")

    while True:
        try:
            x_deg = float(input("Введіть значення x (дійсне число, в градусах): "))
            x_rad = math.radians(x_deg) 
            break
        except ValueError:
            print("Будь ласка, введіть дійсне число.\n")

    print(f"\nОбчислення для n = {n}, x = {x_deg} градусів:")
    print("-" * 40)

    #FOR
    success_for, result_for = calc_for(n, x_rad)
    if success_for:
        print(f"1. Сума (FOR):      {result_for:.6f}")
    else:
        print(f"1. Сума (FOR):      Помилка: {result_for}")

    #WHILE
    success_while, result_while = calc_while(n, x_rad)
    if success_while:
        print(f"2. Сума (WHILE):    {result_while:.6f}")
    else:
        print(f"2. Сума (WHILE):    Помилка: {result_while}")

    #РЕКУРСІЯ
    success_rec, result_rec = calc_recursive(1, n, x_rad)
    if success_rec:
        print(f"3. Сума (РЕКУРСІЯ): {result_rec:.6f}")
    else:
        print(f"3. Сума (РЕКУРСІЯ): Помилка: {result_rec}")

if __name__ == "__main__":
    main()