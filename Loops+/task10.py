n = int(input("Enter number: "))
list_n = []

for i in range(0, n+1):
    list_n.append(i+1)

for j in range(1, n+1, 2):
    list_n[j] = list_n[j] * (-1)

print(sum(list_n))