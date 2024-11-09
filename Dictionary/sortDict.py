dict = {"Math":81,"Physics":83,"Chemistry":87}

dict = sorted(dict.items(), key= lambda x: x[1], reverse= True)

print(dict)