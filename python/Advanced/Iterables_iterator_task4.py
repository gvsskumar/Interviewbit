# Build a custom iterator for reading a file line-by-line without using built-in file iteration.
class FileLineIterator:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')  # open file manually

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()  # manually read one line

        if line == "":
            self.file.close()  # close file when done
            raise StopIteration

        return line.rstrip('\n')  # clean newline


# Usage
file_path = "sample.txt"

iterator = FileLineIterator(file_path)

for line in iterator:
    print(line)