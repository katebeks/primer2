f = open("primer.txt", 'a')
y = 0
while y!=1:
    t = input("Введите строку ")
    if t == "":
        y = 1
    else:
        f.write(t + "\n")
f.close()