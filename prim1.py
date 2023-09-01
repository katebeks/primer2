a = float(input("Введите число - "))
b = float(input("Введите число - "))
c = float(input("Введите число - "))
if (a+b > c) and (a+c > b) and (c+b > a):
    print("Существует треугольник со сторонами " + str(a) + " " + str(b) + " " + str(c))
else:
    print("Не существует треугольник со сторонами " + str(a) + " " + str(b) + " " + str(c))