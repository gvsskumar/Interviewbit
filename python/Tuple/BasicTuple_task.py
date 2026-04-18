# Create a tuple with different data types and print each element using a loop.
mytuple = ("Surya",35,5.2,8000,True)
for ele in mytuple:
    print(f"{ele} : {type(ele)}")


# Write a program to find the length of a tuple without using len().
count = 0
for ele in mytuple:
    count += 1
print(count)

#Access the first, last, and middle element of a tuple.
print(f"First Element {mytuple[0]}")
print(f"Second Element {mytuple[-1]}")
print(f"Middle Element {len(mytuple[mytuple/2])}")