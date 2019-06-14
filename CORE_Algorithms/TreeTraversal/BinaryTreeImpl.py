from __future__ import annotations
from typing import TypeVar, Callable, List

from CORE_Algorithms.TreeTraversal.BinaryTree import BinaryTree

T = TypeVar('T', str, int, float)


class BinaryTreeImpl(BinaryTree[T]):
    __compare: Callable[[T, T], bool]
    __value: T or None
    __left_branch: BinaryTree[T] or None
    __right_branch: BinaryTree[T] or None

    def __init__(self, compare: Callable[[T, T], bool], value: T = None):
        self.__compare = compare
        self.__value = value
        self.__left_branch = None
        self.__right_branch = None

    def __repr__(self):
        return "({} {} {})".format(self.__left_branch, self.__value, self.__right_branch)

    def __eq__(self, other):
        return (self.__value == other.__value)\
               and (self.__left_branch == other.__left_branch)\
               and (self.__right_branch == other.__right_branch)

    def add(self, item: T):
        if self.__value is None:
            self.__value = item
        elif self.__compare(item, self.__value) == 1:
            if self.__left_branch:
                self.__left_branch.add(item)
            else:
                self.__left_branch = BinaryTreeImpl(self.__compare, item)
        else:
            if self.__right_branch:
                self.__right_branch.add(item)
            else:
                self.__right_branch = BinaryTreeImpl(self.__compare, item)

    def get_right(self) -> BinaryTree[T] or None:
        return self.__right_branch

    def get_left(self) -> BinaryTree[T] or None:
        return self.__left_branch

    def get_value(self) -> T or None:
        return self.__value

    def pre_order(self) -> List[T]:
        nodes: List[T] = [self.__value]
        if self.__left_branch is not None:
            nodes.extend(self.__left_branch.pre_order())
        if self.__right_branch is not None:
            nodes.extend(self.__right_branch.pre_order())
        return nodes

    def primitive_compare(self) -> List[T]:
        nodes: List[T] = []
        if self.__left_branch is not None:
            nodes.extend(self.__left_branch.primitive_compare())
        nodes.append(self.__value)
        if self.__right_branch is not None:
            nodes.extend(self.__right_branch.primitive_compare())
        return nodes

    def post_order(self) -> List[T]:
        nodes: List[T] = []
        if self.__left_branch is not None:
            nodes.extend(self.__left_branch.pre_order())
        if self.__right_branch is not None:
            nodes.extend(self.__right_branch.pre_order())
        nodes.append(self.__value)
        return nodes
