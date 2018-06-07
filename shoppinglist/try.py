vowels = ["a", "e", "i", "o", "u"]
my_word = "eAjooDnw"

def disemvowel(word):
    new_word = ''
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    return new_word

print("The word is: ",my_word)
print("Disemvoweled word is: ", disemvowel(my_word))
