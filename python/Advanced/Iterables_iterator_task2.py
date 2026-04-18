# Challenge 2: Check if Object is Iterable
from collections.abc import Iterable
def is_iterable(obj):
   return isinstance(obj,Iterable) 
print(is_iterable(10))  # False
print(is_iterable([1,2,3])) # True
