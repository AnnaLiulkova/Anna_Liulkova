def guess_number_game():
    print("Введіть максимальне число n:")
    try:
        n = int(input().strip())
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    possible_numbers = set(range(1, n + 1))
    
    print("Вводьте питання Каті (числа через пробіл) або слово 'Все' для завершення:")
    while True:
        user_input = input().strip()
        if user_input.lower() == "все":
            break
            
        try:
            # перетворюємо введені числа на множину
            question = set(map(int, user_input.split()))
        except ValueError:
            print("Будь ласка, вводьте тільки числа або слово 'Все'.")
            continue
            
        # якщо іван скаже "так", залишаться числа, які є і в possible_numbers, і в question
        yes_set = possible_numbers.intersection(question)
        
        # якщо іван скаже "ні", залишаться числа з possible_numbers, яких немає в question
        no_set = possible_numbers.difference(question)
        
        if len(yes_set) > len(no_set):
            print("Так")
            possible_numbers = yes_set
        else:
            print("Ні")
            possible_numbers = no_set

    sorted_result = sorted(list(possible_numbers))
    
    print("Результат:")
    print(*(sorted_result))

guess_number_game()