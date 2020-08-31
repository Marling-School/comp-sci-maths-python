import unittest
from typing import List, Optional
from Algorithms.Searching.linear_search import linear_search
from Algorithms.Searching.binary_search import binary_search
from Algorithms.Searching.binary_tree_search import binary_tree_search
from Algorithms.Searching.common import MatchFunction, SearchFunction, NO_MATCH
from Algorithms.Sorting.common import primitive_compare
from Algorithms.Sorting.Person import Person, compare_name, compare_age

# Match Functions for Person objects and criteria
match_name: MatchFunction = lambda criteria, item: primitive_compare(criteria, item.get_name())
match_age: MatchFunction = lambda criteria, item: primitive_compare(criteria, item.get_age())


class TestSearchFunctions(unittest.TestCase):
    __search_functions: List[SearchFunction] = [linear_search, binary_search, binary_tree_search]

    def test_numbers(self):
        for search in self.__search_functions:
            # Create data to search through
            my_list: List[int] = [4, 5, 3, 1, 9, 8]

            # Run a search that should find a match
            my_match: int = search(my_list, 3, primitive_compare, primitive_compare)

            # Run a search that will not find a match
            my_non_match: int = search(my_list, 45, primitive_compare, primitive_compare)

            # Print stuff to show what everything looks like
            print("Integers: {}".format(search.__name__))
            print("Input: {}".format(my_list))
            print("Criteria: {} -> Match: {}".format(3, my_match))
            print("Criteria: {} -> Non-Match: {}".format(45, my_non_match))

            # Check the responses were as expected
            self.assertEqual(2, my_match)
            self.assertEqual(NO_MATCH, my_non_match)

    def test_string(self):
        for search in self.__search_functions:
            # Create data to search through
            my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]

            # Run a search that should find a match
            my_match: int = search(my_list, "Echo", primitive_compare, primitive_compare)

            # Run a search that will not find a match
            my_non_match: int = search(my_list, "X-Ray", primitive_compare, primitive_compare)

            # Print stuff to show what everything looks like
            print("Strings: {}".format(search.__name__))
            print("Input: {}".format(my_list))
            print("Criteria: {} -> Match: {}".format("Echo", my_match))
            print("Criteria: {} -> Non-Match:{}".format("X-Ray", my_non_match))

            # Check the responses were as expected
            self.assertEqual(4, my_match)
            self.assertEqual(NO_MATCH, my_non_match)

    def test_objects(self):
        for search in self.__search_functions:
            # Create data to search through
            my_list: List[Person] = [
                Person("Frodo", 55),
                Person("Sam", 35),
                Person("Bilbo", 111),
                Person("Sauron", 3000),
                Person("Gollum", 500)
            ]

            # Run searches that should find a matches
            by_name: int = search(my_list, "Frodo", match_name, compare_name)
            by_age: int = search(my_list, 3000, match_age, compare_age)

            # Run a search that will not find a match
            my_non_match: int = search(my_list, "Aragorn", match_name, compare_name)

            # Print stuff to show what everything looks like
            print("Objects: {}".format(search.__name__))
            print("Input: {}".format(my_list))
            print("By Name: Criteria: {} -> {}".format("Frodo", by_name))
            print("By Age: Criteria: {} -> {}".format(3000, by_age))
            print("Non-Match: Criteria: {} -> {}".format("Aragorn", my_non_match))

            # Check the responses were as expected
            self.assertEqual(0, by_name)
            self.assertEqual(3, by_age)
            self.assertEqual(NO_MATCH, my_non_match)

