# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
player_1 = 0
player_2 = 0
sum = 121
num = [-1, 1]
lot = random.choice(num)
def players(lot, sum):
    while sum>0:
        if lot == 1:
            player_1 = int(input(f'Игрок 1 ведите число конфет: '))
            if 29 > player_1 > 0:
                sum = sum - player_1
                if sum <= 29:
                    print('Игрок 1 победил!')
                    break
                print(f'Осталось конфет {sum}')
                lot = lot * -1
            else: print('Ошибка! Введите количество от 1 до 28')
        if lot == -1:
            player_2 = int(input(f'Игрок 2 ведите число конфет: '))
            if 29 > player_2 > 0:
                sum = sum - player_2
                if sum <= 29:
                    print('Игрок 2 победил!')
                    break
                print(f'Осталось конфет {sum}')
                lot = lot * -1
            else:
                print('Ошибка! Введите количество от 1 до 28')
    return (sum)

def easy_bot(lot, sum):
    while sum>0:
        if lot == 1:
            player_1 = int(input(f'Игрок 1 ведите число конфет: '))
            if 29 > player_1 > 0:
                sum = sum - player_1
                if sum <= 29:
                    print('Игрок 1 победил!')
                    break
                print(f'Осталось конфет {sum}')
                lot = lot * -1
            else: print('Ошибка! Введите количество от 1 до 28')
        if lot == -1:
            player_2 = random.randint(1,28)
            print(f'Ходит бот.. он забирает {player_2} конфет')
            sum = sum - player_2
            if sum <= 29:
                print('Бот победил!')
                break
                print(f'Осталось конфет {sum}')
            lot = lot * -1
        print(f'Осталось конфет {sum}')
    return (sum)

def hard_bot(lot, sum):
    while sum>0:
        if lot == 1:
            player_1 = int(input(f'Игрок 1 ведите число конфет: '))
            if 29 > player_1 > 0:
                sum = sum - player_1
                if sum <= 29:
                    print('Игрок 1 победил!')
                    break
                print(f'Осталось конфет {sum}')
                lot = lot * -1
            else: print('Ошибка! Введите количество от 1 до 28')
        if lot == -1:
            player_2 = sum % 29
            if player_2 == 0:
                player_2 = random.randint(1,28)
            print(f'Ходит бот.. он забирает {player_2} конфет')
            sum = sum - player_2
            if sum <= 29:
                print('Бот победил!')
                break
            print(f'Осталось конфет {sum}')
            lot = lot * -1
    return (sum)

print(' C кем хотите сыграть? 1 - игрок, 2 - легкий бот, 3 - сложный бот: ',end='')
a = int(input())
if a == 1:
    print('С помощью жребия мы определим игрока, который ходит первым.')
    print('Бросаем монетку...')
    players(lot, sum)

if a == 2:
    print('С помощью жребия мы определим игрока, который ходит первым.')
    print('Бросаем монетку...')
    easy_bot(lot,sum)

if a == 3:
    print('С помощью жребия мы определим игрока, который ходит первым.')
    print('Бросаем монетку...')
    hard_bot(lot,sum)