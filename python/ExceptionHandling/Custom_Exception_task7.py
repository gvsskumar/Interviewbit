# Create a custom exception that triggers when password length is less than 8 characters.
# Custom Exception
class WeakPasswordError(Exception):
    pass


def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    else:
        print("Password is valid.")


try:
    user_password = input("Enter your password: ")
    check_password(user_password)

except WeakPasswordError as e:
    print("Custom Exception:", e)

finally:
    print("Program execution completed.")