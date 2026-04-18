#
def process_api_response(response):
    # Assert that status code is 200
    assert response["status_code"] == 200, "API request failed. Status code is not 200."

    # Process response data
    data = response["data"]
    print("Processing Data:", data)


# Example API response
api_response = {
    "status_code": 200,
    "data": {"name": "Satya", "age": 25}
}

try:
    process_api_response(api_response)

except AssertionError as e:
    print("Assertion Error:", e)