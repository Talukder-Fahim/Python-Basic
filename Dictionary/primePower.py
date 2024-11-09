# limit = int(input("Enter the limit: "))
limit = 10
numbers = list(range(2, limit + 1))

prime_numbers = []

for num in numbers:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

#prime_numbers = [2,3,5,7]

primeDict = {}

pow_list = []

for i in prime_numbers:
    # print(i)
    for j in prime_numbers:
        # if i ** (prime_numbers.index((prime_numbers.index(i)))+1) < 100 :
            # pow_list.append()
        # print(str(j)+"j")
        if i != j and i < j:
            if i ** j < 100 :
                pow_list.append(j)
print(pow_list)