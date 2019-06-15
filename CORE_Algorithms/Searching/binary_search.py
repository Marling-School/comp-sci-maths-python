from typing import Optional, List, Tuple
from math import floor
from CORE_Algorithms.Sorting.bubble_sort import bubble_sort
from CORE_Algorithms.Searching.common import \
    Searchable, \
    Criteria, \
    MatchFunction, \
    CompareFunction, \
    NO_MATCH


def binary_search(input_list: List[Searchable],
                  criteria: Criteria,
                  match: MatchFunction,
                  compare: CompareFunction) -> Optional[Searchable]:
    """
    Searches through a list by sorting the list,
    then dividing it in half each time until a match found
    """
    # Create a list of tuples that preserve the original index of the value with the value itself
    tuple_list: List[Tuple[int, Searchable]] = [(idx, item) for idx, item in enumerate(input_list)]
    sorted_list: List[Tuple[int, Searchable]] = bubble_sort(tuple_list, lambda x, y: compare(x[1], y[1]))

    # Calculate initial values of lowest/highest pointers to encapsulate whole list
    lowest_ptr: int = 0
    highest_ptr: int = len(sorted_list) - 1

    while True:
        # Calculate new middle and make the comparison
        middle_ptr: int = floor((lowest_ptr + highest_ptr) / 2)
        comparison: int = match(criteria, sorted_list[middle_ptr][1])

        if comparison == 0:
            # Item found, return the first item in the tuple (the index in the original list)
            return sorted_list[middle_ptr][0]
        elif lowest_ptr == highest_ptr:
            # This is the exit condition
            break
        elif comparison == 1:
            # If the item is larger than the middle, but we are actually at the upper end...it aint there
            if middle_ptr == 0:
                return NO_MATCH
            highest_ptr = middle_ptr - 1
        else:  # Comparison == -1
            # If the item is smaller than the middle, but we are actually at the lower end...it aint there
            if middle_ptr == len(input_list) - 1:
                return NO_MATCH
            lowest_ptr = middle_ptr + 1

    return NO_MATCH
