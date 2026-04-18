# String convert to Uper case
str1 = 'surya'
print(str1.upper()) # SURYA

str2 = 'VENKATA'
print(str2.lower()) # venkata

str3 = ' python is easy and python is powerful '
print(str3.capitalize()) # Python is easy and python is powerful
print(str3.title()) # Python Is Easy And Python Is Powerful
print(str3.strip()) # python is easy and python is powerful
print(str3.lstrip()) # python is easy and python is powerful   
print(str3.rstrip()) #     python is easy and python is powerful
print(str3.replace('python','java')) # java is easy and java is powerful
print(str3.split(' ')) # ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']
print(str3.endswith('powerful')) #True
print(str3.startswith('python')) #True

text = "PyThOn"
print(text.swapcase()) #pYtHoN 

str4 = ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']
print(' '.join(str4)) # python is easy and python is powerful

