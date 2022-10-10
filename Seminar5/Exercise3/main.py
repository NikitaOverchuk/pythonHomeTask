import my_functions


print('Добро пожаловать в игру "Крестики-Нолики"')
field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
my_functions.my_print(field)
sign1, sign2 = input("Игрок 1, чем предпочитаете играть: X или 0? "), 0
if sign1 == "X":
    sign2 = "0"
else:
    sign2 = "X"
gamer = 0
print("Только помните: задавайте 2 числа от 0 до 2 через пробел, потому что здесь все как в матрицах")
for k in range(9):
    if k % 2 == 0:
        print("Игрок 1, сделайте Ваш ход")
        i, j = list(map(int, input().split()))
        field[i][j] = sign1
    else:
        print("Игрок 2, теперь Ваш черед")
        i, j = list(map(int, input().split()))
        field[i][j] = sign2
    my_functions.my_print(field)
    if not my_functions.checking(field):
        gamer = k
        break
if gamer == 0:
    print("Дружеская ничья!")
elif gamer % 2 == 0:
    print("Игрок 1 был сильнее, мои поздравления!")
else:
    print("Поздравляю Игрока 2 с победой!")
