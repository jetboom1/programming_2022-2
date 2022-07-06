from arrays import Array

class AngleADT:
    """The abstract data type for representing an Martian-like type of messaging"""
    def __init__(self):
        self._single_angle = 360/16
        self._angle_array = None
        self._hex_dict = dict()
        self._fill_hex_dict()
    def encode_message(self, message):
        """Encodes the message into an angle array and returns the angle array. For the sake of the extended
        cyrillic support, the encoding is not ASCII, but Windows-1251"""
        encoded_message = message.encode('windows-1251')
        letters = ''         #letters is a combined string
                            # of all the hex values of the message
        for char in encoded_message:
            char_hex = hex(char)
            letters += str(char_hex)[2:]
        self._angle_array = Array(len(letters))
        index = 0
        prev_angle = 0
        for letter in letters:
            angle = self._single_angle * self._hex_dict[letter] - prev_angle
            if angle == 0:
                angle = 360
            self._angle_array.__setitem__(index, angle)
            index += 1
            prev_angle = self._single_angle * self._hex_dict[letter]
        return self._angle_array

    def print_array(self):
        '''Prints the angle array'''
        print('Angle Array: [', end='')
        for i in range(len(self._angle_array)):
            print(self._angle_array.__getitem__(i), end=' ')
        print(']')

    def __repr__(self):
        '''Returns a string representation of the angle array'''
        s = 'Angle Array: ['
        for i in range(len(self._angle_array)):
            s += str(self._angle_array.__getitem__(i)) + ' '
        s += ']'
        return s

    def _fill_hex_dict(self):
        '''Fills the hex dictionary with the hex values of the letters'''
        self._hex_dict['0'] = 0
        self._hex_dict['1'] = 1
        self._hex_dict['2'] = 2
        self._hex_dict['3'] = 3
        self._hex_dict['4'] = 4
        self._hex_dict['5'] = 5
        self._hex_dict['6'] = 6
        self._hex_dict['7'] = 7
        self._hex_dict['8'] = 8
        self._hex_dict['9'] = 9
        self._hex_dict['a'] = 10
        self._hex_dict['b'] = 11
        self._hex_dict['c'] = 12
        self._hex_dict['d'] = 13
        self._hex_dict['e'] = 14
        self._hex_dict['f'] = 15

if __name__ == '__main__':
    dt = AngleADT()
    dt.encode_message('hello')
    assert str(dt) == 'Angle Array: [135.0 45.0 -45.0 -22.5 22.5 135.0 -135.0 135.0 -135.0 202.5 ]'
    dt.encode_message('1 січня')
    assert str(dt) == 'Angle Array: [67.5 -45.0 22.5 -45.0 337.5 -315.0 225.0 -180.0 270.0 -180.0 157.5 -22.5 45.0 360 ]'