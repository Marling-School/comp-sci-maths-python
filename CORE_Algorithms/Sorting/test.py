import unittest
from typing import List, Optional, Callable, TypeVar
from random import randint
from CORE_Algorithms.Sorting.bubble_sort import bubble_sort
from CORE_Algorithms.Sorting.merge_sort import merge_sort


class Person:
    """"
    This class is used to test that custom comparators work with sorting objects
    """

    __name: str
    __age: int

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __repr__(self):
        return "{}: {}".format(self.__name, self.__age)

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


T = TypeVar('T')

# This is the standard form for sort functions
SortFunction = Callable[[List[T], Callable[[T, T], bool]], List[T]]
CompareFunction = Callable[[T, T], bool]

in_order: CompareFunction = lambda x, y: x > y
reverse_order: CompareFunction = lambda x, y: x < y
name_order: CompareFunction[Person] = lambda x, y: x.get_name() > y.get_name()
age_order: CompareFunction[Person] = lambda x, y: x.get_age() > y.get_age()


class TestSort:
    """"
    General test class, it needs to be given the sort function and the test case
    so that it can call sorts and make assertions.
    """
    __test: unittest.TestCase = None
    __sort_function: SortFunction = None

    def set_test(self, test: unittest.TestCase, sort_function: SortFunction):
        self.__sort_function = sort_function
        self.__test = test

    def test_numbers(self):
        my_list: List[int] = [4, 5, 3, 1, 9, 8]
        my_sorted_list: List[int] = self.__sort_function(my_list, in_order)
        my_reversed_list: List[int] = self.__sort_function(my_list, reverse_order)

        print("Integers\nInput: {}\nSorted: {}\nReversed: {}".format(
            my_list, my_sorted_list, my_reversed_list))
        self.__test.assertEqual([1, 3, 4, 5, 8, 9], my_sorted_list)
        self.__test.assertEqual([9, 8, 5, 4, 3, 1], my_reversed_list)

    def test_string(self):
        my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]
        my_sorted_list: List[str] = self.__sort_function(my_list, in_order)
        my_reversed_list: List[str] = self.__sort_function(my_list, reverse_order)
        print("Strings\nInput: {}\nSorted: {}\nReversed: {}".format(
            my_list, my_sorted_list, my_reversed_list))
        self.__test.assertEqual(
            ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Sierra"],
            my_sorted_list)
        self.__test.assertEqual(
            ["Sierra", "Foxtrot", "Echo", "Delta", "Charlie", "Bravo", "Alpha"],
            my_reversed_list)

    def test_random(self):
        my_list: List[int] = [randint(0, 100) for i in range(100)]
        my_sorted_list: List[int] = self.__sort_function(my_list, in_order)

        print("Random Numbers\nInput: {}\nSorted: {}".format(
            my_list, my_sorted_list))

        last: Optional[int] = None
        num_checks: int = 0
        for s in my_sorted_list:
            if last is not None:
                num_checks += 1
                self.__test.assertTrue(last <= s)
            last = s
        self.__test.assertEqual(num_checks, len(my_list) - 1)

    def test_objects(self):
        my_list: List[Person] = [
            Person("Frodo", 55),
            Person("Sam", 35),
            Person("Bilbo", 111),
            Person("Sauron", 3000),
            Person("Gollum", 500)
        ]
        by_name: List[Person] = self.__sort_function(my_list, name_order)
        by_age: List[Person] = self.__sort_function(my_list, age_order)

        by_name_names = [x.get_name() for x in by_name]
        by_age_names = [x.get_name() for x in by_age]

        print("Objects\nInput: {}\nBy Name: {}\nBy Age: {}".format(
            my_list, by_name, by_age))
        self.__test.assertEqual(["Bilbo", "Frodo", "Gollum", "Sam", "Sauron"], by_name_names)
        self.__test.assertEqual(["Sam", "Frodo", "Bilbo", "Gollum", "Sauron"], by_age_names)


class TestBubbleSort(TestSort, unittest.TestCase):

    def setUp(self) -> None:
        print("Testing Bubble Sort")
        super().set_test(self, bubble_sort)

    def tearDown(self) -> None:
        print("DONE Testing Bubble Sort")


class TestMergeSort(TestSort, unittest.TestCase):

    def setUp(self) -> None:
        print("Testing Merge Sort")
        super().set_test(self, merge_sort)

    def tearDown(self) -> None:
        print("DONE Testing Merge Sort")
