# Write a function that checks if a string is a palindrome.
def palindromeString(name):
    if len(name)>1:
        if name == name[::-1]:
            return f"{name} is a palindrome"
        return f"{name} is not a palindrome"
    else: 
        return "Invalid string"
print(palindromeString('Surya'))    