dey = 3
month = 9
year = 2023
try:
    year1 = int(input("Введите год своего рождения - "))
    month1 = int(input("Введите месяц своего рождения - "))
    dey1 = int(input("Введите день своего рождения - "))
except ValueError:
    print("Некорректное значение")
except TypeError:
    print("Неверный тип")
else:
    n = year - year1
    if month1 > month:
        n = n-1
    elif month1 == month:
        if dey < dey1:
            n = n - 1
print("Ваш возраст - ", n)