number = int(input("Введите номер билета: "))
leftPart = number // 100000 + number % 100000 // 10000 + number % 10000 // 1000
rightPart = number % 1000 // 100 + number % 100 // 10 + number % 10
if leftPart == rightPart:
    print("yes")
else:
    print("no")