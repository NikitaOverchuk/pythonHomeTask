# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

nums = list(map(int, input().split()))
res = []
for i in range(len(nums) // 2):
    res.append(nums[i] * nums[-(i + 1)])
if len(nums) % 2 != 0:
    res.append((nums[len(nums) // 2])**2)
print(*res)