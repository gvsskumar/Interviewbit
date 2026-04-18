# Write a function that accepts any number of keyword arguments and prints them.
def show_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,"-->",value)
show_kwargs(name="Surya",age=35,flag=True,height=5.2) 