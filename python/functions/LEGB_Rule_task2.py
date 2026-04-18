x = 10   # Global variable

def show_value():
    x = 5   # Local variable (conflicts with global x)
    print("Inside function:", x)

show_value()

print("Outside function:", x)