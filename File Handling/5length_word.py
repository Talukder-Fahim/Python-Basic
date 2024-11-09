with open('zen.txt','r') as rf :
    lines = rf.readlines()
    for line in lines:
        line = line.split()
        # print(line)
        for words in line:
            if len(words) > 7 :
                print(words)

