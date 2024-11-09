def calcFactorial(x):
    if x==1:
        return 1
    else:
        return calcFactorial(x-1)*x

print(calcFactorial(5))
print(calcFactorial(1000))