# Write a function that accepts any number of integers and returns their sum.
def show_integers(*args):
    total = 0
    for num in args:
        if type(num) is int:
            total +=num
    return total;        
print(show_integers(1,2,3,4)) # 10
print(show_integers(1,2.4,3,4)) # 8   