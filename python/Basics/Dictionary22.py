# Retrieve all keys and values from a dictionary variable.
# Using keys() and values()
person = {"name": "Satya", "age": 28, "city": "Hyderabad"}

print("Keys:", person.keys())
print("Values:", person.values())

# Using items() (Keys and Values Together)
person = {"name": "Satya", "age": 28, "city": "Hyderabad"}

for key, value in person.items():
    print(key, ":", value)

    