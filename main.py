import tkinter as tk
from tkinter import messagebox

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def add_number():
    try:
        number = float(entry.get())
        data.append(number)
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите число.")

def show_average():
    average = calculate_average(data)
    result_label.config(text=f'Среднее значение: {average}')
    data_label.config(text=f'Введенные данные: {data}')

# Основное окно
root = tk.Tk()
root.title("Среднее значение")

data = []

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Добавить", command=add_number)
add_button.pack(side=tk.LEFT, padx=5)

average_button = tk.Button(root, text="Показать среднее", command=show_average)
average_button.pack(pady=10)

data_label = tk.Label(root, text="Введенные данные: []")
data_label.pack()

result_label = tk.Label(root, text="Среднее значение: 0")
result_label.pack()

root.mainloop()
