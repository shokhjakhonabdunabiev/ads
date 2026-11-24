from __future__ import annotations

from typing import Any

""" Implement Queue """


class Node:
    def __init__(self, val: Any, next: Node | None = None):
        self.val: Any = val
        self.next: Node | None = next

    def __repr__(self):
        return f"Node({self.val})"


class Queue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    # Time Comeplexity: O(1)
    # Space Complexity: O(1)
    def enque(self, val: Any):
        node = Node(val)
        self.length += 1

        if self.head == None or self.tail == None:  # we can use (self.head is None) too
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    # Time Comeplexity: O(1)
    # Space Complexity: O(1)
    def dequeu(self) -> Any:
        if self.head == None:
            return None

        self.length -= 1
        head = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return head.val

    # Time Comeplexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> Any:
        if self.head == None:
            return None
        return self.head.val

    def __repr__(self):
        s = []
        curr = self.head
        while curr:
            s.append(f"{curr} <=")
            curr = curr.next
        s.append("None")
        return " ".join(s)


if __name__ == "__main__":
    q = Queue()
    print("Init:", q)
    q.enque(1)
    print("Enque:", q)
    q.enque(2)
    print("Enque:", q)
    q.enque(3)
    print("Enque:", q)
    print("Peek:", q.peek())
    q.dequeu()
    print("Deque:", q)
    print("Peek:", q.peek())
    q.dequeu()
    print("Deque:", q)
    q.dequeu()
    print("Deque:", q)
    print("Peek:", q.peek())
    q.dequeu()
    print("Deque:", q)
