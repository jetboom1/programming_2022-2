class Rational:
    def __init__(self, nom, denom):
        self.nominator = nom
        self.denominator = denom
    def __str__(self):
        return f'{self.nominator}/{self.denominator}'
    def __add__(self, other):
        if isinstance(other, Rational):
            if self.denominator == other.denominator:
                return f'{self.nominator+other.nominator}/{self.denominator}'
            else:
                new_denominator = lcm(self.denominator, other.denominator)
                other_multiplyer = new_denominator/other.denominator
                self_multiplyer = new_denominator/self.denominator
                return Rational(int(self.nominator*self_multiplyer+other.nominator*other_multiplyer), int(new_denominator))
    def __sub__(self, other):
        if isinstance(other, Rational):
            if self.denominator == other.denominator:
                return f'{self.nominator-other.nominator}/{self.denominator}'
            else:
                new_denominator = lcm(self.denominator, other.denominator)
                other_multiplyer = new_denominator/other.denominator
                self_multiplyer = new_denominator/self.denominator
                return Rational(int(self.nominator*self_multiplyer-other.nominator*other_multiplyer), int(new_denominator))
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(int(self.nominator*other.nominator),int(self.denominator*other.denominator))
    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self * Rational(int(other.denominator), int(other.nominator))



def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def test_rational():
    print("Testing class Rational ...")
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert (type(rational1) == Rational)
    assert (isinstance(rational1, Rational))
    assert (str(rational1) == "1/4")

    # here you can add two numbers
    rational2 = Rational(2, 5)
    assert (str(rational1 + rational2) == "13/20")

    # here is a substraction
    assert (str(rational1 - rational2) == "-3/20")

    # multiplication
    assert (str(rational1 * rational2) == "2/20")

    # division
    assert (str(rational1 / rational2) == "5/8")

    assert (type(rational1 + rational2) == Rational)
    assert (type(rational1 - rational2) == Rational)
    assert (type(rational1 * rational2) == Rational)
    assert (type(rational1 / rational2) == Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()