from __future__ import annotations
from typing import List


class Person:
    name: str
    age: int
    favourite_colour: str

    def __init__(self, name: str, age: int, favourite_colour: str):
        self.name = name
        self.age = age
        self.favourite_colour = favourite_colour

    def to_csv(self) -> str:
        return "{},{},{}".format(self.name, self.age, self.favourite_colour)

    @staticmethod
    def from_csv(csv: str) -> Person:
        parts: List[str] = csv.split(",")
        if len(parts) != 3:
            raise Exception("Incorrect number of parts")
        name: str = parts[0]
        age: int = int(parts[1])
        favourite_colour: str = parts[2]
        return Person(name, age, favourite_colour)