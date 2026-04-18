# Write a Python API validation function that raises InvalidRequestException when required fields are missing.
# Custom Exception
class InvalidRequestException(Exception):
    pass


def validate_request(data):
    required_fields = ["name", "email", "age"]

    for field in required_fields:
        if field not in data:
            raise InvalidRequestException(f"Missing required field: {field}")

    print("API request is valid.")


# Example API request data
request_data = {
    "name": "Satya",
    "email": "satya@example.com"
}

try:
    validate_request(request_data)

except InvalidRequestException as e:
    print("Custom Exception:", e)

finally:
    print("Request validation completed.")