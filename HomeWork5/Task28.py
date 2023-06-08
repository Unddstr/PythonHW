def fu(a, b):
    if b == 0:
        return a
    return fu(a + 1, b - 1)


print(fu(3, 5))
