n = input("Give a number: ")
n = int(n)

for i in range(1, 11): 
    if i == n:
        continue
    print(i)