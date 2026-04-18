# Write a function that prints student details with a default course "Python".
def studentInfo(name,email,phone,course="python"):
    print(f"Name :{name}")
    print(f"Email :{email}")
    print(f"Phone :{phone}")
    print(f"Course :{course}")
studentInfo("Surya","surya@gmail.com","9346814210")
print("--------------------------------")
studentInfo("Satya","satya@gmail.com","7013675726",'React')    