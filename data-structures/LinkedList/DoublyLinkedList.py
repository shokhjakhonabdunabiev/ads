'''
Implement Doubly LinkedList
P.S. A lot of pointers to take care of!
'''

from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, val: Any, prev: Node = None, next: Node = None):
        self.val = val
        self.prev = prev
        self.next = next


    def __repr__(self):
       return f"Node({self.val})"


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head: Node = None
        self.tail: Node = None


    def length(self) -> int:
        return self.length


    def prepend(self, val: Any):
        node = Node(val)
        self.length += 1
        if self.head is None:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node


    def append(self, val: Any):
        node = Node(val)
        self.length += 1
        if self.tail is None:
            self.tail = self.head = node
            return
    
        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next


    def insert_at(self, index: int, val: Any):
        if index < 0 or index > self.length:
            raise IndexError("index out of bounds")
        elif index == 0:
            self.prepend(val)
            return
        elif index == self.length:
            self.append(val)
            return
        
        self.length += 1
        curr = self.head
        i = 0
        while i != index and curr:
            curr = curr.next
            i += 1
        
        node = Node(val)
        node.prev = curr.prev
        node.next = curr
        curr.prev.next = curr.prev = node


    def remove(self, item: Any) -> Any:
        curr = self.head
        while curr and curr.val != item:
            curr = curr.next
        return self.remove_node(curr)


    def remove_at(self, index: int) -> Any:
        node = self.getAt(index)
        return self.remove_node(node)       


    def remove_node(self, node: Node) -> Any:
        if node is None:
            return
        
        self.length -= 1
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        
        node.prev = node.next = None
        return node.val
    

    def get(self, index: int) -> Any:
        return self.getAt(index)
    

    def getAt(self, index: int):
        if index < 0 or index >= self.length:
            raise IndexError("index out of bounds")
        curr = self.head
        i = 0
        while i != index and curr:
            curr = curr.next
            i += 1
        return curr
    

    def __repr__(self):
        s = []
        cur = self.head
        while cur:
            s.append(f"{cur} =>")
            cur = cur.next
        s.append(f"None")
        return " ".join(s) 


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    print("Init:", linked_list)
    linked_list.prepend(1)
    print("Prepend:", linked_list)
    linked_list.prepend(2)
    print("Prepend:", linked_list)
    linked_list.append(3)
    print("Append:", linked_list)
    linked_list.append(4)
    print("Append:", linked_list)
    linked_list.insert_at(2, 5)
    print("Insert at:", linked_list)
    linked_list.insert_at(0, 6)
    print("Insert at:", linked_list)
    linked_list.insert_at(6, 7)
    print("Insert at:", linked_list)
    linked_list.append(8)
    print("Append:", linked_list)
    linked_list.prepend(9)
    print("Prepend:", linked_list)
    print("Removed element:", linked_list.remove_at(0))
    print("Remove at 0:", linked_list)
    print("Removed element:", linked_list.remove_at(3))
    print("Remove at 3:", linked_list)
    print("Removed element:", linked_list.remove_at(6))
    print("Remove at 6:", linked_list)
    linked_list.append(8)
    print("Insert at:", linked_list)
    # print("Removed element:", linked_list.remove_at(7)) # out of bounds case
    # print("Remove at 7:", linked_list)
    print("Get 0:", linked_list.get(0))
    print("Get 3:", linked_list.get(3))
    print("Get 4:", linked_list.get(4))
    print("Get 10:", linked_list.get(10))