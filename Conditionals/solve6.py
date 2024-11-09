a = int(input())

if  a>0 :
    if 2 ** a :
        print("Yes")
    else:
        print("No")
elif a<0 :
    print("Negative input is not valid")
else:
    print("Zero is not a valid input")