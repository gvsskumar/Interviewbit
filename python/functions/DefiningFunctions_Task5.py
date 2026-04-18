# Write a function that counts the number of vowels in a string.
def Vowels(mystr):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in mystr:
        if ch in vowels:
            count +=1
    return count
print(Vowels("Welcome a python"))        