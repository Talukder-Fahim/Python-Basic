n = input("Give a number: ")
n = int(n)

for i in range(1, 11): 
    print(str(i) + ". Hello")
    if i == n:
        break
    print("Hi")
    