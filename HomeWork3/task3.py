# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.(если получаются длинные числа после запятой,
# это нормально и особенность данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20)
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
lst2 = [(round(random.random()*10, 2)),(round(random.random()*10, 2)),(round(random.random()*10, 2)),
        (round(random.random()*10, 2)),(round(random.random()*10, 2)),(round(random.random()*10, 2))]
print(lst2)
min_num = min(lst2)
max_num = max(lst2)
print(f'max = {max_num}, min = {min_num}')
print(f'Разница: {max_num%1 - min_num%1}')