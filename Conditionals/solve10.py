num1 = float(input("Enter a number :"))
num2 = float(input("Enter another number :"))
operator = input("+,-,*,/ :")

if operator == "+" :
    a = num1 + num2 
    print(f"Addition: {a}")
elif operator == "-" :
    b = num1 - num2
    print(f"Substraction: {b}")
elif operator == "*" :
    c = num1 * num2
    print(f"Multipication: {c}")
elif operator == "/" :
    if  num2 == 0: 
        print("Division: Zero as divisor is not valid!")
    else :
        d = num1 / num2
        print(f"Division: {d}")
else:
    print("Invalid operator input")
    
