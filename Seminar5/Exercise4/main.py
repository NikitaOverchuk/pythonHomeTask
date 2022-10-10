# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

fin = open("Seminar5\Exercise4\input.txt", encoding="utf8")
fout = open('Seminar5\Exercise4\output.txt', 'w', encoding='utf8')
line = fin.readline().strip()


def f(a):
    result, k, res = [], 0, [[1, a[0]], ]
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            res.append([1, a[i]])
            k += 1
        else:
            res[k][0] += 1
    for i in res:
        result.append(('9' + i[1]) * (i[0] // 9) + str(i[0] % 9) + i[1])
    return ''.join(result)


def p(b):
    result = []
    for i in range(1, len(b), 2):
        result.append(b[i] * int(b[i - 1]))
    return ''.join(result)


changed_line = f(line)
line_back = p(changed_line)
print(changed_line, file=fout)
print(line_back, file=fout)
print(line == line_back, file=fout)
fout.close()
