# Write a function that prints the multiplication table of a number.
def Multiplcate(n):
    
    for i in range(1,n+1):
        result = n*i
        print(f"{n} x {i} = {result}")
Multiplcate(3)        
