'''point'''
# pylint: disable=C0103
# pylint: disable=W0611
from math import cos, sin, radians

class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    >>> Point(1,1).x
    1
    """

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point.
        The x and y coordinates can be specified.
        If they are not, the point defaults to the origin.'''
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def rotate(self, beta, other_point):
        "Rotate point around other point"
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.x
        ypoint3 = ypoint3 + other_point.y
        return self.move(xpoint3, ypoint3)
