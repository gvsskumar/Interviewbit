# Implement an iterator that returns even numbers up to n.
class EvenNumber:
    def __init__(self,max_num):
        self.max_num = max_num
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.num += 2
        if self.num <= self.max_num:
            return self.num
        raise StopIteration
    
evens = EvenNumber(10)
for n in evens:
    print(n)    
