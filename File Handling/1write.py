import random 

with open('numbers.txt','w') as file :
    for i in range(10):
        file.write(str(random.randint(1,100))+"\n")