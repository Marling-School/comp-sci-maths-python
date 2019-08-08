from typing import List, TypeVar, Callable
from random import randint

T = TypeVar('T')


def get_sorting_algorithm(name: str) -> Callable[[T, T], bool]:
    """
    Retrieve a sorting algorithm from one of the named ones
    :param name:
    :return:
    """
    if name == "ascending":
        return lambda x, y: x < y
    elif name == "descending":
        return lambda x, y: x > y
    else:
        raise Exception(f"Unknown sorting algorithm: {name}")


def bubble_sort(items: List[T], in_right_order: Callable[[T, T], bool]) -> List[T]:
    """
    Sort a list of items, using a custom comparator
    :param items: The list to sort
    :param in_right_order: The function to check two items are in the right order
    :return:
    """
    output_items: List[T] = [x for x in items]
    for top in range(len(items), 1, -1):
        for current in range(0, top - 1):
            if not in_right_order(output_items[current], output_items[current + 1]):
                swap: T = output_items[current + 1]
                output_items[current + 1] = output_items[current]
                output_items[current] = swap
    return output_items


# Create a list of random numbers
my_list: List[int] = [randint(0, 100) for x in range(20)]

# Sort it using two different comparison functions
sort_asc = get_sorting_algorithm("ascending")
ascending_list: List[int] = bubble_sort(my_list, sort_asc)

sort_desc = get_sorting_algorithm("descending")
descending_list: List[int] = bubble_sort(my_list, sort_desc)

print(f"Raw: {my_list}")
print(f"Ascending: {ascending_list}")
print(f"Descending: {descending_list}")
