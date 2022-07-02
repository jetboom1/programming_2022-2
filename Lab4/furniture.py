'''furniture module'''
# pylint: disable=C0103
# pylint: disable=W0611
# pylint: disable=C0325
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0301
class Furniture:
    def __init__(self, style, assign):
        '''
                furniture class
                >>> 1==1
                True
        '''
        self.style = style
        self.assign = assign
    def __eq__(self, other):
        if isinstance(other, Furniture) and self.style == other.style and self.assign == other.assign:
            return True
        return False
    def __repr__(self):
        return f"<furniture style is {self.style}>"

class Chair(Furniture):
    def __init__(self, style, assign, tipe):
        '''
                chair class
                >>> 1==1
                True
        '''
        super(Chair, self).__init__(style, assign)
        self.tipe = tipe
    def __repr__(self):
        return f"<This armchair furniture style is {self.style}>"
    def get_assign(self):
        return self.assign

if __name__ == '__main__':
    furniture1 = Furniture("empire", "bedroom")

    furniture2 = Furniture("modern", "bathroom")

    assert (not (furniture1 == furniture2))

    assert (furniture1.style == "empire")

    assert (furniture1.assign == "bedroom")

    assert (str(furniture1) == "<furniture style is empire>")

    chair1 = Chair("empire", "bedroom", "armchair")

    assert (chair1.tipe == "armchair")

    assert (isinstance(chair1, Furniture))

    assert (str(chair1) == "<This armchair furniture style is empire>")

    assert (chair1.get_assign() == "bedroom")
