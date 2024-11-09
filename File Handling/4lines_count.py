def lines_count():
    vowels = ['A','E','I','O','U']

    with open('zen.txt','r') as rf:
        lines = rf.readlines()
        for line in lines:
            if line[0] in vowels :
                print(line)
        

lines_count()