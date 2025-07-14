input_item = True
res = []
print('-.' * 50)
print('Вводите элементы последовательности по одному. Для прекращения ввода введите пустую строку.')
print('-.' * 50)
while input_item:
    item = input('Введите числовой элемент последовательности: ')
    if item.isdigit():
        res.append(int(item))
    elif item == '':
        input_item = False
    else:
        item = input('Элемент не является числовым!')

print(f'Ваш список элементов: {res}')
res.sort()
print(f'Ваш список отсорттрован: {res}')