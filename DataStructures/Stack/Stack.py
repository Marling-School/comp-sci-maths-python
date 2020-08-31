from typing import List, TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    capacity: int
    data: List[T or None]
    top: int

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = 0

    def __str__(self):
        return "{}".format(self.data)

    def is_full(self):
        return self.top == self.capacity

    def is_empty(self):
        return self.top == 0

    def push(self, item: T):
        if self.is_full():
            raise Exception('Stack Overflow')

        self.data[self.top] = item
        self.top += 1

    def peek(self) -> T:
        if self.is_empty():
            raise Exception('Stack Underflow')
        return self.data[self.top - 1]

    def pop(self) -> T:
        item: T = self.peek()
        self.top -= 1
        return item
