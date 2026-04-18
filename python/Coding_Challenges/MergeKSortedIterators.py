# Merge K Sorted Iterators
import heapq

def mergedsorted_iterator(iterator):
    min_heap = []

    for i,it in enumerate(iterator):
        try:
            first_element = next(it)
            heapq.heappush(min_heap,(first_element,i,it))
        except StopIteration:
            continue

    while min_heap:
        value, i, it = heapq.heappop(min_heap)
        yield value
        try:
            next_element = next(it)
            heapq.heappush(min_heap,(next_element,i,it))
        except StopIteration:
            continue    

it1 = iter([1,4,8])
it2 = iter([2,7,9])
it3 = iter([3,5,6])
iterator = [it1,it2,it3]
result = mergedsorted_iterator(iterator)
for item in result:
    print(item)
