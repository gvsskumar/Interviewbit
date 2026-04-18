# Custom Iterator Using Built-in File Iteration
class FileLineIterator:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')
        self.iterator = iter(self.file)  # use built-in iterator

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator).rstrip('\n')
        except StopIteration:
            self.file.close()
            raise


# Usage
reader = FileLineIterator("sample.txt")

for line in reader:
    print(line)