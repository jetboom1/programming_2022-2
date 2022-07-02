"""points module"""
# pylint: disable=C0301
# pylint: disable=C0116
# pylint: disable=C0103
import math
class Point:
    """
    point class
    >>> print(Point(3,4))
    Point in two-dimensional space with coordinates (3, 4)
    """
    def __init__(self, x, y):
        '''documentation'''
        self.x = x
        self.y = y
    def vector_length(self):
        '''
        vector length
        :return: float
        >>> Point(3, 4).vector_length()
        5.0
        '''
        length = math.sqrt(self.x**2+self.y**2)
        return round(length,2)
    def __str__(self):
        '''to be able to print things'''
        return 'Point in two-dimensional space with coordinates ({0}, {1})'.format(self.x,self.y)
    def __repr__(self):
        '''to represent it right'''
        return f'Point(x={self.x}, y={self.y})'
    def __eq__(self, other):
        '''to make some things equal and some things not'''
        if isinstance(other, Point) and self.x == other.x and self.y == other.y:
            return True
        elif isinstance(other, Point) and self.x == other.x and self.y == other.y and other.z == 0:
            return True
        return False

class Point3D(Point):
    '''
    3D point class
    >>> print(Point3D(3,4,5))
    Point in three-dimensional space with coordinates (3, 4, 5)
    '''
    def __init__(self, x, y, z=0):
        '''documentation'''
        super(Point3D, self).__init__(x,y)
        self.z = z
    def __str__(self):
        '''to be able to print things'''
        return "Point in three-dimensional space with coordinates ({0}, {1}, {2})".format(self.x, self.y, self.z)
    def __repr__(self):
        '''to represent it right'''
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
    def __eq__(self, other):
        '''to make some things equal and some things not'''
        if isinstance(other, Point3D) and self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        elif isinstance(other, Point) and self.x == other.x and self.y == other.y and self.z == 0:
            return True
        return False
    def vector_length(self):
        '''
        vector length
        :return: float
        >>> Point3D(3, 4, 12).vector_length()
        13.0
        '''
        length = math.sqrt(self.x**2+self.y**2+self.z**2)
        return round(length,2)

if __name__ == '__main__':
    point1 = Point(17, 2)
    assert (point1.y, point1.x) == (2, 17)
    assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"

    point2 = Point3D(17, 4, 2)
    print(Point(3, 4))
    assert (point2.y, point2.z, point2.x) == (4, 2, 17)
    assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
    assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"

    assert Point(3, 4) == Point(3, 4)
    assert Point(3, 4) != Point(2, 3)

    assert Point(5, 4) == Point3D(5, 4, 0)
    assert Point3D(5, 4, 0) == Point(5, 4)

    assert Point(5, 4) != Point3D(5, 4, 1)
    assert Point3D(5, 4, 1) != Point(5, 4)

    assert Point3D(8, 7, 0) == Point3D(8, 7)

    assert Point(3, 4).vector_length() == 5
    assert Point(4, 5).vector_length() == 6.4
    assert Point(6, -12).vector_length() == 13.42
    assert Point(100, 0).vector_length() == 100

    assert Point3D(-6, -12, 0).vector_length() == 13.42, Point3D(-6, -12, 0).vector_length()
    assert Point3D(3, 4, 12).vector_length() == 13
    assert Point3D(-13, 14, -15).vector_length() == 24.29
