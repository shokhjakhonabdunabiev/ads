'''
Least Frequently Used (LFU) Cache
'''
import collections

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.node_map = dict()
    
    def insert(self, val: int):
        node = Node(val)
        self.node_map[val] = node
        self.length += 1

        if self.head is None:
            self.head = self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def popleft(self):
        node = self.head
        self.pop(node.val)
        return node.val

    def pop(self, val: int):
        if val not in self.node_map:
            return

        self.length -= 1
        node = self.node_map[val]
        self.node_map.pop(val, None)

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = node.next = None
        

class LFU:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.cache = dict() # <key, value>
        self.cnt_map = collections.defaultdict(int) # <key, cnt>
        self.list_map = collections.defaultdict(LinkedList) # <cnt, LinkedList> 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.counter(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
            
        if key not in self.cache and len(self.cache) == self.cap:
            res = self.list_map[self.min_freq].popleft()
            self.cache.pop(res)
            self.cnt_map.pop(res)

        self.cache[key] = value
        self.counter(key)
        self.min_freq = min(self.min_freq, self.cnt_map[key])
    
    def counter(self, key: int):
        cnt = self.cnt_map[key]
        self.cnt_map[key] += 1
        self.list_map[cnt].pop(key)
        self.list_map[cnt+1].insert(key)
        if cnt == self.min_freq and self.list_map[cnt].length == 0:
            self.min_freq += 1
        

if __name__ == "__main__":
    lfu = LFU(1)
    lfu.put(1, 1)
    lfu.put(2, 2)
    lfu.get(1)
    lfu.get(2)