def is_prime(n):
    for i in range(2, n+1):
        if n % i == 0:
            return False
        if i * i > n:
            return True

print(is_prime(7))
print(is_prime(15))
print(is_prime(11))

