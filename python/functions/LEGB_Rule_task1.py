# Create a global variable and modify it inside a function using the global keyword.

count = 10   # Global variable

def update_count():
    global count
    count = count + 5
update_count()
print(count)

