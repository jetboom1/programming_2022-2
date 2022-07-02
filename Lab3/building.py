'''building'''
# pylint: disable=C0103
# pylint: disable=W0611
import classroom
class AcademicBuilding:
    """represents academic building
    >>> 1==1
    True
    """
    def __init__(self, address, classrooms):
        '''init'''
        self.address = address
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

if __name__ == '__main__':
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms = [classroom_016, classroom_007, classroom_008]
    building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    building.total_equipment()
    print(building.__str__())
