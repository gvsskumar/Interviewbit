# Reverse a string stored in a variable.
name = str("Surya")
print(name[::-1])

# Reverse a string using a for loop.
text = "Python"
rev = ""
for ch in text:
    rev = ch + rev
    print(rev)
print(rev)