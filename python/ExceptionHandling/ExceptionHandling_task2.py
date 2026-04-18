# Write a program that asks the user to enter two numbers and safely performs division using try and except.
data = [1,5]
try:
    result = int(data[0])+int(data[1])
except ZeroDivisionError:
    print("Zero Devision Error")
else:
    print("result",result)
finally:
    print("Program Execuation completed")        