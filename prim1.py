str1 = "текст слова мама папа слова текст если много мама что текст слова мама бабушка тетя"
list1 = list(str1.split(" "))
print(list1)
list2 = list(set(list1))
print(list2)
obj1 = dict()
for i in list2:
    j = list1.count(i)
    obj1[i] = j
for key, val in obj1.items():
    print(key, "-", val )
