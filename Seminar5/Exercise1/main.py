fin = open("Seminar5\Exercise1\input.txt", encoding="utf8")
fout = open("Seminar5\Exercise1\output.txt", "w", encoding="utf8")
for line in fin:
    words = list(line.strip().split())
    for j in words:
        if j.find("абв") == -1:
            print(j, file=fout, end=" ")
    print(file=fout)
fout.close()
