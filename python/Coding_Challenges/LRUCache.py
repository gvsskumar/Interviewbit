class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self,node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next = node
        self.head = node

    def _remove(self,node):
        nxt = node.next
        prv = node.prev
        node.next = nxt
        node.prev = prv

    def _move_to_head(self,node):
        self._remove(node)
        self._add(node)

    def get(self,key:int)->int:
        if key not in self.cache:
            return -1
        
# Tobe continued lattter        
                
        