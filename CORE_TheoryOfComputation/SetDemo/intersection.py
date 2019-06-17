from typing import Set
from CORE_TheoryOfComputation.SetDemo.capture_csv import capture_string_csv

first: Set[str] = capture_string_csv('Please type the first list')
second: Set[str] = capture_string_csv('Please type the second subset')

print("Intersection of {} and {}: {}".format(
    first,
    second,
    first.intersection(second)
))
