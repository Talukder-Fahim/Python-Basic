sample_dict = {
                "name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"
                }


keys = ["name","salary"]


dict = {}
for k,v in sample_dict.items():
    if k in keys:
        dict[k] = v

print(dict)
