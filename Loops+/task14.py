lst = []
x = ""
y = False

n = int(input("Jersey numbers : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)

for i in range(0, len(lst)):    
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            x += str(lst[j]) + " "
            y = True

if y == True:           
    print("Duplicate jersey number: ", x)
    
else:
    print("No duplicates")