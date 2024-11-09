with open('notes.txt','r') as rf:
    lines = rf.readlines()
    # print(lines) 

    for line in lines:
        count = 0
        for words in line:
            if words[-1].isdigit():
                count += 1
        print(f"Number of words ending with a digit are {count}")
