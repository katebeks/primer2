str1 = "lakjfnv;ha z dhfnv jan;kjdfnv lknlkdfb  alkdfjblka"
list1 = list(str1)
print(list1)
for i in range(len(list1)-1, -1,-1):
    if list1.count(list1[i]) > 1:
        list1.pop(i)
list1 = tuple(list1)
print(list1)