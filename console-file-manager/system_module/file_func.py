import os
import json
import shutil
import getpass
import platform


def add_separators(func):
    def inner(*args, **kwargs):
        print('^v' * 13, end='^')
        print(f' {func.__name__} ', end='')
        print('^v' * 13, end='^\n')
        res = func(*args, **kwargs)
        print('^v' * 30, end='^\n')
        return res
    return inner


@add_separators
def create_folder():
    try:
        name = input('Введите название папки: ')
        os.mkdir(name)
    except FileExistsError:
        print(f'Папка "{name}" уже существует!')
    else:
        print(f'Папка "{name}" успешно создана!')

@add_separators
def delete_folder():
    try:
        name = input('Введите название папки: ')
        os.rmdir(name)
    except FileNotFoundError:
        print(f'Папки "{name}" не существует!')
    else:
        print(f'Папка "{name}" успешно удалена!')

@add_separators
def copy_file_or_folder():
    name = input('Введите название копируемой папки/файла: ')
    if not os.path.exists(name):
        print(f'Папки/файла "{name}" не существует!')
        return

    copy = input('Введите название новой папки/файла: ')
    if name == copy:
        print(f'Названия не могут совпадать')
        return

    name = os.path.join(os.getcwd(), name)
    copy = os.path.join(os.getcwd(), copy)

    shutil.copy(name, copy) if os.path.isfile(name) else shutil.copytree(name, copy)
    print(f'Папка/файл успешно скопирован!')

@add_separators
def show_list_dir():
    for item in os.listdir():
        print(f'---> {item}')

@add_separators
def save_list_dir():
    with open('listdir.txt', 'w') as file:
        json.dump({'files': show_files(), 'dirs': show_forders()}, file)

@add_separators
def show_forders():
    folders = []
    for item in os.listdir():
        if os.path.isdir(item):
            folders.append(item)
            print(f'---> {item}')
    return folders

@add_separators
def show_files():
    files = []
    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
            print(f'---> {item}')
    return files

@add_separators
def get_os():
    print(platform.platform())


@add_separators
def get_dev():
    #print(sys.argv[0])
    print(getpass.getuser())