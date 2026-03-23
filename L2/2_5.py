def main_menu():
    BLUE = '\033[94m'
    RESET = '\033[0m'
    
    groups = {
        "КС-21": {"students": 30, "head": "Іванов І.І."},
        "КІ-22": {"students": 10, "head": "Сидоренко С.С."},
        "КН-23": {"students": 23, "head": "Петренко П.П."}
    }

    while True:
        print(BLUE + "\n" + "="*50)
        print("Поточний стан словника:", groups)
        print("-" * 50)
        print("1) Кількість студентів у зазначеній групі")
        print("2) ПІБ старости у зазначеній групі")
        print("3) Кортеж груп (студентів <= заданого значення)")
        print("4) Кортеж груп (студентів >= заданого значення)")
        print("5) Зміна кількості студентів у групі")
        print("6) Зміна ПІБ старости у групі")
        print("7) Додавання нової групи")
        print("8) Видалення заданої групи")
        print("9) Множина ПІБ старост зазначених груп")
        print("10) Вихід з програми")
        print("="*30 + RESET)
        
        choice = input("Оберіть пункт меню (1-10): ")

        if choice == '1':
            group = input("Введіть назву групи: ")
            if group in groups:
                print(f"Кількість студентів: {groups[group]['students']}")
            else:
                print("Такої групи не знайдено")

        elif choice == '2':
            group = input("Введіть назву групи: ")
            if group in groups:
                print(f"Староста: {groups[group]['head']}")
            else:
                print("Такої групи не знайдено")

        elif choice == '3':
            try:
                val = int(input("Введіть максимальну кількість студентів: "))
                res = tuple(g for g, d in groups.items() if d['students'] <= val)
                print(f"Результат: {res}")
            except ValueError:
                print("Помилка: введіть число")

        elif choice == '4':
            try:
                val = int(input("Введіть мінімальну кількість студентів: "))
                res = tuple(g for g, d in groups.items() if d['students'] >= val)
                print(f"Результат: {res}")
            except ValueError:
                print("Помилка: введіть число")

        elif choice == '5':
            group = input("Введіть назву групи: ")
            if group in groups:
                try:
                    new_count = int(input("Введіть нову кількість студентів: "))
                    groups[group]['students'] = new_count
                    print("Дані оновлено")
                except ValueError:
                    print("Помилка: введіть число")
            else:
                print("Такої групи не знайдено")

        elif choice == '6':
            group = input("Введіть назву групи: ")
            if group in groups:
                new_head = input("Введіть нове ПІБ старости: ")
                groups[group]['head'] = new_head
                print("Дані оновлено")
            else:
                print("Такої групи не знайдено")

        elif choice == '7':
            group = input("Введіть назву нової групи: ")
            if group not in groups:
                try:
                    count = int(input("Введіть кількість студентів: "))
                    head = input("Введіть ПІБ старости: ")
                    groups[group] = {"students": count, "head": head}
                    print("Групу додано")
                except ValueError:
                    print("Помилка: кількість студентів має бути числом")
            else:
                print("Така група вже існує")

        elif choice == '8':
            group = input("Введіть назву групи для видалення: ")
            if group in groups:
                del groups[group]
                print("Групу видалено")
            else:
                print("Такої групи не знайдено")

        elif choice == '9':
            input_groups = input("Введіть назви груп через пробіл (наприклад: КС-21 КН-23): ").split()
            heads_set = set(groups[g]['head'] for g in input_groups if g in groups)
            print(f"Множина ПІБ старост: {heads_set}")

        elif choice == '10':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний ввід. Оберіть від 1 до 10")
main_menu()