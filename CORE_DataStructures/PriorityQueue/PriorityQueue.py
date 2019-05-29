from typing import Tuple, List, TypeVar, Generic
from CORE_DataStructures.LinkedList.LinkedList import LinkedList

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    __items: LinkedList[Tuple[T, int]]

    def __init__(self):
        self.__items = LinkedList()

    def __repr__(self):
        return "{}".format(self.__items)

    def is_empty(self):
        return self.__items.is_empty()

    def enqueue(self, item: T, priority: int):
        for prioritisedItem, index in self.__items:
            if priority > prioritisedItem[1]:
                self.__items.insert((item, priority), index)
                return
        self.__items.append((item, priority))

    def dequeue(self) -> Tuple[T, int] or None:
        if self.is_empty():
            raise Exception('Queue Empty')

        item: Tuple[T, int] = self.__items.get(0)
        self.__items.remove(0)
        return item


