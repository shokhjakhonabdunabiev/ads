from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, val: Any, prev: Node = None):
        self.val = val
        self.prev = prev

    def __repr__(self):
        return f"Node({self.val})"

class Stack:
    def __init__(self):
        self.head: Node = None
        self.length = 0

    def push(self, val: Any):
        node = Node(val)
        self.length += 1
        if self.length == 1:
            self.head = node
            return

        node.prev = self.head
        self.head = node

    def pop(self) -> Any:
        if self.length == 0:
            return None

        self.length -= 1
        head = self.head
        self.head = self.head.prev
        return head.val

    def peek(self) -> Any:
        if self.length == 0:
            return None
        return self.head.val

    def __repr__(self):
        s = []
        curr = self.head
        while curr:
            s.append(f"{curr} =>")
            curr = curr.prev
        s.append("None")
        return " ".join(s)


if __name__ == "__main__":
    stack = Stack()
    print("Init:", stack)
    stack.push(1)
    print("Push:", stack)
    stack.push(2)
    print("Push:", stack)
    stack.push(3)
    print("Push:", stack)
    stack.push(4)
    print("Push:", stack)
    print("Peek:", stack.peek())
    stack.pop()
    print("Pop:", stack)
    stack.pop()
    print("Pop:", stack)
    stack.pop()
    print("Pop:", stack)
    stack.pop()
    print("Pop:", stack)
    print("Peek:", stack.peek())
    
