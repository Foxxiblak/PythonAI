res = input("Введите последовательность через разделитель ',' ';' '/' : ")
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

siq = list(set(siq))
print(siq)