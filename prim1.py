def registr1(func):
    def wrapper():
        y = func()
        #print(y)
        #y = list(y.split(" "))
        y = str(y).upper()
        #y = str(y[0]) + " " + str(y[1])
        print("Привет "+y)
    return wrapper
@registr1
def hello():
    x = input("Введите имя ")
    print("Привет "+x)
    return x

hello()