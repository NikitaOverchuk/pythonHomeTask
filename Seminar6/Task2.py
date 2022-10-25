# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# nums = list(map(int, input().split()))
# res1 = set()
# res2 = set()
# for i in nums:
#     if i in res1:
#         res2.add(i)
#     else:
#         res1.add(i)
# print(*sorted(res1 - res2))

nums = list(map(int, input().split()))
print(*filter(lambda x: nums.count(x) == 1, nums))
