# Swap the values of two variables without using a third variable.
# Method -1
a = int(10)
b = int(20)
a,b = b,a
print(a,b) # a=20,b=10

# Method-2
x = int(5)
y = int(10)
x = x+y
y = x-y
x = x-y
print(x,y) # x=10,y=5