def horizontal(f):
    for i in range(3):
        res = False
        for j in range(1, 3):
            if f[i][j] != f[i][0] or f[i][j] == "-":
                res = True
        if not res:
            return False
    return True


def vertical(f):
    for j in range(3):
        res = False
        for i in range(1, 3):
            if f[i][j] != f[0][j] or f[i][j] == "-":
                res = True
        if not res:
            return False
    return True


def diagonal(f):
    res1 = False
    for i in range(1, 3):
        if f[i][i] == '-' or f[i][i] != f[0][0]:
            res1 = True
    res2 = False
    for i in range(3):
        if f[2 - i][i] == '-' or f[2 - i][i] != f[2][0]:
            res2 = True
    return res1 and res2


def checking(f):
    return horizontal(f) and diagonal(f) and vertical(f)


def my_print(f):
    for i in f:
        print("\t".join(i))
