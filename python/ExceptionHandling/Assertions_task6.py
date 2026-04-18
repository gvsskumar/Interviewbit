# Write a program that asserts a file path exists before reading it.
import os

def read_file(file_path):
    # Assert that the file exists
    assert os.path.exists(file_path), "File path does not exist."

    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:\n", content)


try:
    path = input("Enter file path: ")
    read_file(path)

except AssertionError as e:
    print("Assertion Error:", e)