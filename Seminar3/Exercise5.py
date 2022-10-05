# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input())
resPos = [0, 1]
resNeg = [0, 1]
for i in range(n - 1):
    resPos.append(resPos[-1] + resPos[-2])
    resNeg.append(resNeg[-2] - resNeg[-1])
resNeg.reverse()
resNeg.pop()
resNeg.extend(resPos)
print(resNeg)
