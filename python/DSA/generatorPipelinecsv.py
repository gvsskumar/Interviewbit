import csv

# 1️⃣ Read CSV lazily
def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


# 2️⃣ Filter rows
def filter_rows(rows, condition):
    for row in rows:
        if condition(row):
            yield row


# 3️⃣ Transform rows
def transform_rows(rows):
    for row in rows:
        # Example transformation
        row['salary'] = float(row.get('salary', 0))
        row['age'] = int(row.get('age', 0))
        yield row


# 4️⃣ Aggregate (example: average salary)
def aggregate(rows):
    total = 0
    count = 0

    for row in rows:
        total += row['salary']
        count += 1

    return total / count if count else 0


# 5️⃣ Save output (optional stage)
def write_csv(rows, output_file):
    rows = iter(rows)
    first = next(rows, None)
    if not first:
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=first.keys())
        writer.writeheader()
        writer.writerow(first)

        for row in rows:
            writer.writerow(row)

pipeline = read_csv("large_file.csv")

pipeline = filter_rows(pipeline, lambda r: int(r['age']) > 30)

pipeline = transform_rows(pipeline)

avg_salary = aggregate(pipeline)

print("Average Salary:", avg_salary)

# 💡 Alternative: Save Filtered Data
# pipeline = read_csv("large_file.csv")
# pipeline = filter_rows(pipeline, lambda r: int(r['age']) > 30)
# pipeline = transform_rows(pipeline)

# write_csv(pipeline, "output.csv")