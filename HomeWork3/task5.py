# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
lst = [0, 1, 1, ]
n = input("Задайте число: ")
n = int(n)
fib1 = 1
fib2 = 1
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    lst.append(fib_sum)
    i = i + 1
lst2 = []
for i in range(0,len(lst)):
    v = (lst[i]*-1)
    lst2.append(v)
lst_rev = list(reversed(lst2))
lst_result = lst_rev + lst
lst_result.remove(0)
print(lst_result)