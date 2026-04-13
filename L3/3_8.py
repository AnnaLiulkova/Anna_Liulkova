def find_treasure():
    x, y = 0, 0
    print("Введіть шлях (наприклад, 'North 7'). Для завершення введіть 'Treasure!':")
    
    while True:
        line = input().strip()
        if line == "Treasure!":
            break
        
        try:
            direction, steps = line.split()
            steps = int(steps)
            
            if direction == "North": y += steps
            elif direction == "South": y -= steps
            elif direction == "East": x += steps
            elif direction == "West": x -= steps
        except (ValueError, IndexError):
            print("Некоректний формат. Спробуйте ще раз")
            
    print(f"Координати скарбу: {x} {y}")

find_treasure()