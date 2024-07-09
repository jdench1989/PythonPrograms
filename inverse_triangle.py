def inverse_triangle(n):
    for num in range(n, 0, -1):
        if num % 2 != 0:
            print('*' * num)


inverse_triangle(9)
