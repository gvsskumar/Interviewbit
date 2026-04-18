# Example: Parsing multiple large text files in parallel
import multiprocessing
import os
import time

# Simulated file parsing function
def parse_file(file_path):
    print(f"Processing {file_path} in PID: {os.getpid()}")
    word_count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word_count += len(line.split())
    return (file_path, word_count)

def main():
    # Suppose we have multiple files
    files = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file4.txt"
    ]
    
    start_time = time.time()
    
    # Using multiprocessing Pool for simplicity
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(parse_file, files)
    
    end_time = time.time()
    
    # Display results
    for file_path, count in results:
        print(f"{file_path}: {count} words")
    
    print(f"Parallel processing took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
