x = [int(i) for i in input("").split()]
list_x= list(set(x))

y = []

for i in sorted(list_x):
    y.append(x.index(i))

print(f"first: {y[0]}\nsecond: {y[1]}\nthird: {y[2]}")