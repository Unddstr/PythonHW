number = abs(int(input("Введите трехзначное число: ")))
print(number % 10 + number % 100 // 10 + number // 100)