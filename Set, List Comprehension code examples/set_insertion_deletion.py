# Create a set
my_set = {1, 2, 3, 4, 5,8}

my_set.add(6)  
print("After adding 6:", my_set)

my_set.add(4)
print("After adding 4 again:", my_set)

my_set.remove(2)  
print("After removing 2:", my_set)

""" my_set.remove(7)  
print("After removing 7:", my_set)
 """
my_set.discard(3) 
print("After discarding 3:", my_set)

my_set.discard(8) 
print("After discarding 8:", my_set)
