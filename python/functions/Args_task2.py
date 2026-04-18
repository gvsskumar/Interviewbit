# Write a function that multiplies all numbers passed using *args.
def multiply_integers(*args):
    total = 1
    for num in args:
        if type(num) is int:
            total *=num
    return total;        
print(multiply_integers(1,2,3,4)) # 24
print(multiply_integers(1,2.4,3,4)) # 12  