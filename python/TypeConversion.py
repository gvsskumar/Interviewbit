#Type Conversion Automatic
x = 10;
y = 2.5;

print(type(x)); # <class 'int'>
print(type(y)); # <class 'float'>

#Type Conversion Explicit int to float
x = int(10);
y = float(2.5);
z = x+y;
print(type(x)); # <class 'int'>
print(type(y)); # <class 'float'>
print(type(z)); # <class 'float'>