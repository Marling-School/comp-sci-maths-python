from typing import Optional, List, Tuple
from CORE_Algorithms.Searching.common import \
    Searchable, \
    Criteria, \
    MatchFunction, \
    CompareFunction, \
    NO_MATCH
from CORE_Algorithms.TreeTraversal.BinaryTreeImpl import BinaryTree, BinaryTreeImpl


def binary_tree_search(input_list: List[Searchable],
                       criteria: Criteria,
                       match: MatchFunction,
                       compare: CompareFunction) -> Optional[Searchable]:
    """
    Searches through a list by putting all the items into a binary tree
    then navigating the tree until the item is found.
    """
    # Create a tree of tuples to preserve the index alongside the original value
    tree_node: BinaryTree[Tuple[int, Searchable]] = \
        BinaryTreeImpl[Tuple[int, Searchable]](lambda x, y: compare(x[1], y[1]))
    for index, item in enumerate(input_list):
        # noinspection PyTypeChecker
        tree_node.add((index, item))

    while tree_node is not None:
        comparison: int = match(criteria, tree_node.get_value()[1])
        if comparison == 0:
            return tree_node.get_value()[0]
        elif comparison == 1:
            tree_node = tree_node.get_left()
        else:
            tree_node = tree_node.get_right()

    return NO_MATCH
