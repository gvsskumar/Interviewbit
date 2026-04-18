# Example: Worker Pool for Parallel File Processing
import multiprocessing
import os
import time

# Simulated file processing function
def process_file(file_path):
    """
    Pretend this function parses a file (CPU-heavy or I/O-heavy)
    """
    print(f"[PID {os.getpid()}] Processing {file_path}")
    word_count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word_count += len(line.split())
    except FileNotFoundError:
        word_count = 0
    return (file_path, word_count)

def main():
    # List of files to process
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

    start_time = time.time()
    
    # Create a pool of workers equal to number of CPU cores
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map files to the pool (distributes tasks to workers)
        results = pool.map(process_file, files)

    # Results contain (file_path, word_count)
    for file_path, count in results:
        print(f"{file_path}: {count} words")
    
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()