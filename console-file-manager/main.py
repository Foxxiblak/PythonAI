from system_module.file_func import *
from games.victory import start_game
from games.bank import start_game as start_bank
import sys

def add_separators(func):
    def inner(*args, **kwargs):
        print('-.' * 30, end='-\n')
        res = func(*args, **kwargs)
        print('-.' * 30, end='-\n')
        return res
    return inner

@add_separators
def print_menu():
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. сохранить содержимое рабочей директории в файл')
    print('6. посмотреть только папки')
    print('7. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. выход')
    return input('Что выбираем? ')

def parse_menu(value):
    match(value):
        case '1':
            create_folder()
        case '2':
            delete_folder()
        case '3':
            copy_file_or_folder()
        case '4':
            show_list_dir()
        case '5':
            save_list_dir()
        case '6':
            show_forders()
        case '7':
            show_files()
        case '8':
            get_os()
        case '9':
            get_dev()
        case '10':
            start_game()
        case '11':
            start_bank()
        case'12':
            sys.exit(0)
        case _:
            print('Введено что-то не то :( ')


while True:
    value = print_menu()
    parse_menu(value)
