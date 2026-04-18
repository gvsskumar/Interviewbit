# Create a function that asserts a matrix is not empty before performing operations.
def process_matrix(matrix):
    # Assert that matrix is not empty
    assert matrix and len(matrix) > 0, "Matrix cannot be empty."

    print("Matrix is valid.")
    
    # Example operation: print matrix elements
    for row in matrix:
        print(row)


try:
    matrix_data = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    process_matrix(matrix_data)

except AssertionError as e:
    print("Assertion Error:", e)
