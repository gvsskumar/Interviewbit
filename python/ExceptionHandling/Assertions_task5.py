def process_array(arr):
    # Assert that all elements are integers
    for value in arr:
        assert isinstance(value, int), f"Invalid value {value}. All elements must be integers."

    print("All values are integers.")
    print("Array:", arr)


try:
    numbers = [10, 20, 30, 40]   # Example array
    process_array(numbers)

except AssertionError as e:
    print("Assertion Error:", e)