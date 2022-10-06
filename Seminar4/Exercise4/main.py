# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randrange, choice


k = int(input())
sign = ("+", "-")
f_out = open("Seminar4\Exercise4\output.txt", "w", encoding="utf8")
print(randrange(-100, 101), "*x**", k, sep="", end=f" {choice(sign)} ", file=f_out)
for i in range(k - 1, 1, -1):
    n = randrange(0, 101)
    if n != 0:
        print(n, "*x**", i, sep="", end=f" {choice(sign)} ", file=f_out)
q = randrange(-100, 101)
if q != 0:
    print(q, "*x", sep="", end=" ", file=f_out)
m = randrange(0, 101)
if m != 0:
    print(f'{choice(sign)}', m, end=" ", file=f_out)
print("= 0", file=f_out)
f_out.close()
