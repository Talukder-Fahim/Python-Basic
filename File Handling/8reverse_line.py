with open('zen.txt','r') as rf:
    lines = rf.readlines()
    lines = lines[::-1]

    for line in lines:
        print(line.removesuffix('\n'))