with (open("primer.txt", 'r', encoding='utf-8') as f):
    list1 = f.readlines()
    print(list1)
    print("Колличество строк - ", len(list1))
    m = 1
    for i in list1:
        print("Символов в ", m, " строке - ", len(i.replace("\n", '')))
        list2 = list(i.split(" "))
        print("Слов в ", m, " строке - ", len(list2))
        m += 1

