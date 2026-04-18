# 
def check_divisible(a, b):
    # Ensure divisor is not zero
    assert b != 0, "Divisor cannot be zero."

    # Check divisibility
    assert a % b == 0, f"{a} is not divisible by {b}"

    print(f"{a} is divisible by {b}")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    check_divisible(num1, num2)

except AssertionError as e:
    print("Assertion Error:", e)

except ValueError:
    print("Invalid input! Please enter numeric values.")