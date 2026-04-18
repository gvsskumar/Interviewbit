# Write a class that mimics range() behavior using iterator protocol. 
class MyRange:
    def __init__(self, start, stop=None, step=1):
        # Handle range(n) case
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop

        if step == 0:
            raise ValueError("step cannot be 0")

        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        # Handle positive step
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        # Handle negative step
        else:
            if self.current <= self.stop:
                raise StopIteration

        value = self.current
        self.current += self.step
        return value


# Usage examples
print(list(MyRange(5)))          # [0, 1, 2, 3, 4]
print(list(MyRange(2, 10, 2)))  # [2, 4, 6, 8]
print(list(MyRange(10, 2, -2))) # [10, 8, 6, 4]