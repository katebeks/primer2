list1 = [1,7,3,3,2,5,6,1,5,8,1,5,1,2,3,5,7,8]
print(list1)
a = int(input("Введите начало интервала "))
b = int(input("Введите конец интервала "))
#list2 = []
for i in range(len(list1)-1, 0, -1):
    for j in range(a, (b+1)):
        if list1[i] == j:
            list1.remove(list1[i])
print(list1)