# Write a context manager to safely open and close multiple files.
class MultiFileManager:
    def __init__(self, *file_paths, mode='r'):
        self.file_paths = file_paths
        self.mode = mode
        self.files = []

    def __enter__(self):
        for path in self.file_paths:
            f = open(path, self.mode)
            self.files.append(f)
        return self.files  # return list of file objects

    def __exit__(self, exc_type, exc_value, traceback):
        for f in self.files:
            try:
                f.close()
            except Exception:
                pass  # ensure all files attempt to close

        if exc_type:
            print(f"Error occurred: {exc_value}")

        return False  # propagate exception
    
    