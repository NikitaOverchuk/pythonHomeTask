# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        n //= i
        print(i, end=" ")
        i = 2
    else:
        i += 1
