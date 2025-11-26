'''
Implement HashMap.

- HashMap is implemented using array and hashing under the hood.
- HashMap is great for constant lookups based of key
- Each element that stored in HashMap is hashed and placed in the hashed value modulo length of array (hash % capacity).
- Hashing may cause collisions, so it is recommended to keep track of load factor. And double the capacity of array,
  when load factor reaches certain point (ususally 0.7)
- when collisions occur, there are several ways/implementations to handle them:
    - Separate chaining with Python lists
    - Open addressing with linear probing
    - Quadratic probing / double hashing
    - Robin Hood hashing
    - Cuckoo hashing
    - Hopscotch hashing
'''

class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashMap:
    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.data: list[ListNode] = [None] * self.capacity

    def put(self, key, val):
        self.length += 1
        if self.load_factor() >= 0.7:
            self.resize()
        
        idx = self.hash(key)
        node = ListNode(key, val)

        curr = self.data[idx]
        if curr is None:
            self.data[idx] = node
            return

        prev = None
        while curr:
            if curr.key == key:
                curr.val = val
                return
            prev = curr
            curr = curr.next
        prev.next = node
        
    def get(self, key):
        idx = self.hash(key)
        curr = self.data[idx]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
    
    def remove(self, key):
        idx = self.hash(key)
        prev, curr = None, self.data[idx]
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        
        if curr is None:
            return

        self.length -= 1

        if curr == self.data[idx]:
            self.data[idx] = curr.next
        if prev:
            prev.next = curr.next

        return curr.val

    def hash(self, key):
        return hash(key) % self.capacity
    
    def load_factor(self):
        return self.length / self.capacity        

    def resize(self):
        self.capacity *= 2
        old_data = self.data
        self.data = [None] * self.capacity

        for node in old_data:
            while node:
                self.put(node.key, node.val)
                node = node.next

if __name__ == "__main__":
    mp = HashMap()
    mp.put("a", 1)
    mp.put("b", 2)
    mp.put("c", 3)
    mp.put("d", 4)
    mp.put("e", 5)
    mp.put("f", 6)
    print("Cap:", mp.capacity)
    mp.put("h", 7)
    print("Cap:", mp.capacity)
    mp.put("i", 8)
    mp.put("j", 9)
    mp.put("k", 10)
    mp.put("l", 11)
    print(mp.get("a"))
    print(mp.get("b"))
    print(mp.get("c"))
    print(mp.get("d"))
    print(mp.get("e"))
    print(mp.get("f"))
    print(mp.get("h"))
    print(mp.get("i"))
    print(mp.get("j"))
    print(mp.get("k"))
    print(mp.get("l"))
    print(mp.get("m"))
    mp.remove("a")
    print(mp.get("a"))
    mp.put("a", 1000)
    print(mp.get("a"))
    mp.put("a", 2000)
    print(mp.get("a"))