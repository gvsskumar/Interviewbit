# Write a context manager that opens a file and ensures it closes automatically.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")

with FileManager("test.txt", "w") as f:
    f.write("Hello World")