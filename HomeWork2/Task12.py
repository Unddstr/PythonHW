# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

flag = 1
for x in range(1, 1001):
    for y in range(1, 1001):
        if p == x * y and s == x + y:
            print(x, y)
            flag = 0
            break
    if flag == 0:
        break
