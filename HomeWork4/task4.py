#Задана натуральная степень k.
#Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
import random


k = int(input('Введите натуральную степень k: '))
lst_koef = []
lst1 = []
res = []
str_res=''
while k > -1:
    if k > 1:
        lst_koef.append(random.randint(0, 101))
        lst1.append(f'x^{k}')
    elif k == 1:
        lst_koef.append(random.randint(0, 101))
        lst1.append(f'x')
    elif k == 0:
        lst_koef.append(random.randint(0, 101))
        lst1.append('')
    k-=1
for i in range(0, len(lst_koef)):
    if lst_koef[i] == 1 and i<len(lst_koef)-1:
        res.append(lst1[i])
    elif lst_koef[i] == 0:
        continue
    res.append(str(lst_koef[i]) + (lst1[i]))
    if lst1[i] == '':
        continue
for i in range(0,len(res)):
    if i < len(res)-1:
        str_res+=str(res[i])+'+'
    elif i == len(res)-1:
        str_res+=str(res[i])+'=0'
file = open("test.txt", "w")
file.write(str_res)
file.close()