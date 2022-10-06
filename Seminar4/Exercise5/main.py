fin1 = open("Seminar4\Exercise5\input.txt", encoding="utf8") 
fin2 = open("Seminar4\Exercise5\input1.txt", encoding="utf8")
fout = open("Seminar4\Exercise5\output.txt", "w", encoding="utf8")
m1, m2 = list(fin1.readline().strip().split()), list(fin2.readline().strip().split())
my_dict = dict()
for i in range(0, len(m1), 2):                        #заполняем словарь первым многочленом
    num = list(m1[i].split("x^"))
    if len(num) == 1:                                   #проверка на х^0 и х^1
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
    if i != 0 and m1[i - 1] == '-':
        value = -value
    my_dict[n] = my_dict.get(n, 0) + value

for i in range(0, len(m2), 2):                #заполняем словаpь вторым многочленом
    num = list(m2[i].split("x^"))
    if len(num) == 1:
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
    if i != 0 and m2[i - 1] == '-':
        value = -value
    my_dict[n] = my_dict.get(n, 0) + value
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
