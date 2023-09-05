import random
list1 = []
f = 0
a = int(input("Введите количество строк "))
b = int(input("Введите количество столбцов "))
for i in range(a):
    list2 = []
    for j in range(b):
        f = random.randint(-10, 10)
        list2.append(f)
    list1.append(list2)
for i in list1:
    print(i)
k = 0
maxx = 0
for i in list1:
    print(i[k])
    if maxx < i[k]:
        maxx = i[k]
    k += 1
print("Максимальный элемент диоганали матрицы - ", maxx)