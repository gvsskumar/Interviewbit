data = [10,0]
try:
    num1 = data[0]
    num2 = data[1]
    result = num1/num2
    
except ZeroDivisionError:
    print("Zero devision by Value Error")
else:
    print("Result:",result)
finally:
    print("program execution completed")
    