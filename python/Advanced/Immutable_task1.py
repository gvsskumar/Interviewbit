# Challenge 2: Modify Mutable vs Immutable
def modify(x, lst):
    x += 10
    lst.append(100)

a = 5
b = [1,2]

modify(a, b)

print(a)  # 5 (immutable)
print(b)  # [1,2,100] (mutable)