# Check if a variable is mutable objects
# Using id()
a = [1,2,3]
print ("before ",id(a))
a.append(4)
print ("after ",id(a))
print(a)

print(isinstance(a, type(a)))

b = "Surya"
print ("before ",id(b))
a.append(4)
print ("after ",id(b))
print(b)

print(isinstance(b, type(b)))


