# Write a function that calculates the factorial of a number.
def Factorial(n):
    if n==0 or n==1:
        return 1
    result = 1
    for num in range(2,n+1):
        result *= num
    return result   
    
print(Factorial(5))        