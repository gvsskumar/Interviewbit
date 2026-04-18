# Implement a custom iterator that generates Fibonacci numbers up to n.
class myiterator:
    def __init__(self,n):
        self.n = n
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a >self.n:
            raise StopIteration
        value = self.a
        self.a,self.b = self.b,self.a+self.b
        return value

fib = myiterator(5)
for fn in fib:
    print(fn)        