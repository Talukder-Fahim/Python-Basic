def digit_count():
    count = 0
    with open('sample.txt','r') as rf :
        for i in rf.read() :
            if i.isdigit() :
                count += 1
        print("Count:", count)

digit_count()
