#Docstrings
def add(a, b):
    """
    Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of `a` and `b`.
    """
    return a + b

print(add.__doc__)    

#Types of Docstrings
#1. Module Docstring :  : Where it goes: First line of the file
"""
This module handles user authentication.
"""

#2. Class Docstring: Where it goes: Just inside the class definition
class User:
    """Represents a system user."""

#3. Method Docstring:Where it goes: Inside the method
class User:
    def login(self):
        """Logs the user into the system."""
#4. Function Docstring: Where it goes: Inside the function
def add(a, b):
    """Returns the sum of two numbers."""
#5. Variable Docstring:Where it goes: Immediately after the variable
count = 10
"""Stores the maximum retry count."""
#6. Argument Docstring:Where it goes: Inside function docstring
def add(a, b):
    """
    Args:
        a (int): First number
        b (int): Second number
    """
#7. Exception Docstring:Where it goes: Inside function docstring
def divide(a, b):
    """
    Raises:
        ZeroDivisionError: If b is zero
    """
#8. Attribute Docstring:Where it goes: Inside class docstring
class User:
    """
    Attributes:
        name (str): User name
    """
#9. Docstring Template:What it is: A structure/format used to write docstrings
# Examples: Google, NumPy, Sphinx

#10. Inline Docstring: Where it goes: Inside code block
x += 1
"""Increment counter"""

#11. Nested Docstring: Where it goes: Inside nested function
def outer():
    """Outer function"""

    def inner():
        """Inner function"""
#13. Google Docstring :
# Style: Human-readable, clean
# Used by: Google, many startups
def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of numbers
    """
#14. Numpy Docstring
#Style: Scientific & data-oriented
#Used by: NumPy, Pandas, ML libraries
def add(a, b):
    """
    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        Sum of numbers
    """
#15. Sphinx Docstring
# Style: Machine-readable
# Used by: Large documentation systems
def add(a, b):
    """
    :param a: First number
    :param b: Second number
    :return: Sum of numbers
    """
#16. Pydoc Docstring
# What it is: Python’s built-in documentation generator
# Key point: It uses existing docstrings