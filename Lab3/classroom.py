'''classroom'''
# pylint: disable=C0103
# pylint: disable=W0611
class Classroom:
    """
    represents classroom
    >>> Classroom('080', 80, ['PC', 'projector', 'mic']).capacity
    80
    """
    def __init__(self, number, capacity, equipment):
        '''init'''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def __str__(self):
        '''print'''
        return f'Classroom {self.number} has a capacity of {self.capacity} persons and has the ' \
               f'following equipment: {", ".join(self.equipment)}.'
    def is_larger(self, classroom):
        '''is_larger'''
        if classroom.capacity < self.capacity:
            return True
        return False
    def equipment_differences(self, classroom):
        '''equipment_differences'''
        return list(set(self.equipment).difference(set(classroom.equipment)))
    def __repr__(self):
        '''repr'''
        '''Classroom('016', 80, ['PC', 'projector', 'mic'])'''
        return f"Classroom('{self.number}', {self.capacity}, {self.equipment})"

obj = Classroom('080', 80, ['PC', 'projector', 'mic'])
obj1 = Classroom('080', 80, ['PC', 'difference', 'ginger'])
print(obj.equipment_differences(obj1))
print(obj)