from typing import List
from CORE_Algorithms.Sorting.common import CompareFunction, Sortable


def bubble_sort(input_list: List[Sortable],
                comparator: CompareFunction) -> List[Sortable]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list
    """
    output_list: List[Sortable] = list(input_list)
    for top in range(len(input_list), 1, -1):
        for current in range(top - 1):
            comparison: int = comparator(output_list[current], output_list[current + 1])
            if comparison < 0:
                swap: Sortable = output_list[current]
                output_list[current] = output_list[current + 1]
                output_list[current + 1] = swap
    return output_list
