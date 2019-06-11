from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable

T = TypeVar('T', str, int, float)


class BinaryTree(Generic[T], ABC):
    """
    Interface for a graph, edges can be added, and then the set of related vertices can be queried
    """
    @abstractmethod
    def add(self, from_v: T) -> None:
        pass

    @abstractmethod
    def get_right(self) -> BinaryTree[T] or None:
        pass

    @abstractmethod
    def get_left(self) -> BinaryTree[T] or None:
        pass

    @abstractmethod
    def get_value(self) -> T or None:
        pass


class BinaryTreeImpl(BinaryTree[T]):
    __is_to_left: Callable[[T, T], bool]
    __value: T or None
    __left_branch: BinaryTree[T] or None
    __right_branch: BinaryTree[T] or None

    def __init__(self, is_to_left: Callable[[T, T], bool], value: T = None):
        self.__is_to_left = is_to_left
        self.__value = value
        self.__left_branch = None
        self.__right_branch = None

    def __repr__(self):
        return "({} {} {})".format(self.__left_branch, self.__value, self.__right_branch)

    def add(self, item: T):
        if self.__value is None:
            self.__value = item
        elif self.__is_to_left(item, self.__value):
            if self.__left_branch:
                self.__left_branch.add(item)
            else:
                self.__left_branch = BinaryTreeImpl(self.__is_to_left, item)
        else:
            if self.__right_branch:
                self.__right_branch.add(item)
            else:
                self.__right_branch = BinaryTreeImpl(self.__is_to_left, item)

    def get_right(self) -> BinaryTree[T] or None:
        return self.__right_branch

    def get_left(self) -> BinaryTree[T] or None:
        return self.__left_branch

    def get_value(self) -> T or None:
        return self.__value