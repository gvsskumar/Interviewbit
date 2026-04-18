# Create a dictionary where values contain lists of numbers and calculate their sum.
my_dict = {"amount1":100,"amount2":200,"amount3":300}
sum = 0
for amt in my_dict:
    sum += int(amt)
print(sum)    