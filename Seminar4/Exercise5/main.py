def fill_dict(m):
    for i in range(0, len(m), 2):                   # заполняем словарь многочленами
        num = list(m[i].split("x^"))
        if len(num) == 1:                              # проверка на х^0 и х^1
            if num[0].isdigit():
                num.append(0)
            else:
                num = num[0].split("x")
        value, n = num
        if value == '':
            value = 1
        if n == '':
            n = 1
        value, n = int(value), int(n)
        if i != 0 and m[i - 1] == '-':
            value = -value
        my_dict[n] = my_dict.get(n, 0) + value


fin1, fin2 = open("input.txt", encoding="utf8"), open("input1.txt", encoding="utf8")
fout = open("output.txt", "a", encoding="utf8")
mnog1, mnog2, my_dict = list(fin1.readline().strip().split()), list(fin2.readline().strip().split()), dict()
fill_dict(mnog1)
fill_dict(mnog2)
lst = list(my_dict.items())
lst.sort(reverse=True)
print(lst[0][1], "x^", lst[0][0], sep="", end=" ", file=fout)          # выводим первый одночлен, чтобы +\- в начале писать
for i in lst:
    if i[1] != 0:
        if i[1] < 0:
            print("- ", abs(i[1]), "x^", i[0], sep="", end=" ", file=fout)
        else:
            print("+ ", i[1], "x^", i[0], sep="", end=" ", file=fout)
fout.close()
