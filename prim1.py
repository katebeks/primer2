import random


def Gen(a,b):
    global mass
    mass = []
    for i in range(10):
        mass.append(random.randint(a, b))
a = int(input("Введите начало диопазона "))
b = int(input("Введите конец диопазона "))
Gen(a,b)
print(mass)