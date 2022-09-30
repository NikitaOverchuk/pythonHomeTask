# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
myList = list(map(int, input().split()))
res = []
for i in range(-myList[0], myList[0] + 1):
    res.append(i)
print(*res)
print(res[myList[1] + 1] * res[myList[2] + 1])
