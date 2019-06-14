import unittest
from typing import List, Optional
from CORE_Algorithms.Searching.linear_search import linear_search
from CORE_Algorithms.Searching.binary_search import binary_search
from CORE_Algorithms.Searching.binary_tree_search import binary_tree_search
from CORE_Algorithms.Searching.common import MatchFunction, SearchFunction, NO_MATCH
from CORE_Algorithms.Sorting.common import primitive_compare
from CORE_Algorithms.Sorting.Person import Person, compare_name, compare_age

# Sort Functions for Person objects
match_name: MatchFunction = lambda criteria, item: primitive_compare(criteria, item.get_name())
match_age: MatchFunction = lambda criteria, item: primitive_compare(criteria, item.get_age())


class TestSearchFunctions(unittest.TestCase):
    __search_functions: List[SearchFunction] = [linear_search, binary_search, binary_tree_search]

    def test_numbers(self):
        for search in self.__search_functions:
            my_list: List[int] = [4, 5, 3, 1, 9, 8]
            my_match: int = search(my_list, 3, primitive_compare, primitive_compare)
            my_non_match: int = search(my_list, 45, primitive_compare, primitive_compare)
            print("Integers: {}\nInput: {}\nMatch: {}\nNon-Match: {}".format(
                search.__name__, my_list, my_match, my_non_match))
            self.assertEqual(2, my_match)
            self.assertEqual(NO_MATCH, my_non_match)

    def test_string(self):
        for search in self.__search_functions:
            my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]
            my_match: int = search(my_list, "Echo", primitive_compare, primitive_compare)
            my_non_match: int = search(my_list, "X-Ray", primitive_compare, primitive_compare)
            print("Strings: {}\nInput: {}\nMatch: {}\nNon-Match:{}".format(
                search.__name__, my_list, my_match, my_non_match))
            self.assertEqual(4, my_match)
            self.assertEqual(NO_MATCH, my_non_match)

    def test_objects(self):
        for search in self.__search_functions:
            my_list: List[Person] = [
                Person("Frodo", 55),
                Person("Sam", 35),
                Person("Bilbo", 111),
                Person("Sauron", 3000),
                Person("Gollum", 500)
            ]
            by_name: int = search(my_list, "Frodo", match_name, compare_name)
            by_age: int = search(my_list, 3000, match_age, compare_age)
            my_non_match: int = search(my_list, "Aragorn", match_name, compare_name)

            print("Objects: {}\nInput: {}\nBy Name: {}\nBy Age: {}\nNon-Match: {}".format(
                search.__name__, my_list, by_name, by_age, my_non_match))
            self.assertEqual(0, by_name)
            self.assertEqual(3, by_age)
            self.assertEqual(NO_MATCH, my_non_match)

