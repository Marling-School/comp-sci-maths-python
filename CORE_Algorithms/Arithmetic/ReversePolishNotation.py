from typing import Dict, Callable
from CORE_Algorithms.Stack.StackImpl import Stack, StackImpl

operators: Dict[str, Callable[[float, float], float]] = dict()
operators['+'] = lambda a, b: a + b
operators['-'] = lambda a, b: a - b
operators['*'] = lambda a, b: a * b
operators['/'] = lambda a, b: a / b


class ReversePolishNotation:
    """
    An instance of this class is created with an algebraic expression.
    It can then be called upon to evaluate expressions given dictionaries of values.
    The expressions must be well formed RPN using single letter algebraic substitutions
    """
    __expression: str

    def __init__(self, expression: str):
        self.__expression = expression

    def evaluate(self, values: Dict[str, float]):
        my_stack: Stack[float] = StackImpl[float]()

        for e in self.__expression:
            if e in operators:
                op: Callable[[float, float], float] = operators[e]
                a: float = my_stack.pop()
                b: float = my_stack.pop()
                ab = op(a, b)
                my_stack.push(ab)
            else:
                value: float = values.get(e)
                my_stack.push(value)

        return my_stack.pop()
