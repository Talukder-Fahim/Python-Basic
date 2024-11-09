x = float(input("1st number :"))
y = float(input("2nd number :"))

operation = int(input("Choice (1/2/3/4)? (1.Addition)(2.Subtraction)(3.Multipication)(4.Division) :"))

if operation == 1 :
    print(f"Addition:{x+y}")
elif operation == 2 :
    print(f"Substraction:{x-y}")
elif operation == 3 :
    print(f"Multipicaton:{x*y}")
elif operation == 4 :
    z = int(input("Choice (1/2)? (1.Quotient)(2.Remainder) :"))
    if z == 1 :
        print(f"Quotient:{x/y}")
    elif z == 2 :
        print(f"Remainder:{x%y}")
    else :
        print("Invalid input")
else :
    print("Invalid input")
