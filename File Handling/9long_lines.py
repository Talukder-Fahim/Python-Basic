def long_lines():
    with open('lines.txt','r') as rf :
        lines = rf.readlines()
        # print(lines)
        for line in lines :
            words = line.split()
            if len(words) >= 8 :
                print(line,end='')

            # print(line,end='')            
            # print(words)


long_lines()