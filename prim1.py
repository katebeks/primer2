x = int(input("Введите число "))
k = 0
a1 = 0
a2 = 1
a3 = 0
while k < x:
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3
    k += 1
#print("Результат - ", y)
