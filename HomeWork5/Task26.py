def fu(a, b):
    if b == 0:
        return 1
    return a * fu(a, b - 1)


print(fu(3, 5))
