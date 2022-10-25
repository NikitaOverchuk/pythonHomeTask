# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randrange, choice


k = int(input())
sign = ("+", "-")
f_out = open("input.txt", "w", encoding="utf8")
print(randrange(-100, 101), "*x^", k, sep="", end=" ", file=f_out)
for i in range(k - 1, -1, -1):
    n = randrange(0, 101)
    if n != 0:
        if i == 1:
            print(f"{choice(sign)} ", n, "*x", sep="", end=" ", file=f_out)
        elif i == 0:
            print(f'{choice(sign)}', n, end=" ", file=f_out)
        else:
            print(f"{choice(sign)} ", n, "*x^", i, sep="", end=" ", file=f_out)
print("= 0", file=f_out)
f_out.close()
