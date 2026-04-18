# What is *args in Python?

# *args allows a function to accept a variable number of positional arguments.
# It collects multiple arguments into a tuple.

def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3, 4)

# **kwargs allows a function to accept a variable number of keyword arguments.
# All keyword arguments are collected into a dictionary.

def show_details(**kwargs):
    print(kwargs)

show_details(name="Satya", age=25, dept="IT")