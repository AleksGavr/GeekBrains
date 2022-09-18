# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *
import time


def play_game(steps, balance, players):
    print(f'{players}, сколько конфет возьмете?')
    if players == 'Бот':
        if balance == 28:
            move = 28
        else:
            move = balance % 28 - 1
            if move == 0:
                move = 1
    else:
        move = int(input())
    if move > steps or move > balance:
        print(f'За один ход можно брать не более {steps}, всего у нас {balance}.')
        play_game(steps, balance, players)
    else:
        balance = balance - move
        if balance > 0:
            print(f'Осталось {balance}')
            if players == player1:
                players = player2
            else:
                players = player1
            play_game(steps, balance, players)
        else:
            print('Все конфеты разобраны.')
            print(f'{players}, Вы выиграли, можете забрать все конфеты!')


print('\n' * 10)
print('Правила игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n Первый ход '
      'определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются '
      'сделавшему последний ход.')
print('\n' * 2)

step = 28
total = 2021

player1 = input('Ваше имя?\n')
player2 = 'Бот'
print(f'{player1}, Вы играете против бота')

print('Бросим жребий')
time.sleep(2)

x = randint(0, 1)
if x == 1:
    player = player1
else:
    player = player2

print(f'{player} Вы ходите первым!')

play_game(step, total, player)
