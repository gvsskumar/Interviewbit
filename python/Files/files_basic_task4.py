# Example: Read log file and count errors
with open('app.log','r') as file:
    count = 0
    for line in file:
        if "Error" in line:
            count += 1
    print(count)        
