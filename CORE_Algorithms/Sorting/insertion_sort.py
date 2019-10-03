from typing import List
from CORE_Algorithms.Sorting.common import CompareFunction, Sortable


def insertion_sort(input_list: List[Sortable],
                   comparator: CompareFunction) -> List[Sortable]:
    """"
    Sorts the input list, using the provided comparator
    to decide if two elements are in the correct order.
    Returns a copy of the list sorted, makes no changes to input list
    """
    output_list: List[Sortable] = list(input_list)

    for index in range(1, len(output_list)):
        for workBackwards in range(index, 0, -1):
            lower: int = workBackwards - 1
            upper: int = workBackwards
            comparison: int = comparator(output_list[lower], output_list[upper])

            # The comparator returns -1 if the first item is 'greater than' the second one
            if comparison < 0:
                # Temporary variable to prevent overwrites
                swap: Sortable = output_list[lower]
                output_list[lower] = output_list[upper]
                output_list[upper] = swap

    return output_list
