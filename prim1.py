try:
    year1 = int(input("Введите год рождения  1-го человека- "))
    month1 = int(input("Введите месяц рождения 1-го человека- "))
    dey1 = int(input("Введите день рождения 1-го человека- "))
    year2 = int(input("Введите год рождения 2-го человека- "))
    month2 = int(input("Введите месяц рождения 2-го человека- "))
    dey2 = int(input("Введите день рождения 2-го человека- "))
    if year1 < year2:
        print("старше 1-ый человек")
    elif year1 == year2:
        if month1 < month2:
            print("старше 1-ый человек")
        elif month1 == month2:
            if dey1 < dey2:
                print("старше 1-ый человек")
            elif dey1 == dey2:
                print("Они ровестники")
            else:
                print("старше 2-oй человек")
        else:
            print("старше 2-oй человек")
    else:
        print("старше 2-oй человек")
except ValueError:
    print("Некорректное значение")

