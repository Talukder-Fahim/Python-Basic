keys = ["Black", "Red", "Maroon", "Yellow"]
values = ["#000000", "#FF0000", "#800000","#FFFF00"]

new = dict(zip(keys,values))
list = []

for k,v in new.items():
    dic = {"color_name" : k , "color_code" : v}
    list.append(dic)
   


print(list)