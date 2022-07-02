'''cats module'''
# pylint: disable=C0103
# pylint: disable=W0611
# pylint: disable=C0325
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=C0301
class Animal:
    def __init__(self, phylum, clas):
        '''
                animal class
                >>> 1==1
                True
            '''
        self.phylum = phylum
        self.clas = clas
    def __repr__(self):
        return f'<animal class is {self.clas}>'
    def __eq__(self, other):
        if isinstance(other, Animal) and self.phylum == other.phylum and self.clas == other.clas:
            return True
        return False
class Cat(Animal):
    '''
            cat class
            >>> 1==1
            True
    '''
    def __init__(self, phylum, clas, genus):
        super(Cat, self).__init__(phylum, clas)
        self.genus = genus
    def sound(self):
        return 'Meow'
    def __repr__(self):
        return f'<This {self.genus} animal class is {self.clas}>'

if __name__ == '__main__':
    animal1 = Animal("chordata", "mammalia")

    assert (animal1.phylum == "chordata")

    assert (animal1.clas == "mammalia")

    assert (str(animal1) == "<animal class is mammalia>")

    animal2 = Animal("chordata", "birds")

    assert (not (animal1 == animal2))

    cat1 = Cat("chordata", "mammalia", "felis")

    assert (cat1.sound() == "Meow")

    assert (cat1.genus == "felis")

    assert (isinstance(cat1, Animal))

    assert (str(cat1) == "<This felis animal class is mammalia>")