from typing import Any


class CircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.length = 0
        self.data: list[Any] = [None] * k
        self.head: int | None = None
        self.tail: int | None = None

    def enQueue(self, value: int) -> bool:
        if self.length == self.capacity:
            return False

        self.length += 1
        if self.length == 1:
            self.head = self.tail = 0
            self.data[0] = value
            return True

        assert isinstance(self.tail, int)

        self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False

        assert isinstance(self.head, int)

        self.length -= 1
        self.data[self.head] = None
        if self.length == 0:
            self.head = self.tail = None
            return True

        self.head = (self.head + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.head is None:
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.tail is None:
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

