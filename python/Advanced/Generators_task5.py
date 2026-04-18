# 1. READ
def read_data(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()


# 2. FILTER
def filter_data(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line


# 3. TRANSFORM
def transform_data(lines):
    for line in lines:
        # Example: split log into structured data
        parts = line.split(" - ")
        yield {
            "timestamp": parts[0],
            "level": parts[1],
            "message": parts[2] if len(parts) > 2 else ""
        }


# 4. AGGREGATE
def aggregate_data(records):
    count = 0
    for _ in records:
        count += 1
    return count


# PIPELINE EXECUTION
pipeline = read_data("app.log")
pipeline = filter_data(pipeline, "ERROR")
pipeline = transform_data(pipeline)

result = aggregate_data(pipeline)

print("Total ERROR logs:", result)