n = int(input("Введите количество монеток: "))
orel = 0
reshka = 0
for i in range(n):
    coin = input("Введите 1 если орел, 0 если решка: ")
    if coin == "0":
        reshka += 1
    if coin == "1":
        orel += 1
print("Нужно перевернуть монет: ", min(reshka, orel))
