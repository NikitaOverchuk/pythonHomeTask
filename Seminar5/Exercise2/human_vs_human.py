# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


candy = 100
print("Приветствую Вас, Игрок1 и Игрок2")
gamer_1 = input("Игрок1, как я могу обращаться к Вам? ")
gamer_2 = input("Игрок2, представьтесь, пожалуйста:) ")
turn = [gamer_1, gamer_2]
human_1 = random.choice(turn)
turn.remove(human_1)
human_2 = turn[0]
while candy != 0:
    print(f"На столе лежит {candy} конфет(а)")
    print(f"{human_1}, сколько Вы хотите забрать? Рекомендую присмотреться к цифре {candy % 29}")
    k = int(input())
    while k > 28 or k < 1:
        print(f"Вы ввели {k},а нужно число от 1 до 28 включительно.Пожалуйста, сделайте это снова, только правильно:)")
        k = int(input())
    candy -= k
    if candy == 0:
        print(f"{human_1}, Вы выиграли. Поздравляю!!!")
        break
    else:
        print(f"На столе осталось {candy} конфет(а)")
        print(f"{human_2}, сколько Вы хотите забрать?")
        l = int(input())
        while l > 28 or l < 1:
            print(
                f"Вы ввели {l},а нужно число от 1 до 28 включительно.Пожалуйста, сделайте это снова, только правильно:)")
            l = int(input())
        candy -= l
        if candy == 0:
            print(f"{human_2}, Вы победили. Мои поздравления :)!!!")
            break