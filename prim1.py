def registr1(func):
    def wrapper(*x):
        y = func(*x)
        y = list(y.split(" "))
        y[1] = str(y[1]).upper()
        y = str(y[0]) + " " + str(y[1])
        print(y)
    return wrapper
@registr1
def hello(x):
     return "Привет "+x
x = input("Введите имя ")
hello(x)
