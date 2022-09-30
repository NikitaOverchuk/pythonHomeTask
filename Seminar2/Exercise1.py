# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = tuple(input())
res = 0
for i in n:
    if i.isdigit():
        res += int(i)
print(res)
