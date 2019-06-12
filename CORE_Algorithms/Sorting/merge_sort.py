from typing import List, TypeVar, Callable, Optional
from math import floor

T = TypeVar('T')


def merge_sort(input_list: List[T],
               comparator: Callable[[T, T], bool],
               left_pointer: Optional[int] = None,
               right_pointer: Optional[int] = None) -> List[T]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list
    """
    if left_pointer is None:
        left_pointer = 0
    if right_pointer is None:
        right_pointer = len(input_list) - 1

    # Exit condition, the list is a single item
    if left_pointer == right_pointer:
        return [input_list[left_pointer]]

    # Calculate the middle and recurse the sort for both halves
    middle: int = floor((left_pointer + right_pointer) / 2)
    first_half: List[T] = merge_sort(input_list, comparator, left_pointer, middle)
    second_half: List[T] = merge_sort(input_list, comparator, middle + 1, right_pointer)

    # Merge the two halves into a single sorted list
    output_list: List[T] = []
    while (len(first_half) > 0) and (len(second_half) > 0):
        if comparator(first_half[0], second_half[0]):
            output_list.append(second_half.pop(0))
        else:
            output_list.append(first_half.pop(0))

    # Push any stragglers from the list with items remaining
    output_list.extend(first_half)
    output_list.extend(second_half)

    return output_list
