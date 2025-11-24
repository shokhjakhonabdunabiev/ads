'''
Implement Heap
- insert: TC - O(n*log(n))
- delete: TC - O(n*log(n))
'''
class MinHeap:
    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, val: int):
        self.data[self.length] = val
        self.heapify_up(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            return -1
        
        out = self.data[0]
        self.length -= 1

        if self.length == 0:
            self.data = []
            return out

        self.data[0] = self.data[self.length]
        self.heapify_down(0)
        return out

    def heapify_down(self, idx: int):
        if idx >= self.length:
            return
        
        l_idx = self.left_child(idx)
        r_idx = self.right_child(idx)
        if l_idx >= self.length:
            return
        
        l_val = self.data[l_idx]
        r_val = self.data[r_idx]
        val = self.data[idx]

        if l_val > r_val and val > r_val:
            self.data[idx], self.data[r_idx] = self.data[r_idx], self.data[idx]
            self.heapify_down(r_idx)
        elif r_val > l_val and val > l_val:
            self.data[idx], self.data[l_idx] = self.data[l_idx], self.data[idx]
            self.heapify_down(l_idx)

    def heapify_up(self, idx: int):
        if idx == 0:
            return
    
        p_idx = self.parent()
        p_val = self.data[p_idx]
        val = self.data[idx]

        if p_val > val:
            self.data[idx], self.data[p_idx] = self.data[p_idx], self.data[idx]
            self.heapify_up(p_idx)

    def parent(self, idx: int) -> int:
        return (idx - 1) // 2
    
    def left_child(self, idx: int) -> int:
        return idx * 2 + 1
    
    def right_child(self, idx: int) -> int:
        return idx * 2 + 2