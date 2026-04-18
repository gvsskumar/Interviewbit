# Write a Python script that calculates factorial and use pdb breakpoints to debug incorrect results.
import pdb

def factorial(n):
    pdb.set_trace()   # Debugging breakpoint
    
    result = 1
    for i in range(1, n + 1):
        result = result * i
    
    return result


num = int(input("Enter a number: "))
output = factorial(num)
print("Factorial:", output)

# Useful pdb Commands
| Command      | Description          |
| ------------ | -------------------- |
| `n`          | Execute next line    |
| `s`          | Step into function   |
| `p variable` | Print variable value |
| `c`          | Continue execution   |
| `q`          | Quit debugger        |
