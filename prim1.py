a = [1,7,3,2,2,5,6,4,5,8]
print(a)
sum1 = 0
for i in a:
    sum1 +=i
sum1 = sum1 / len(a)
print("Среднее арифметическое = ",sum1)
for i in a:
    if i< sum1:
        print(i)
#print("Сумма положительных четных элементов = ",sum1)