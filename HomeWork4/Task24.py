n = int(input("Введите кол-во кустов на грядке: "))
gryadka = [int(input("Введите кол-во ягод на кусте: ")) for _ in range(n)]
maximum = max(gryadka[-1] + gryadka[0] + gryadka[1], gryadka[-2] + gryadka[-1] + gryadka[0])
for i in range(0, len(gryadka)-2):
    maximum = max(gryadka[i] + gryadka[i + 1] + gryadka[i + 2], maximum)

print(f"Максимальное кол-во собранных ягод: {maximum}")
