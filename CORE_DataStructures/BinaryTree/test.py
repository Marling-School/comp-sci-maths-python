import unittest
from CORE_DataStructures.BinaryTree.BinaryTree \
    import TraverseInOrder, TraversePostOrder, TraversePreOrder, BinaryTree


def str_is_to_left(a: str, b: str) -> bool:
    return a < b


class TestStringMethods(unittest.TestCase):

    def test_adj_list_graph(self):
        my_tree: BinaryTree[str] = BinaryTree(str_is_to_left)

        my_tree.add('B')
        my_tree.add('A')
        my_tree.add('D')
        my_tree.add('E')
        my_tree.add('C')
        my_tree.add('F')

        print("My Binary Tree:{}".format(my_tree))

        for t in [TraversePreOrder, TraverseInOrder, TraversePostOrder]:
            traverse: t[str] = t()
            print("Traversing {}".format(traverse.get_name()))
            traverse.traverse(my_tree, lambda x: print(x, end=", "))
            print("")



