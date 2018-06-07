def sillycase(word):
    return word[:len(word)//2].lower() + word[len(word)//2:].upper()

print(sillycase("ApPlEjUiCe"))
