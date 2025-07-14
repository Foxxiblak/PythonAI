vegetable_name = 'Tomato' #str, название
vegetable_weight = 0.3 #float, вес
vegetable_color = 'red' #str, цвет
vegetable_is_edible = True #boolean, съедобен ли
vegetable_is_root = False #boolean, корнеплод ли
vegetable_percentage_water = 80 #int ex. 80% => 80, процент содержащийся воды

print(f'Овощ: {vegetable_name}, {type(vegetable_name)}')
print(f'Вес: {vegetable_weight}, {type(vegetable_weight)}')
print(f'Цвет: {vegetable_color}, {type(vegetable_color)}')
print(f'Овощ съедобен: {vegetable_is_edible}, {type(vegetable_is_edible)}')
print(f'Это корнеплод: {vegetable_is_root}, {type(vegetable_is_root)}')
print(f'Процент воды: {vegetable_percentage_water}%, {type(vegetable_percentage_water)}')


