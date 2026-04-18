# Print the following pattern using nested loops
rows = 5

for i in range(1, rows + 1):      # Outer loop for rows
    for j in range(i):            # Inner loop for stars
        print("*", end="")
    print()                       # Move to next line

#output
#*
#**
#***
#****
#*****   
# ===========rever printing * ==#

rows = 5

for i in range(rows, 0,  -1):      # Outer loop for rows
    for j in range(i):            # Inner loop for stars
        print("*", end="")
    print()