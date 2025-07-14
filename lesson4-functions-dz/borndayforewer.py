"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
year_ask = 'Ввведите год рождения А.С.Пушкина: '
day_ask = 'Ввведите день рождения Пушкина: '
success = 'Верно'
fail = 'Не верно'
def print_ask(ask):
    return input(ask)

def print_res(text):
    print(text)

def ask_year():
    year = print_ask(year_ask)
    while year != '1799':
        print_res(fail)
        year = print_ask(year_ask)

def ask_day():
    day = print_ask(day_ask)
    while day != '6':
        print_res(fail)
        day = print_ask(day_ask)

ask_year()
ask_day()
print_res(success)
