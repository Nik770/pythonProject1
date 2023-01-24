# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = input('Введите текст: ').split()
edit = list(filter(lambda x: not 'абв' in x, text))
print(*edit)