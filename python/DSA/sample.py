from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity):
        if capacity <= 0:
            print("Capacity must be >0")
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self,key:int):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self,key:int,value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            removed_key,removed_value = self.cache.popitem(last=False)
            print(f"removed_key : {removed_key}, removed_value: {removed_value}")

    def display(self):
        print("cache sate",dict(self.cache))

if __name__ == "__main__":
    lru = LRUCache(3)

    lru.put(1,'A')
    lru.put(2,'B')
    lru.put(3,'C')
    lru.display()

