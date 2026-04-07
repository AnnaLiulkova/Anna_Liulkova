def print_p_letters(n):
    if not (1 <= n <= 9):
        print("Число має бути від 1 до 9.")
        return

    row1 = " ___  " * n
    row2 = "".join([f"| {i} \\ " for i in range(1, n + 1)])
    row3 = "|___/ " * n
    row4 = "|     " * n
    row5 = "|     " * n
    row6 = "|     " * n

    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)

print_p_letters(6)