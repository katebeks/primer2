x = input("Введите число ")
k = len(x)
y = ""
while k > 0:
    y = y + x[k-1]
    k -= 1
print("Результат - ", y)
