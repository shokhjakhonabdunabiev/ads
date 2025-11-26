'''
Least Recently Used (LRU) Cache.

- LRU cache is used to keep track of the least recently used elements.
- Lookup for the least recently used node should be constant.
- Doubly Linked List together with HashMap can make the constant look up possible.

LRU should have the following functionalities:
    - get least 
'''

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRU:
    def __init__(self, cap=10):
        self.cap = cap
        self.head: Node = None
        self.tail: Node = None
        self.cache: dict[int, Node] = dict()

    def put(self, key: int, val: int):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, val)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.head
            self.remove(lru)
            del self.cache[lru.key]

    def get(self, key: int):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def insert(self, node: Node):
        if self.tail is None:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, node: Node):
        if node is None:
            return
        
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.prev = node.next = None
        
if __name__ == "__main__":
    lru_cache = LRU(1)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.cache)
    print(lru_cache.get(1))
    print(lru_cache.get(2))