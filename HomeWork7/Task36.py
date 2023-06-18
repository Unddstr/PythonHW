def print_operation_tabel(operation, num_row=6, num_colum=6):
    for i in range(num_row):
        for j in range(num_colum):
            print(operation(i + 1, j + 1), end="\t")
        print(" ")
    return 0


print_operation_tabel(lambda x, y: x * y)
