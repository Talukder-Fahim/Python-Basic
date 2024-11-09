string = input()

list_of_string =(string.split())
new_dict = {}
# print(list_of_string)

for words in list_of_string:
    new_dict[words] = list_of_string.count(words)

print(new_dict)