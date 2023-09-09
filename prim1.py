list1 = [5, "dog cat mam house mam", "cat mam dad milk", "dad mam dog", "cat cat mam cat", "dog cat house mam"]
str1 = ""
list2 = []
for i in list1:
    print(i)
for i in range(1, list1[0]+1):
    if i == list1[0]:
        str1 = str1 + list1[i]
    else:
        str1 = str1 + list1[i] + " "
list2 = list(str1.split(" "))
#print(list2)
list3 = list(set(list2))
list3.sort()
print(list3)
obj1 = dict()
for i in list3:
    j = list2.count(i)
    obj1[i] = j
maxx = 0
keyy = ""
for key, val in obj1.items():
    print(key, "-", val )
    if maxx < val:
        maxx = val
        keyy = key
print("Слово, которое встречается чаще всего - ", keyy)
