x = input()

keys = []
value = []

dict = {}

for i in x:
    if i not in keys :
        keys.append(i)
        value.append(x.count(i))

# print("Keys:",keys)
# print("value:",value)

for k,v in zip(keys,value):
    dict[k]=v
print(dict)