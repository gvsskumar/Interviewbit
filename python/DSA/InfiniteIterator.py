# Build a custom iterator class supporting infinite sequences
class InfiniteCounter:
    def __init__(self,start=0,step=1):
        self.current = start
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        value = self.current
        self.current +=self.step
        return value

counter = InfiniteCounter(1,2)
for index,val in enumerate(counter):
    if index == 5:
        break
    print(val)