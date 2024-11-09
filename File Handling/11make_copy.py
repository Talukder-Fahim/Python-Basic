def make_copy():
    with open('input.txt','r') as rf:
        lines = rf.readlines()
        for line in lines:
            words = line.split()
        
        with open('output.txt','w') as wf:
            for word in words:
                output = word.capitalize() + ' '
                wf.write(output)





make_copy()