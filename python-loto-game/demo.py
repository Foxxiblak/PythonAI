def range(start, end):
    res = []
    if start > end:
        help = start
        start = end
        end = help
    elif start == end:
        return [start]

    i = start
    while i < end:
        res.append(i)
        i += 1
    return res

print(range(-2,-2))
print(range(-2,3))
print(range(3,-2))
print(range(0,16))
print(range(6,4))
print(range(-6,-4))
print(range(-3,-7))
print(range(0,-16))



'''
for i in range(6, -1, -1):
    print(i)
print('-' * 30)

for i in range(6, 0, -1):
    print(i)
print('-' * 30)

for i in range(0, 6):
    print(i)
print('-' * 30)

for i in range(-6, 1):
    print(i)
print('-' * 30)

for i in range(-6, 6):
    print(i)
print('-' * 30)

arr=[1, -5, 6, 13, 12, -45, -100, -56, 0, 12, 1, 456, 3, 9, 10, 12, 22, 11, 2000]
result=[]
for i in range(len(arr)) :
  item = arr[i]
  if i>0 :
    item += arr[i-1]
  if i<len(arr)-1:
    item += arr[i+1]
  result.append(item)
print(result)

cat = 'Murka'

match(cat):
    case 'Murka':
        print('Hello Murka')
    case 'Barsik':
        print('Hello Barsik')
    case 'Mars':
        print('Meow')
    case _:
        print('No cat')


print( int(float('15.6')) )

def equel(a, b = 14):
    if a > b:
        print(f'A({a}) > B({b})')
    elif b > a:
        print(f'A({a}) < B({b})')
    else:
        print(f'A({a}) = B({b})')

    str = 'Hello world'
    #i = 0
    #while i < len(str):
    #    print(f' i = {i}: {str[i]}')
    #    i = i + 1

    for i in range(len(str)):
        print(f' i = {i}: {str[i]}')

while True:
    a1 = int(input('Введите число А: '))
    b1 = int(input('Введите число B: '))
    begemot = 100
    equel(begemot, b1)
    equel(7, 8)
    equel(3, 5)
    equel(a1, b1)
    equel(11, 22)
    equel(11*20, 220)
'''