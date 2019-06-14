from typing import List, Callable, TypeVar

Sortable = TypeVar('Sortable')

# This is the standard form for sort functions
CompareFunction = Callable[[Sortable, Sortable], int]
SortFunction = Callable[[List[Sortable], CompareFunction], List[Sortable]]


# Standard Compare Functions
def in_order(x, y):
    if x == y:
        return 0
    elif x < y:
        return 1
    else:
        return -1


def reverse_order(x, y):
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1
