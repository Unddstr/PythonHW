m = int(input("m: "))
n = int(input("n: "))
k = int(input("k: "))

if (k % m == 0 or k % n == 0) and m * n >= k:
    print("yes")
else:
    print("no")