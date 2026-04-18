# Write a Python function that converts a list of strings to integers and handles invalid values using try/except.
def convert_str_int(mylist):
    result = []
    for item in mylist:
       try:
           if type(int(item)) is int:
                result.append(int(item))           
       except:
           print("Invalid Value skipped")
    return result
            
print(convert_str_int([12,2.5,'65','5x','surya']))
# mylist = [5,'Surya',8.5,True]
# try:
#     for item in mylist:
#         try:
#             if type(int(item)) is int:
#                 print(int(item))
#         except ValueError:
#          print(f"{item} is not integer")
# except:
#     print("Value is not integer")
# finally:
#     print("Done")    


