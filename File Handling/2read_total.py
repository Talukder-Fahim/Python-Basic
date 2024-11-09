with open('numbers.txt','r') as rf:
    sum = 0
    for i in rf:
        print(i.strip())
        sum += int(i)
    print('Total:',sum)