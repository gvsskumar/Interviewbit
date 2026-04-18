# Create a program that counts word frequency in a sentence.
sentence = "python is easy and python is powerful"
words = sentence.split(" ")
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] = 1

print(frequency)   
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
     
