"""
 a class to hold coordinate information
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Coordinate:
    """
    A class to hold coordinate information
    Attributes:
        x: the x coordinate
        y: the y coordinate
    """

    x: float
    y: float

    def __sub__(self, other: Coordinate):
        """
        Subtract a coordinate from this coordinate
        :param other: the coordinate to subtract
        :return:
        """
        return Coordinate(self.x - other.x, self.y - other.y)

    def __add__(self, other: Coordinate):
        """
        Add a coordinate to this coordinate
        :param other: the coordinate to add
        :return:
        """
        return Coordinate(self.x + other.x, self.y + other.y)

    def x_delta(self, other: Coordinate) -> float:
        """
        Calculate the x delta between this coordinate and another coordinate
        :param other: the other coordinate
        :return: the x delta between the two coordinates
        """
        return self.x - other.x

    def y_delta(self, other: Coordinate) -> float:
        """
        Calculate the y delta between this coordinate and another coordinate
        :param other: the other coordinate
        :return: the y delta between the two coordinates
        """
        return self.y - other.y

    def distance(self, other: Coordinate) -> float:
        """
        Calculate the distance between this coordinate and another coordinate
        :param other: the other coordinate
        :return: the distance between the two coordinates
        """
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        )
