year = input("Введите год рождения А.С Пушкина: ")
if year.isdigit():
    year = int(year)
    if year == 1799:
        print('Верно')
    else:
        print('Неверно')
else:
    print('Это вообще не год -.-')