# Write a function that calculates the average of a list but uses assert to ensure the list is not empty. 
def calculate_average(numbers):
    # Assert to ensure list is not empty
    assert len(numbers) > 0, "The list cannot be empty."

    avg = sum(numbers) / len(numbers)
    return avg


# Example list
num_list = [10, 20, 30, 40]

try:
    result = calculate_average(num_list)
    print("Average:", result)

except AssertionError as e:
    print("Assertion Error:", e)