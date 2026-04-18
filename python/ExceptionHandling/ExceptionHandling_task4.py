# Write a program that reads numbers from a list and catches errors if a non-numeric value appears.
numbers = [10, "20", 30, "abc", 40, "50x", 60]

valid_numbers = []
errors = []

for value in numbers:
    try:
        valid_numbers.append(float(value))
    except ValueError:
        errors.append(value)

print("Valid Numbers:", valid_numbers)
print("Invalid Values:", errors)
