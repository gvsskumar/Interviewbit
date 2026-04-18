# Write two functions:
#   One prints the result
#   One returns the result
#   Then use the returned value in another calculation.
# Function that prints the result
def print_sum(a, b):
    result = a + b
    print("Sum is:", result)


def return_sum(a, b):
    result = a + b
    return result


print_sum(5, 3)


value = return_sum(5, 3)


final_result = value * 2
print("Final Result:", final_result)