import random
list1 = []
f = 0
a = int(input("Введите количество строк "))
b = int(input("Введите количество столбцов "))
for i in range(a):
    list2 = []
    for j in range(b):
        f = random.randint(-9, 9)
        list2.append(f)
    list1.append(list2)
for i in list1:
    print(i)
k = 0
rez = 0
o = 0
for i in range(1,a):
    for j in range(k+1):
        o = list1[i][j]
        if o < 0:
            rez += 1
    k += 1
print("Кооличество чисел меньше 0 под главной диагональю - ", rez)