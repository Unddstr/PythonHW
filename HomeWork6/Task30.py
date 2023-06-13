first_element = int(input("Введите первый элемент массива: "))
d = int(input("Введите шаг прогрессии: "))
n = int(input("Введите колличество элемментов в массиве: "))
mass = []

for i in range(n):
    mass.append(first_element + i * d)

print(*mass)
