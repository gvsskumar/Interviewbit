# Write a generator to stream large log files and yield only lines containing "ERROR".
def stream_error_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:   # built-in lazy iteration (no full file load)
            if "ERROR" in line:
                yield line.strip()


# Usage
for log in stream_error_logs("app.log"):
    print(log)