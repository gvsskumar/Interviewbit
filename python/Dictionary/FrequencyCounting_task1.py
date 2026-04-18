# Count the frequency of each character in a string.
text = "VenkataSatyaSuryaKumar"
frequency = {}
for ch in text:
    if ch.lower() in frequency:
        frequency[ch.lower()] += 1
    else:
        frequency[ch.lower()] = 1
print(frequency)             
# {'v': 1, 'e': 1, 'n': 1, 'k': 2, 'a': 6, 't': 2, 's': 2, 'y': 2, 'u': 2, 'r': 2, 'm': 1}

