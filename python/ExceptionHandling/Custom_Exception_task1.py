#Write a Python program that raises a custom exception if a user enters an age less than 18, Need for answers
# Define custom exception
class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeTooSmallError("Age must be 18 or above.")

    print("Access granted. You are eligible.")

except AgeTooSmallError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a valid number.")

finally:
    print("Program execution completed.")