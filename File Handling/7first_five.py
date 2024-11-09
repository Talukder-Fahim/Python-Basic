def first_five():
    # with open('names2.txt','r') as rf:
    with open('names.txt','r') as rf:    
        lines = rf.readlines()
        
        if len(lines) > 5 :
            plain_lines = lines[:5]
            for line in plain_lines:
                print(line.removesuffix('\n'))
                

        elif len(lines) < 5 :
            for line in lines:
                print(line.removesuffix('\n'))
    
first_five()