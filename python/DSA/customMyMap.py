class MyMap:
    def __init__(self,func,iterable):
        self.func = func
        self.itertor = iter(iterable)
    def __iter__(self):
        return self  
    def __next__(self):
        item = next(self.itertor)
        return self.func(item)
    
def square(x):
    return x*x

def evenNumber(x):
    if x%2==0:
     return x
    
num = [1,2,3,4]
mapped = MyMap(square,num)
for val in mapped:
    print(val)    
