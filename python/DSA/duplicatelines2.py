import os
import heapq
import tempfile

CHUNK_SIZE = 100 * 1024 * 1024  # 100MB per chunk


def split_and_sort(file_path):
    temp_files = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        chunk = []
        current_size = 0

        for line in f:
            chunk.append(line)
            current_size += len(line.encode('utf-8'))

            if current_size >= CHUNK_SIZE:
                chunk.sort()
                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
                temp_file.writelines(chunk)
                temp_file.close()

                temp_files.append(temp_file.name)
                chunk = []
                current_size = 0

        # Last chunk
        if chunk:
            chunk.sort()
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
            temp_file.writelines(chunk)
            temp_file.close()
            temp_files.append(temp_file.name)

    return temp_files

def merge_files(sorted_files, output_file):
    files = [open(f, 'r', encoding='utf-8') for f in sorted_files]

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in heapq.merge(*files):
            out.write(line)

    for f in files:
        f.close()

def find_duplicates(sorted_file):
    prev_line = None
    count = 0

    with open(sorted_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line == prev_line:
                count += 1
            else:
                if count > 1:
                    print(f"{prev_line} -> {count} times")
                count = 1

            prev_line = line

        # Last line check
        if count > 1:
            print(f"{prev_line} -> {count} times")

def process_large_file(file_path):
    print("Step 1: Splitting and sorting chunks...")
    temp_files = split_and_sort(file_path)

    print("Step 2: Merging sorted chunks...")
    sorted_output = "sorted_output.txt"
    merge_files(temp_files, sorted_output)

    print("Step 3: Finding duplicates...")
    find_duplicates(sorted_output)

    # Cleanup temp files
    for f in temp_files:
        os.remove(f)


if __name__ == "__main__":
    process_large_file("mytext.txt")                    