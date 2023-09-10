import math
import random
def krug():
    k = int(input("Введите радиус круга - "))
    k = math.pi * k*k
    return (k)

def priamoug():
    a = int(input("Введите сторону 1 прямоугольника - "))
    b = int(input("Введите сторону 2 прямоугольника - "))
    k = a * b
    return (k)

def treug():
    a = int(input("Введите 1 сторону треугольника "))
    b = int(input("Введите 2 сторону треугольника "))
    c = int(input("Введите 3 сторону треугольника "))
    p = (a + b + c)/2
    k = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return (k)
print("Сделайте выбор:\n1. Найти площадь круга\n2. Найти площадь прямоугольника\n3. Найти площадь треугольника")
v = int(input())
if v == 1:
    print("Площадь круга ", krug())
elif v == 2:
    print("Площадь прямоугольника ", priamoug())
elif v == 3:
    print("Площадь треугольника ", treug())
else:
    print("Такого варианта нет")