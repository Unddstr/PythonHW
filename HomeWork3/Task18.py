n = int(input("Введите количество элементов в массиве: "))
sp = []

for i in range(n):
    sp.append(int(input("Введите целое число: ")))

x = int(input("Введите число к которому мы ищем ближайшее из массива: "))

diff = abs(sp[0] - x)
result = sp[0]

for i in range(1, n):
    nextDiff = abs(sp[i] - x)
    if nextDiff < diff:
        diff = nextDiff
        result = sp[i]

print(f"Ближайшее число к {x} в массиве: {result}")
