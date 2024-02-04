# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()

# Задание списка городов
cities = ['Москва', 'Санкт-Петербург']

# Задание словаря, где ключом является город, а значением - список магазинов
shops = {'Москва': ['М1', 'М2', 'М3', 'М4'], 'Санкт-Петербург': ['СПб1', 'СПб2']}

# Создание функции, которая обновляет значение выпадающего списка магазинов
def update_shops(*args):
    selected_city = city_var.get()
    shop_menu['values'] = shops[selected_city]
    shop_var.set(shops[selected_city][0])

# Создание переменной для хранения выбранного города и привязка ее к выпадающему списку
city_var = tk.StringVar(value=cities[0])
city_menu = ttk.Combobox(root, textvariable=city_var, values=cities, state='readonly')
city_menu.grid(row=0, column=0)

# Создание переменной для хранения выбранного магазина и привязка ее к выпадающему списку
shop_var = tk.StringVar(value=shops[cities[0]][0])
shop_menu = ttk.Combobox(root, textvariable=shop_var, state='readonly')
shop_menu.grid(row=0, column=1)

# Привязка функции обновления магазинов к изменению значения города
city_var.trace('w', update_shops)

# Запуск главного цикла обработки событий
root.mainloop()
