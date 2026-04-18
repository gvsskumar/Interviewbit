# Write a program that defines a custom exception for invalid email format.
# Custom Exception
class InvalidEmailError(Exception):
    pass


def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format.")
    else:
        print("Valid Email:", email)


try:
    user_email = input("Enter your email: ")
    validate_email(user_email)

except InvalidEmailError as e:
    print("Custom Exception:", e)

finally:
    print("Program execution completed.")