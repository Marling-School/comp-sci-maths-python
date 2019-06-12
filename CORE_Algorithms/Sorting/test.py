import unittest
from typing import List, Optional
from random import randint
from CORE_Algorithms.Sorting.bubble_sort import bubble_sort


class Person:
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


class TestBubbleSort(unittest.TestCase):
    def test_numbers(self):
        my_list: List[int] = [4, 5, 3, 1, 9, 8]
        my_sorted_list: List[int] = bubble_sort(my_list)
        my_reversed_list: List[int] = bubble_sort(my_list, lambda x, y: x < y)

        print("Integers\nInput: {}\nSorted: {}\nReversed: {}".format(
            my_list, my_sorted_list, my_reversed_list))
        self.assertEqual([1, 3, 4, 5, 8, 9], my_sorted_list)
        self.assertEqual([9, 8, 5, 4, 3, 1], my_reversed_list)

    def test_string(self):
        my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]
        my_sorted_list: List[str] = bubble_sort(my_list)
        my_reversed_list: List[str] = bubble_sort(my_list, lambda x, y: x < y)
        print("Strings\nInput: {}\nSorted: {}\nReversed: {}".format(
            my_list, my_sorted_list, my_reversed_list))
        self.assertEqual(
            ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Sierra"],
            my_sorted_list)
        self.assertEqual(
            ["Sierra", "Foxtrot", "Echo", "Delta", "Charlie", "Bravo", "Alpha"],
            my_reversed_list)

    def test_random(self):
        my_list: List[int] = [randint(0, 100) for i in range(100)]
        my_sorted_list: List[int] = bubble_sort(my_list)

        print("Random Numbers\nInput: {}\nSorted: {}".format(
            my_list, my_sorted_list))

        last: Optional[int] = None
        num_checks: int = 0
        for s in my_sorted_list:
            if last is not None:
                num_checks += 1
                self.assertTrue(last <= s)
            last = s
        self.assertEqual(num_checks, len(my_list) - 1)

    def test_objects(self):
        my_list: List[Person] = [
            Person("Frodo", 55),
            Person("Sam", 35),
            Person("Bilbo", 111),
            Person("Sauron", 3000),
            Person("Gollum", 500)
        ]
        by_name: List[Person] = bubble_sort(my_list, lambda x, y: x.get_name() > y.get_name())
        by_age: List[Person] = bubble_sort(my_list, lambda x, y: x.get_age() > y.get_age())

        by_name_names = [x.get_name() for x in by_name]
        by_age_names = [x.get_name() for x in by_age]

        print("Objects\nInput: {}\nBy Name: {}\nBy Age: {}".format(
            my_list, by_name, by_age))
        self.assertEqual(["Bilbo", "Frodo", "Gollum", "Sam", "Sauron"], by_name_names)
        self.assertEqual(["Sam", "Frodo", "Bilbo", "Gollum", "Sauron"], by_age_names)
