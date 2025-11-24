'''
Linked List consist of nodes where each node had value and pointer to next value.
LinkedList has the following functionalities:
    - append
    - prepend
    - insertAt
    - removeAt
    - get
'''

from __future__ import annotations # Can use not defined class in its constructor
# quotes can be used too "ListNode" instead of import above
from typing import Any

class Node:
    def __init__(self, val: Any, next: Node = None):
        self.val = val
        self.next = next

    def __repr__(self):
       return f"Node({self.val})"

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head: Node = None
        self.tail: Node = None

    # Time Complexity: O(1)
    def prepend(self, val: Any):
        node = Node(val)
        self.length += 1

        if self.length == 1:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head = node

    # Time Complexity: O(1)
    def append(self, val: Any):
        node = Node(val)
        self.length += 1

        if self.length == 0:
            self.tail = self.head = node
            return

        self.tail.next = node
        self.tail = self.tail.next

    # Time Complexity: O(n)
    def insert_at(self, index: int, val: Any):
        if index < 0 or index > self.length:
            raise Exception("out of bounds")
        elif index == self.length:
            self.append(val)
            return
        elif index == 0:
            self.prepend(val)
            return
        
        node = Node(val)
        self.length += 1

        prev, curr = None, self.head
        i = 0
        while i != index and curr:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = node
        node.next = curr

    # Time Complexity: O(n)
    def remove_at(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise Exception("out of bounds") # we can terminate function silently too
        
        self.length -= 1
        if index == 0:
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.val

        prev, curr = None, self.head
        i = 0
        while i != index and curr:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        curr.next = None

        if index == self.length:
            self.tail = prev

        return curr.val if curr else None

    # Time Complexity: O(n)
    def get(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise Exception("out of bounds")

        curr = self.head
        i = 0
        while i != index and curr:
            curr = curr.next
            i += 1
        
        return curr.val if curr else None
    
    def __repr__(self):
        s = []
        cur = self.head
        while cur:
            s.append(f"{cur} =>")
            cur = cur.next
        s.append(f"None")
        return " ".join(s) 


if __name__ == "__main__":
    linked_list = LinkedList()
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