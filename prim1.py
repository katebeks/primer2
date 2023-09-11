x = int(input("Введите число - "))
def sumcifr(x):
    if x // 10 == 0:
        return x
    else:
        return x%10+sumcifr(x//10)

print(sumcifr(x))
