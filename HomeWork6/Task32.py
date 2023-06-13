from random import randint
from typing import List


def get_list(number: int) -> List[int]:
    return [randint(-10, 10) for _ in range(number)]


num = int(input("введите число элементов массива: "))
numbers = get_list(num)
mn = int(input("введите минимум: "))
mx = int(input("введите максимум: "))

for i in range(len(numbers)):
    if mn <= numbers[i] <= mx:
        print(i, end=" ")
