import tkinter as tk
from tkinter import messagebox
import math

def calculate(event=None):
    
    """
    y = tg(x / (1 - e^x)),  якщо x <= 0
    y = sqrt(ln(x - 3)),     якщо x > 1
    """

    try:
        x = float(entry_x.get())
    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректне числове значення")
        return

    lbl_subfunc.config(text="Підфункція: ")
    lbl_result.config(text="Результат: ", fg="black")


    if x <= 0:
        lbl_subfunc.config(text="Підфункція: y = tg( x / (1 - e^x) )")
        
        if x == 0:
            lbl_result.config(text="Помилка: Знаменник (1 - e^x) дорівнює нулю при x = 0", fg="red")
        else:
            try:
                arg = x / (1 - math.exp(x))
                
                # Переводимо аргумент із градусів у радіани
                y = math.tan(math.radians(arg))
                
                lbl_result.config(text=f"Результат: y = {y:.4f}", fg="green")
            except OverflowError:
                lbl_result.config(text="Помилка: Переповнення при обчисленні експоненти", fg="red")
            except Exception as e:
                lbl_result.config(text=f"Непередбачена помилка: {e}", fg="red")

    elif x > 1:
        lbl_subfunc.config(text="Підфункція: y = sqrt( ln(x - 3) )")
        
        if x <= 3:
            lbl_result.config(text="Помилка: Аргумент логарифма (x - 3) має бути строго більше 0", fg="red")
        else:
            try:
                ln_val = math.log(x - 3)
                
                # Перевірка області визначення квадратного кореня
                if ln_val < 0:
                    lbl_result.config(text="Помилка: Підкореневий вираз ln(x - 3) від'ємний. (x має бути >= 4)", fg="red")
                else:
                    y = math.sqrt(ln_val)
                    lbl_result.config(text=f"Результат: y = {y:.4f}", fg="green")
            except Exception as e:
                lbl_result.config(text=f"Непередбачена помилка: {e}", fg="red")
                
    else:
        lbl_subfunc.config(text="Підфункція: Не визначена для (0 < x <= 1)")
        lbl_result.config(text="Помилка: x не входить до області визначення жодної з гілок", fg="red")


# --- Графічний інтерфейс ---
root = tk.Tk()
root.title("Перше завдання")
root.geometry("500x250")
root.resizable(False, False)

padding = {'padx': 10, 'pady': 5}

tk.Label(root, text="Введіть значення аргументу x:", font=("Arial", 13)).pack(**padding)

entry_x = tk.Entry(root, font=("Arial", 13), width=15)
entry_x.pack(**padding)

btn_calc = tk.Button(root, text="Обчислити", font=("Arial", 13, "bold"), command=calculate)
btn_calc.pack(**padding)
root.bind('<Return>', calculate)

lbl_subfunc = tk.Label(root, text="Підфункція: ", font=("Arial", 13, "italic"))
lbl_subfunc.pack(**padding)

lbl_result = tk.Label(root, text="Результат: ", font=("Arial", 13, "bold"), wraplength=480)
lbl_result.pack(**padding)

root.mainloop()