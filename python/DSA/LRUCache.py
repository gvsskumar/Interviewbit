from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        
        if key not in self.cache:
            return -1
        
        # Move accessed key to end
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value):
        
        if key in self.cache:
            # Move key to end (recently used)
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        # Remove least recently used (LRU)
        if len(self.cache) > self.capacity:
            removed_key, removed_value = self.cache.popitem(last=False)
            print(f"Evicted: {removed_key} -> {removed_value}")

    def display(self):
        
        print("Cache state:", dict(self.cache))


# ✅ Move this OUTSIDE the class
# This ensures the code runs only when the file is executed directly.
if __name__ == "__main__":
    lru = LRUCache(3)
    
    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    lru.display()  
    # Expected: {1: 'A', 2: 'B', 3: 'C'}

    lru.get(1)  
    lru.display()  
    # Expected: {2: 'B', 3: 'C', 1: 'A'}

    lru.put(4, "D")
    # Evicts keys 2 and then 3

    lru.display()  
    # Expected: {1: 'A', 4: 'D', 5: 'E'}

    print(lru.get(2))  # -1 (not found)