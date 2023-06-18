def fu(stishok):
    count_a = list(filter(lambda x: x == 'а', stishok[0]))
    for i in stishok:
        if list(filter(lambda x: x == 'а', i)) != count_a:
            return "Пам парам"
    return "Парам пам-пам"


stishok = input("Напишите стихотворение: ").split()
print(fu(stishok))
