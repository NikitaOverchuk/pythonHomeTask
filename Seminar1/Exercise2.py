myList = []
for i in range(1, -1, -1):
    for j in range(1, -1, -1):
        for k in range(1, -1, -1):
            myList.append([bool(i), bool(j), bool(k)])
print("not(x or y or z) == (not(x) and not(y) and not(z))")
for i in myList:
    print(f"x = {i[0]} \t y = {i[1]} \t z = {i[2]}")
    print(not(i[0] or i[1] or i[2]) == (not(i[0]) and not(i[1]) and not(i[2])))
    print()
