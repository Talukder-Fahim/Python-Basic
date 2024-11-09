numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')
print()
numbers = [1, 2, 3, 4, 5]
squares_generator = (x ** 2 for x in numbers)
print(squares_generator)
""" for i in squares_generator:
    print(i,end=" ") """