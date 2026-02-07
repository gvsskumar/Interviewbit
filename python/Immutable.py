# Immutable in Python examples
# Example 1 Int data type
x = 10;
y = x;
x = 20;
print(x); # 20
print(y); # 10
# Y gets the value of x at assignment time, Integers are immutable.

# Example 2
a = 25;
a = "Hello";
print(a); # Hello

# Example 3
a = 25;
print(type(a)); # <class 'int'>
a = "Hello";
print(type(a)); # <class 'str'>

#Example -2 Strings are immutable
str1 = "Hello";
str2 = str1;
str1 = "Bye";
print(str1); # Bye
print(str2); # Hello

#Example -3 Boolean are immutable
bool1 = True;
bool2 = bool1;
bool1 = False;
print(bool1); # False
print(bool2); # True

# Float are immutable
float1 = 1.0;
float2 = float1;
float1 = 2.0;
print(float1); # 2.0
print(float2); # 1.0

# Example -4 None are immutable
none1 = None;
none2 = none1;
none1 = "Hello";
print(none1); # Hello
print(none2); # None

#Example -5 Tuple are immutable
tuple1 = (1, 2, 3);
tuple2 = tuple1;
tuple1 = (4, 5, 6);
print(tuple1); # (4, 5, 6)
print(tuple2); # (1, 2, 3)

#Example -6 List are immutable
list1 = [1, 2, 3];
list2 = list1;
list1 = [4, 5, 6];
print(list1); # [4, 5, 6]
print(list2); # [1, 2, 3]

#Example -7 Dictionary are immutable
dict1 = {"a": 1, "b": 2};
dict2 = dict1;
dict1 = {"c": 3, "d": 4};
print(dict1); # {'c': 3, 'd': 4}
print(dict2); # {'a': 1, 'b': 2}

#Example -8 Set are immutable
set1 = {1, 2, 3};
set2 = set1;
set1 = {4, 5, 6};
print(set1); # {4, 5, 6}
print(set2); # {1, 2, 3}

#Example -9 frozenset are immutable
frozenset1 = frozenset({1, 2, 3});
frozenset2 = frozenset1;
frozenset1 = frozenset({4, 5, 6});
print(frozenset1); # frozenset({4, 5, 6})
print(frozenset2); # frozenset({1, 2, 3})

#Example -10 Bytes are immutable
bytes1 = b"Hello";
bytes2 = bytes1;
bytes1 = b"Bye";
print(bytes1); # b'Bye'
print(bytes2); # b'Hello'

#Example -11 Bytearray are immutable
bytearray1 = bytearray(b"Hello");
bytearray2 = bytearray1;
bytearray1 = bytearray(b"Bye");
print(bytearray1); # bytearray(b'Bye')
print(bytearray2); # bytearray(b'Hello')

#Example -12 Complex are immutable
complex1 = 1 + 2j;
complex2 = complex1;
complex1 = 3 + 4j;
print(complex1); # (3+4j)
print(complex2); # (1+2j)

#Example -13 Range are immutable
range1 = range(5);
range2 = range1;
range1 = range(10);
print(range1); # range(0, 10)
print(range2); # range(0, 5)

#Example -14 Ellipsis are immutable
ellipsis1 = ...;
ellipsis2 = ellipsis1;
ellipsis1 = ...;
print(ellipsis1); # ...
print(ellipsis2); # ...

#Example -15 NotImplemented are immutable
notimplemented1 = NotImplemented;
notimplemented2 = notimplemented1;
notimplemented1 = NotImplemented;
print(notimplemented1); # NotImplemented
print(notimplemented2); # NotImplemented

#Example -16 None are immutable
none1 = None;
none2 = none1;
none1 = None;
print(none1); # None
print(none2); # None
