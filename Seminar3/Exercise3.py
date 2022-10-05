# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

maxNum, minNum, nums = 0, 0, input().split()
for i in nums:
    if not(i.isdigit()):
        i = float(i) % 1
        if i > maxNum:
            maxNum = i
        elif i < minNum or minNum == 0:
            minNum = i
print(round(maxNum - minNum, 2))
