# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import choice, randint

bank = 201
limit = 28
player_1 = input('Имя игрока: ')
player_2 = 'Бот'

turn = choice([player_1, player_2])

while bank:
    if turn == player_1:
        turn = player_2
    else:
        turn = player_1

    if turn == player_1:
        n = input(f'{turn}, ваш ход: ')
        while not (n.isdigit() and int(n) > 0):
            n = input('Введите целое положительное число: ')
        while not int(n) <= limit:
            n = input(f'По условию вы не можете взять больше {limit} конфет. '
                      f'Попробуйте ещё раз: ')
        while not int(n) <= bank:
            n = input(f'Вы пытаетесь взять больше конфет, чем осталось на столе. Вы можете взять не более {bank}. '
                      f'Попробуйте ещё раз: ')

    else:
        if bank <= 28:
            n = bank
        elif bank % (limit + 1):
            n = bank % (limit + 1)
        else:
            n = randint(1, 28)
        print(f'Ход бота: {n}')

    bank -= int(n)
    print(f'Конфет осталось: {bank}')

print(f'{turn} победил(а)!')