# Реализуйте алгоритм перемешивания списка.
import random


n = int(input("Введите размер списка: "))
res = []
for i in range(n):
    res.append(i)
print(*res)
for i in range(2 * n):
    k = random.randrange(0, n)
    m = random.randrange(0, n)
    res[k], res[m] = res[m], res[k]
print(*res)
