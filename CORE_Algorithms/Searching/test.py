import unittest
from typing import List, Optional
from CORE_Algorithms.Searching.linear_search import linear_search
from CORE_Algorithms.Searching.binary_search import binary_search
from CORE_Algorithms.Searching.binary_tree_search import binary_tree_search
from CORE_Algorithms.Searching.common import MatchFunction, SearchFunction
from CORE_Algorithms.Sorting.Person import Person, compare_name, compare_age

# Standard Sort Functions
primitive_match: MatchFunction = lambda x, y: x == y

# Sort Functions for Person objects
match_name: SearchFunction = lambda criteria, item: item.get_name() == criteria
match_age: SearchFunction = lambda criteria, item: item.get_age() == criteria


class TestSortFunctions(unittest.TestCase):
    __search_functions: List[SearchFunction] = [linear_search, binary_search, binary_tree_search()]

    def test_numbers(self):
        for search in self.__search_functions:
            my_list: List[int] = [4, 5, 3, 1, 9, 8]
            my_match: Optional[int] = search(my_list, 3, primitive_match)
            my_non_match: Optional[int] = search(my_list, 45, primitive_match)
            print("Integers: {}\nInput: {}\nMatch\nNon-Match: {}".format(
                search.__name__, my_list, my_match, my_non_match))
            self.assertEqual(3, my_match)
            self.assertIsNone(my_non_match)

    def test_string(self):
        for search in self.__search_functions:
            my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]
            my_match: List[str] = search(my_list, "Delta", primitive_match)
            my_non_match: List[str] = search(my_list, "X-Ray", primitive_match)
            print("Strings: {}\nInput: {}\nMatch: {}\nNon-Mathch:{}".format(
                search.__name__, my_list, my_match, my_non_match))
            self.assertEqual("Delta", my_match)
            self.assertIsNone(my_non_match)

    def test_objects(self):
        for search in self.__search_functions:
            my_list: List[Person] = [
                Person("Frodo", 55),
                Person("Sam", 35),
                Person("Bilbo", 111),
                Person("Sauron", 3000),
                Person("Gollum", 500)
            ]
            by_name: Optional[Person] = search(my_list, 'Frodo', match_name)
            by_age: Optional[Person] = search(my_list, 3000, match_age)
            my_non_match: Optional[Person] = search(my_list, "Aragorn", match_name)

            print("Objects: {}\nInput: {}\nBy Name: {}\nBy Age: {}\nNon-Match: {}".format(
                search.__name__, my_list, by_name, by_age, my_non_match))
            self.assertEqual("Frodo", by_name.get_name())
            self.assertEqual("Sauron", by_age.get_name())
            self.assertIsNone(my_non_match)

