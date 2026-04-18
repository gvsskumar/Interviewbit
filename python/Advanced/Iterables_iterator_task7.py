# Given a nested list, create an iterator that flattens it (no recursion allowed).
class FlattenIterator:
    def __init__(self, nested_list):
        # Stack will store iterators
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                current = next(self.stack[-1])

                if isinstance(current, list):
                    # Push new iterator onto stack
                    self.stack.append(iter(current))
                else:
                    return current

            except StopIteration:
                # Current iterator exhausted → pop it
                self.stack.pop()

        raise StopIteration


# Usage
nested = [1, [2, [3, 4], 5], 6]

flatten = FlattenIterator(nested)

for num in flatten:
    print(num)