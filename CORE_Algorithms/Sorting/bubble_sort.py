from typing import List, TypeVar, Callable

T = TypeVar('T')


def bubble_sort(input_list: List[T],
                comparator: Callable[[T, T], bool]) -> List[T]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list
    """
    output_list: List[T] = list(input_list)
    for top in range(len(input_list), 1, -1):
        for current in range(top - 1):
            if comparator(output_list[current], output_list[current + 1]):
                swap: T = output_list[current]
                output_list[current] = output_list[current + 1]
                output_list[current + 1] = swap
    return output_list
