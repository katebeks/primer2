a = int(input("Введите минимальный  элемент "))
b = int(input("Введите максимальный  элемент "))
sum1 = 0
for i in range(a+1,b):
    sum1 += i
print(" Сумма элементов = ", sum1)