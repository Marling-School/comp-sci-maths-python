from __future__ import annotations
from typing import TypeVar, Generic, Callable

T = TypeVar('T')


class ListItem(Generic[T]):
    __value: T
    __next_item: ListItem[T] or None

    def __init__(self, value: T):
        self.__value = value
        self.__next_item = None

    def set_next(self, next_item: T):
        self.__next_item = next_item

    def get_value(self) -> T:
        return self.__value

    def get_next_item(self) -> ListItem[T]:
        return self.__next_item

    def __repr__(self):
        return str(self.__value)


class LinkedListIterator(Generic[T]):
    __current: ListItem[T]

    def __init__(self, start_item: ListItem[T]):
        self.__current = start_item

    def __iter__(self) -> T:
        return self

    def __next__(self):
        item: ListItem[T] = self.__current
        self.__current = item.get_next_item()
        return item.get_value()


class LinkedList(Generic[T]):
    __start_item: ListItem[T] or None

    def __init__(self):
        self.__start_item = None

    def insert_at_start(self, item: T):
        if self.__start_item is None:
            self.__start_item = ListItem(item)
        else:
            old_start_item: ListItem[T] = self.__start_item
            self.__start_item = ListItem(item)
            self.__start_item.set_next(old_start_item)

    def insert_at_end(self, item: T):
        if self.__start_item is None:
            self.__start_item = ListItem(item)
        else:
            curr_item: ListItem[T] = self.__start_item
            while curr_item.get_next_item() is not None:
                curr_item = curr_item.get_next_item()
            curr_item.set_next(ListItem[T](item))

    def insert_after_match(self, item: T, matcher: Callable[[T], bool]):
        new_item: ListItem[T] = ListItem(item)
        if self.__start_item is None:
            self.__start_item = new_item
        elif matcher(self.__start_item.get_value()):
            new_item.set_next(self.__start_item.get_next_item())
            self.__start_item.set_next(new_item)
        else:
            curr_item: ListItem[T] = self.__start_item
            while curr_item is not None:
                if matcher(curr_item.get_value()):
                    old_next_item: ListItem[T] = curr_item.get_next_item()
                    curr_item.set_next(new_item)
                    new_item.set_next(old_next_item)
                    break
                else:
                    curr_item = curr_item.get_next_item()

    def insert_before_match(self, item: T, matcher: Callable[[T], bool]):
        new_item: ListItem[T] = ListItem(item)

        if self.__start_item is None:
            self.__start_item = new_item
        elif matcher(self.__start_item.get_value()):
            new_item.set_next(self.__start_item)
            self.__start_item = new_item
        else:
            prev_item: ListItem[T] or None = None
            curr_item: ListItem[T] = self.__start_item
            while curr_item is not None:
                if matcher(curr_item.get_value()):
                    if prev_item is not None:
                        prev_item.set_next(new_item)
                    new_item.set_next(curr_item)
                    break
                else:
                    prev_item = curr_item
                    curr_item = curr_item.get_next_item()

    def get_at_index(self, index: int):
        _index: int = 0
        curr_item: ListItem[T] = self.__start_item
        while curr_item is not None:
            if _index == index:
                return curr_item.get_value()
            curr_item = curr_item.get_next_item()
            _index += 1

    def items(self) -> LinkedListIterator[T]:
        return LinkedListIterator(self.__start_item)

    def iterate_items(self, callback: Callable[[T], None]):
        curr_item: ListItem[T] = self.__start_item
        while curr_item is not None:
            callback(curr_item.get_value())
            curr_item = curr_item.get_next_item()

    def __repr__(self):
        as_str: str = ''
        curr_item: ListItem[T] = self.__start_item
        while curr_item is not None:
            as_str += ' ' + str(curr_item.get_value())
            curr_item = curr_item.get_next_item()
        return as_str

