"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

import os
import json

def add_money():
    num = input('Введите сумму для добавления на счет: ')
    return float(num) if num.isdigit() else 0.0

def purchase(bank_account):
    num = input('Введите сумму покупки: ')
    if num.isdigit():
        if float(num) > bank_account:
            print('\n!!! Недостаточно средств на счёте !!!\n')
            return False
        else:
            name = input('Введите название товара: ')
            return [float(num), name]
    else:
        print('Это не число. Введите число.')
        return False


def print_history(history):
    print('*-' * 30)
    if len(history) == 0:
        print('Пока покупок нет.')
    else:
        for item in history:
            print(f'Вы купили {item["product"]}: {item["ammount"]}')
    print('*-' * 30)

def read_history():
    if os.path.exists('history.json'):
        with open('history.json', 'r') as file:
            res = json.load(file)
            print(res)
            return [res["history"], res["bank_account"]]
    else:
        return [[], 0.0]

def write_history(history, bank_account):
    with open('history.json', 'w') as file:
        json.dump({'history': history, 'bank_account': bank_account}, file)

def start_game():
    exit = False
    read_file_res = read_history()
    history = read_file_res[0]
    bank_account = read_file_res[1]

    while exit == False:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Состояние счета: {bank_account}')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            bank_account += add_money()
        elif choice == '2':
            res = purchase(bank_account)
            if res != False:
                bank_account -= res[0]
                history.append({'product': res[1], 'ammount': res[0]})
        elif choice == '3':
            print_history(history)
        elif choice == '4':
            write_history(history, bank_account)
            exit = True
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    start_game()