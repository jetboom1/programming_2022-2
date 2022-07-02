'''triangle'''
# pylint: disable=C0103
# pylint: disable=W0611
from math import sqrt
import point

class Triangle:
    """represents triangle
    >>> Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3)).is_triangle()
    True
    """
    def __init__(self, p1, p2, p3):
        '''init'''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p1p2 = sqrt((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2)
        self.p1p3 = sqrt((self.p3.x-self.p1.x)**2+(self.p3.y-self.p1.y)**2)
        self.p2p3 = sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
    def is_triangle(self):
        '''is triangle'''
        distances = [self.p1p2,self.p1p3,self.p2p3]
        max_dist = max(distances)
        distances.remove(max_dist)
        if distances[0]+distances[1] > max_dist:
            return True
        return False
    def perimeter(self):
        '''perimeter'''
        return self.p1p2+self.p1p3+self.p2p3
    def area(self):
        '''area'''
        s = self.perimeter()/2
        area = sqrt(s*(s-self.p1p2)*(s-self.p1p3)*(s-self.p2p3))
        return area

triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
print(triangle.is_triangle())
