#METHOD:1 

x = int(input("Enter the first angle :"))
y = int(input("Enter the second angle :"))
z = int(input("Enter the third angle :"))

sum = x+y+z

if 0<x and x<180 and sum == 180 :
    print("Yes")
elif 0<y and y<180 and sum == 180 :
    print("Yes")
elif 0<z and z<180 and sum == 180 :
    print("Yes")
else :
    print("No")

#METHOD:2

# x = int(input("Enter the first angle :"))
# y = int(input("Enter the second angle :"))
# z = int(input("Enter the third angle :"))

# sum = x+y+z

# if (0<x<180) and (0<y<180) and (0<z<180) :
#     if sum == 180:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("No")