# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
lst1 = [random.randint(-9, 9) for i in range(6)]
lst2 = []
print(lst1)
for i in range(len(lst1)//2):
    x = lst1[i]*lst1[len(lst1)-i-1]
    lst2.append(x)
print(lst2)