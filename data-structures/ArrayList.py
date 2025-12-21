'''
Implementation can be extended with load factor.
'''

class ArrayList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.length = 0
        
    def add(self, value: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = value
        self.length += 1
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        return self.array[index]
    
    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.length:
            return
        self.array[index] = value
    
    def remove(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        i = index
        while i < self.length - 1:
            self.array[i] = self.array[i + 1]
            i += 1
        self.array[i] = None
    
    def resize(self) -> None:
        old_capacity = self.capacity
        self.capacity = old_capacity * 2
        new_array = [None] * self.capacity
        for i in range(old_capacity):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def __repr__(self) -> str:
        return str(self.array)
    
if __name__ == "__main__":
    lst = ArrayList(2)
    print(lst)
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(4)
    lst.add(5)
    print(lst)
    lst.set(3, 3)
    lst.set(6, 3)
    print(lst)
    lst.remove(3)
    print(lst)
        