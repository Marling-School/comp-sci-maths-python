from typing import Dict, Callable
from CORE_Algorithms.Stack.StackImpl import Stack, StackImpl

operators: Dict[str, Callable[[float, float], float]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


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
                b: float = my_stack.pop()
                a: float = my_stack.pop()
                ab = op(a, b)
                # print("Evaluating {} {} {} = {}".format(a, e, b, ab))
                my_stack.push(ab)
            else:
                if e not in values:
                    raise Exception(
                        "Could not find {} in values for expression {}".format(e, self.__expression))

                value: float = values.get(e)
                my_stack.push(value)

        return my_stack.pop()
