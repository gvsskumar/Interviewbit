def char_frequency(s):
    result = {} 
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result
    
freq = char_frequency('Venkata Satya')
repeated = {}
non_repeated = {}
repeated = [ch for ch, count in freq.items() if count > 1]
# repeate_char = ' '.join(f"{ch}:{count}" for ch, count in freq.items() if count > 1)
# 
non_repeated = [ch for ch, count in freq.items() if count == 1]
print("Frequency:", freq)
print("Repeated:", repeated)
print("Non-Repeated:", non_repeated)

# {'V': 1, 'e': 1, 'n': 1, 'k': 1, 'a': 4, 't': 2, ' ': 1, 'S': 1, 'y': 1}