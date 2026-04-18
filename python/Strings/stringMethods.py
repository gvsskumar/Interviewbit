# ✅ Python String Methods – One Example Each
# 1
print("hello".capitalize())              # Hello

# 2
print("HELLO".casefold())               # hello

# 3
print("hi".center(10, "-"))             # ----hi----

# 4
print("banana".count("a"))              # 3

# 5
print("hello".encode())                 # b'hello'

# 6
print("file.txt".endswith(".txt"))      # True

# 7
print("hi\tthere".expandtabs(4))        # hi  there

# 8
print("python".find("th"))              # 2

# 9
print("Hello {}".format("World"))       # Hello World

# 10
data = {"name": "Satya"}
print("Hello {name}".format_map(data))  # Hello Satya

# 11
print("python".index("th"))             # 2

# 12
print("abc123".isalnum())               # True

# 13
print("abc".isalpha())                  # True

# 14
print("abc".isascii())                  # True

# 15
print("123".isdigit())                  # True

# 16
print("var_1".isidentifier())           # True

# 17
print("hello".islower())                # True

# 18
print("123".isnumeric())                # True

# 19
print("hello".isprintable())            # True

# 20
print("   ".isspace())                  # True

# 21
print("Hello World".istitle())          # True

# 22
print("HELLO".isupper())                # True

# 23
print("-".join(["a", "b", "c"]))        # a-b-c

# 24
print("hi".ljust(5, "*"))               # hi***

# 25
print("HELLO".lower())                  # hello

# 26
print("   hello".lstrip())              # 'hello'

# 27
table = str.maketrans("a", "b")
print("a cat".translate(table))         # b cbt

# 28
print("key=value".partition("="))       # ('key', '=', 'value')

# 29
print("unhappy".removeprefix("un"))     # happy

# 30
print("file.txt".removesuffix(".txt"))  # file

# 31
print("I love Java".replace("Java", "Python"))  # I love Python

# 32
print("banana".rfind("a"))              # 5

# 33
print("banana".rindex("a"))             # 5

# 34
print("hi".rjust(5, "*"))               # ***hi

# 35
print("key=value=123".rpartition("="))  # ('key=value', '=', '123')

# 36
print("a,b,c".rsplit(",", 1))           # ['a,b', 'c']

# 37
print("hello   ".rstrip())              # 'hello'

# 38
print("a,b,c".split(","))               # ['a', 'b', 'c']

# 39
print("a\nb\nc".splitlines())           # ['a', 'b', 'c']

# 40
print("python".startswith("py"))        # True

# 41
print("   hello   ".strip())            # 'hello'

# 42
print("Hello".swapcase())               # hELLO

# 43
print("hello world".title())            # Hello World

# 44
print("hello".upper())                  # HELLO

# 45
print("42".zfill(5))                    # 00042