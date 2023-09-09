f = open("primer.txt", 'r')
list1 = f.readlines()
print(list1)
str1 = ""
summ = 0
list3 = []
for i in range(len(list1)):
    str1 = list1[i]
    str1.replace("\n", "")
    print(str1)
    list2 = str1.split(" ")
    summ += int(list2[2])
    if int(list2[2]) < 3:
        list3.append(i)
srb = summ/len(list1)
print("Средний балл класса - ", srb)
print("Оценки меньше 3 баллов:")
for i in list3:
    print(list1[i])
f.close()