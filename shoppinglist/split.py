# 1. Need to split a string - Done
# 2. Need to move words into dictionary - Done
# 3. Need to count words in string, so the key is word and value is amount of it in stringself.

# 1. Done

def word_count(string):
    dict_1 = {}
    string = string.lower()
    words = string.split()
    for word in words:
        try:
            dict_1[word] = dict_1[word] + 1
        except KeyError:
            dict_1[word] = 1
    return dict_1

print(word_count("I do not like it Sam I Am"))
