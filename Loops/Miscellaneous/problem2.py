n = int(input())
r = int(input())

nfactorial = 1
for i in range(1 , n+1):
    nfactorial *= i

factorial = 1
for j in range(1 , (n-r)+1):
    factorial *= j

nPr = (nfactorial)/factorial
print(nPr)