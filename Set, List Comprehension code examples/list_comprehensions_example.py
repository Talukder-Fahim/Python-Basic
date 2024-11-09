list1 = []
for item in range(1, 6):
    list1.append(item)
print(list1)   
list2 = [i for i in range(1,6)]
print(list2)







#filtering and mapping
list3 = [item ** 3 for item in range(1, 6)]
print(list3)

list4 = [item for item in range(1, 11) if item % 2 == 0]
print(list4)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print(colors2)

#value assignment
numbers = [1, 2, 3, 4, 5]
new_numbers = []
for x in numbers:
    if x % 2 == 0:
        new_numbers.append(x)
    else:
        new_numbers.append(x * 2)
print(new_numbers)
new_numbers2 = [x if x % 2 == 0 else x * 2 for x in numbers]
print(new_numbers2)

#set comprehension
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
evens = {item for item in numbers if item % 2 == 0}
print(evens)

