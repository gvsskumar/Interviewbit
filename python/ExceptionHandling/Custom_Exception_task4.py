# Create a custom exception called NegativeNumberError and raise it when a negative number is passed to a square root function.
import math

# Custom Exception
class NegativeNumberError(Exception):
    pass


def calculate_square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    
    return math.sqrt(num)


try:
    number = float(input("Enter a number: "))
    result = calculate_square_root(number)
    print("Square Root:", result)

except NegativeNumberError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

finally:
    print("Program execution completed.")