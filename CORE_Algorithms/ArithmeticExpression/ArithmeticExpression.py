from __future__ import annotations
from enum import Enum
from CORE_Algorithms.TreeTraversal.BinaryTreeImpl import BinaryTree, BinaryTreeImpl
from CORE_Algorithms.ReversePolishNotation.ReversePolishNotation import operators


class Notation(Enum):
    prefix = 1,
    infix = 2,
    postfix = 3


class ExpressionNode:
    __id: int
    __op: str

    def is_to_left(self, other: ExpressionNode) -> bool:
        return self.__id < other.__id


class ArithmeticExpression:
    __expression_tree: BinaryTree[ExpressionNode]

    def __init__(self, expression: str):
        self.__expression_tree = BinaryTreeImpl[ExpressionNode](lambda x, y: x.is_to_left(y))
