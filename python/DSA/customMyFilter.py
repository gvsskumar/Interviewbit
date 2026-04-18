class MyFilter:
    def __init__(self,func,iterable):
        self.func = func
        self.iterator = iter(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            item = next(self.iterator)
            if self.func(item):
                return item
def evenNumber(x):
    if x%2==0:
        return x
num = [1,2,3,4,5,6]
result = MyFilter(evenNumber,num)
for val in result:
    print(val)                
