# Create a dictionary variable storing name, age, and city.
# Using Curly Braces {} (Most Common)
person = {"name": "Satya", "age": 28, "city": "Hyderabad"}
print(person)

# Using dict() Constructor
person = dict(name="Satya", age=28, city="Hyderabad")
print(person)

# Using dict() with List of Tuples
person = dict([("name", "Satya"), ("age", 28), ("city", "Hyderabad")])
print(person)

# Using zip() Function
keys = ["name", "age", "city"]
values = ["Satya", 28, "Hyderabad"]

person = dict(zip(keys, values))
print(person)

# Using Dictionary Comprehension
person = {x: x*x for x in range(5)}
print(person)

# Using fromkeys() Method
keys = ["name", "age", "city"]

person = dict.fromkeys(keys, "Unknown")
print(person)

# Creating Empty Dictionary and Adding Values
person = {}
person["name"] = "Satya"
person["age"] = 28
person["city"] = "Hyderabad"

print(person)
