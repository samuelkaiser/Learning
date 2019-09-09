def is_pangram(sentence):
    # a-z string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # check if a-z is in sentence
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True

knownPangram = "The quick brown fox jumps over the lazy dog."
knownNotToBePangram = "I live off espresso"

print(is_pangram(knownPangram))
print(is_pangram(knownNotToBePangram))
