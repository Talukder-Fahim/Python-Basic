n = int(input())
x = 0

while(n > 0): 
    a = n % 10
    x = x * 10 + a 
    n = n // 10
print(x)