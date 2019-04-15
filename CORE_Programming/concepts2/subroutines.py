from math import sin, cos, pi


"""
This function accepts a magnitude and angle (in radians)
It returns a value (a Tuple containing x,y coordinates)
"""
def convertPolarToCartesian(magnitude: float, angle: float) -> (float, float):
    x: float = magnitude * sin(angle)
    y: float = magnitude * cos(angle)

    return x, y


"""
This is a procedure that prints a coordinate, it doesn't return anything
"""
def printCoordinate(name: str, coord: (float, float)):
    print("Coordinate {} is x: {:0.2f}, y: {:0.2f}".format(name, coord[0], coord[1]))


coord1: (float, float) = convertPolarToCartesian(50, pi / 4)
coord2: (float, float) = convertPolarToCartesian(100, 2 * pi / 3)

printCoordinate("First", coord1)
printCoordinate("Second", coord2)

