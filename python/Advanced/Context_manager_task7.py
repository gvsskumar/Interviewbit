# Implement @contextmanager version of a file handler.
from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode='r'):
    f = open(file_path, mode)
    try:
        yield f   # provide file object to with-block
    finally:
        f.close()  # always executed (cleanup)
with open_file("sample.txt") as f:
    content = f.read()
    print(content)        