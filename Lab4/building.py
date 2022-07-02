'''building'''
# pylint: disable=C0103
# pylint: disable=W0611
# pylint: disable=C0325
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0301
class Building:
    def __init__(self, address):
        '''
        building class
        >>> 1==1
        True
        '''
        self.address = address


class House(Building):
    def __init__(self, address, flats):
        '''
        house class
        >>> 1==1
        True
        '''
        super().__init__(address)
        self.flats = flats

class AcademicBuilding(Building):
    """represents academic building
    >>> 1==1
    True
    """
    def __init__(self, address, classrooms):
        '''init'''
        super(AcademicBuilding, self).__init__(address)
        self.classrooms = classrooms
    def total_equipment(self):
        '''total equipment'''
        all_equip = []
        res = []
        for room in self.classrooms:
            for item in room.equipment:
                all_equip.append(item)
        for item in all_equip:
            item_count = (item, all_equip.count(item))
            res.append(item_count)
        print(list(set(res)))
        return list(set(res))
    def __str__(self):
        '''print'''
        string = f'{self.address}\n'
        for room in self.classrooms:
            string += str(room)+'\n'
        return string[:-1]
    