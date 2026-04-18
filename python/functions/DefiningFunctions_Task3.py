# Write a function that returns the reverse of a string.
def reverseString(name):
    if len(name)>1:
        return name[::-1]
    else: 
        return "string length is too short"
print(reverseString('Surya'))    