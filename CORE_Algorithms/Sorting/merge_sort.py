from typing import List
from math import floor
from CORE_Algorithms.Sorting.common import CompareFunction, Sortable


def merge_sort(input_list: List[Sortable],
               comparator: CompareFunction) -> List[Sortable]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list.
    This function delegates to the recursive form, initialising the left and right pointers.
    """
    return merge_sort_recurse(input_list, comparator, 0, len(input_list) - 1)


def merge_sort_recurse(input_list: List[Sortable],
                       comparator: CompareFunction,
                       left_pointer: int,
                       right_pointer: int) -> List[Sortable]:
    """"
    Recursive form of the merge sort that requires the left and right pointers.
    """
    # Exit condition, the list is a single item
    if left_pointer == right_pointer:
        return [input_list[left_pointer]]

    # Calculate the middle and recurse the sort for both halves
    middle: int = floor((left_pointer + right_pointer) / 2)
    first_half: List[Sortable] = merge_sort_recurse(input_list, comparator, left_pointer, middle)
    second_half: List[Sortable] = merge_sort_recurse(input_list, comparator, middle + 1, right_pointer)

    # Merge the two halves into a single sorted list
    output_list: List[Sortable] = []
    while (len(first_half) > 0) and (len(second_half) > 0):
        comparison: int = comparator(first_half[0], second_half[0])
        if comparison < 0:
            output_list.append(second_half.pop(0))
        else:
            output_list.append(first_half.pop(0))

    # Push any stragglers from the list with items remaining
    output_list.extend(first_half)
    output_list.extend(second_half)

    return output_list
