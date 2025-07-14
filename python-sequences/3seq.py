res_1 = input("Введите 1 последовательность через разделитель ',' ';' '/' : ")
res_2 = input("Введите 2 последовательность через разделитель ',' ';' '/' : ")
def get_siq(res):
    if res.find(',') != -1:
        res = res.split(',')
    elif res.find(';') != -1:
        res = res.split(';')
    elif res.find('/') != -1:
        res = res.split('/')
    else:
        res = res.split()

    siq = []
    for i in res:
        if i.isdigit():
            siq.append(int(i))
    return set(siq)

set_1 = get_siq(res_1)
set_2 = get_siq(res_2)

print("Последовательность 1: ", res_1)
print("Последовательность 2: ", res_2)

set_3 = set_1.difference(set_2)
print("Результат: ", list(set_3))

