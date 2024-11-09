string = input().lower()
dictionary = {}

words_list = string.split()

for words in words_list:
    if not words in dictionary:
        dictionary[words] = 0
        print(words,end=" ")

