# Convert a float variable to an integer.
floatValue = float(56)
print(floatValue) # 56.0

floatValue1 = float(True)
print(floatValue1) # 1.0

floatValue2 = float(False)
print(floatValue2) # 0.0

floatValue3 = float()
print(floatValue3) # 0.0

floatValue4 = float("") # ERROR : ValueError: could not convert string to float: ''
print(floatValue4)

# Convert a float variable to an integer
floatValue5 = float(5.6)
print(int(floatValue5)) # 5


