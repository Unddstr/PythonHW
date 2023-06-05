n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

first = [int(input("Введите число для первого списка: ")) for _ in range(n)]
second = [int(input("Введите число для второго списка: ")) for _ in range(m)]

first = set(first)
second = set(second)
result = first.intersection(second)
print(result)
