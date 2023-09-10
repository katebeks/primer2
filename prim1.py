import random
ch = int(input("Введите число "))
def rang(ch):
    k = 0
    while ch != 0:
        ch = ch // 10
        k +=1
    return (k)
print("Колличество разрядов числа - ", rang(ch))