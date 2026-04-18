# Implement tail -f functionality using generators (real-time file reading).
import time

def tail_f(file_path, sleep_interval=0.5):
    with open(file_path, 'r') as f:
        f.seek(0, 2)  # move to end of file

        while True:
            line = f.readline()

            if not line:
                time.sleep(sleep_interval)  # wait for new data
                continue

            yield line.rstrip('\n')


# Usage
for line in tail_f("app.log"):
    print(line)