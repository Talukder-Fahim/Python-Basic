def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
            print(True)
    else:
        print(False)

is_perfect(28)