list_int = [1,2,3,4,5,6,7,8,9]
new_list = []

for i in list_int:
    if i % 2 != 0:
        new_list.append(i)
# print(new_list)
new_dict = {}

for j in new_list:
    new_dict[j] = j**2

print(new_dict)


