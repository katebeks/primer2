n = int(input("Введите число от 1 до 99 - "))
if n % 10 == 1:
    print("Мне " + str(n) + " год ")
elif n % 10 < 5:
    print("Мне " + str(n) + " годa ")
else:
    print("Мне " + str(n) + " лет ")