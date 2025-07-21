import sys
from static.scripts.classifier import vulnerabilities
from models.api import get_response

def print_menu():
    for index, item in enumerate(vulnerabilities, start=1):
        print(f"{index}. {item.class_id} | {item.name} | {item.level.value.upper()} ")

if __name__ == '__main__':
    while True:
        print_menu()
        menu_number = input("Enter vulnerability type number: ")
        if menu_number.isdigit():
            num = int(menu_number)
            if 1 <= num <= 6:
                response = get_response(num - 1)
            elif num == 13:
                print("Exit")
                sys.exit(0)
            else:
                print("Invalid menu item")
        else:
            print("Please enter a number")