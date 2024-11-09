def even_number(l):
    list = []
    for i in l:
        if i % 2 == 0:
            list.append(i)
    print(list)

even_number([1,2,3,4,5,6,7,8,9])