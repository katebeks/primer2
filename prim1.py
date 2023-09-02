try:
    n = int(input("Введите число - "))
    n = n + 'error'
except ValueError:
    print("Некорректное значение")
except TypeError:
    print("Неверный тип")
else:
    print("Вы ввели корректное чисто ", n)