# import os
# # os.getcwd
# # os.listdir
# # os.mkdir
# # os.rmdir
# # os.rename
# # os.path.isdir
# # os.path.isfile
# # os.path.islink
# # os.path.exists

# #(1) Current directory
# print(os.getcwd())

# #(2) Change directory
# # print(os.chdir("/path/to/folder"))

# #(3) List files & folders
# items = os.listdir()
# for item in items:
#     print(item)

# #(4) Create directories
# if not os.path.isdir('test1'):
#     os.mkdir('test1')

# #(5) Remove directories
# os.rmdir('test1')   

# # Create file
# with open('sample.txt','w') as f:
#     if not os.path.isfile('sample.txt'):
#         f.write("Hello world")

# # Delete file
# os.remove('sample.txt')   

# # Rename file



def fibnoci(n):
    f1,f2 = 0,1
    for _ in range(1,n):
        f1,f2 = f2,f1+f2
        print(f"F1: {f1} , F2: {f2}")
        


def wrap():
    @fibnoci(5)
    print("Hello")
wrap()