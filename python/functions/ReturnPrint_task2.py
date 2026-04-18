# Write a function that prints the number of words in a sentence.
def wordsentence(sentence):
    wordlist = sentence.split(" ")
    return len(wordlist)
print(wordsentence("python is easyy and powerfull"))
