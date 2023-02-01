# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# d = int(input('Введите число d: '))
# e = int(input('Введите число e: '))
#
# numbers = [a, b, c, d, e]
# print(numbers)
#
# def max_numbers(numbers):
#     return max(numbers)
# print(max_numbers(numbers))
# def max_numbers(num):
#     return max(num)
data = list(map(int,input('Введите числа через пробел: ').split()))
print(data)
list = [x for x in data if x == max(data)]
print(*list)