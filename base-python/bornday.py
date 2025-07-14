year = input("Введите год рождения А.С Пушкина: ")
if year.isdigit():
    year = int(year)
    if year == 1799:
        day = input("Введите день рождения А.С Пушкина: ")
        if day.isdigit():
            day = int(day)
            if day == 6:
                print('Верно')
            else:
                print('Неверный день рождения')
        else:
            print('Это вообще не день -.-')
    else:
        print('Неверный год')
else:
    print('Это вообще не год -.-')