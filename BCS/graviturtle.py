import logging
import threading
import math
import time
from turtle import Turtle
from typing import List, Tuple


def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper


def create_planet(color: str) -> Turtle:
    planet = Turtle(shape='circle')
    planet.color(color)
    planet.penup()
    return planet


class GraviTurtle:
    __relationships: List[Tuple[Turtle, Turtle, int, int]]

    def __init__(self):
        self.__relationships = []

    def setup_orbit(self, attractor: Turtle, satellite: Turtle, radius: int = 100, frequency: int = 1):
        self.__relationships.append((attractor, satellite, radius, frequency))

    def run(self):
        # main body
        logging.info("Starting Gravity")
        while True:
            now = time.time()
            for attractor, satellite, radius, frequency in self.__relationships:
                apos = attractor.pos()
                x = apos[0] + radius * math.sin(frequency * now)
                y = apos[1] + radius * math.cos(frequency * now)
                satellite.setposition(x, y)

