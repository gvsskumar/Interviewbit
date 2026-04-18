# Create a program that asserts a number must be positive before calculating its square root.
import math

def calculate_square_root(num):
    # Assert to ensure the number is positive
    assert num > 0, "Number must be positive."

    result = math.sqrt(num)
    return result


try:
    number = float(input("Enter a number: "))
    sqrt_value = calculate_square_root(number)
    print("Square Root:", sqrt_value)

except AssertionError as e:
    print("Assertion Error:", e)

except ValueError:
    print("Invalid input! Please enter a numeric value.")