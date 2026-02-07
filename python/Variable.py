x = 10;
y = x;
x = 20;
print(x); # 20
print(y); # 10
# Y gets the value of x at assignment time, Integers are immutable.

# Example 2
a = 25;
a = "Hello";
print(a); # Hello

# Example 3
a = 25;
print(type(a)); # <class 'int'>
a = "Hello";
print(type(a)); # <class 'str'>

# Strings are immutable
str1 = "Hello";
str2 = str1;
str1 = "Bye";
print(str1); # Bye
print(str2); # Hello

# Boolean are immutable
bool1 = True;
bool2 = bool1;
bool1 = False;
print(bool1); # False
print(bool2); # True

# Float are immutable
float1 = 1.0;
float2 = float1;
float1 = 2.0;
print(float1); # 2.0
print(float2); # 1.0

# None are immutable
none1 = None;
none2 = none1;
none1 = "Hello";
print(none1); # Hello
print(none2); # None

