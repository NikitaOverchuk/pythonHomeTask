# 1. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# lst, word = list(input().split()), input()
# index_1 = lst.index(word)
# if index_1 != -1:
#     print(lst.index(word, index_1 + 1))
# else:
#     print(index_1)

lst, word = list(input().split()), input()
index_1 = -1
index_2 = -1
for i, value in enumerate(lst):
    if value == word:
        if index_1 != -1:
            index_2 = i
            break
        else:
            index_1 = i
print(index_2)
