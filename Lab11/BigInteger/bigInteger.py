from node import TwoWayNode

VARIANT = 67 #['==', '!='] ['+', '-'] ['<<', '&']

class BigInteger():
    """
    A class for representing a BigInteger.
    """
    def __init__(self, value='.'):
        """
        Initialize a BigInteger with a string value.
        """
        self.value = value
        self.negative = False
        if value[0] == '-':
            self.negative = True
            self.value = value[1:]
        self.head = None
        self.tail = None
        self.length = 0
        if value != '.':
            self.__build_list()

    def __abs__(self):
        '''
        Return the absolute value of the BigInteger.
        '''
        if self.negative:
            self.negative = False
        return self

    def __eq__(self, other):
        """
        Return True if two BigIntegers are equal.
        """
        if self.length != other.length:
            return False
        for i in range(self.length-1, -1, -1):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other):
        """
        Return True if two BigIntegers are not equal.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Return True if the BigInteger is less than the other.
        """
        if self.negative != other.negative:
            return self.negative
        if self.length < other.length:
            return True
        if self.length > other.length:
            return False
        for i in range(self.length-1, -1, -1):
            if self[i] < other[i]:
                return True
            if self[i] > other[i]:
                return False
        return False

    def __gt__(self, other):
        """
        Return True if the BigInteger is greater than the other.
        """
        if self != other:
            return other < self
        return False

    def __build_list(self):
        """
        Build the Big Integer linked list from the string value.
        """
        for i in range(len(self.value)-1, -1, -1):
            if self.head is None:
                self.head = TwoWayNode(int(self.value[i]))
                self.tail = self.head
                self.length += 1
                continue
            self.tail.next = TwoWayNode(int(self.value[i]))
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            self.length += 1
        self.tail.next = None

    def __getitem__(self, item):
        """
        Return the item`s data at index.
        """
        if item < 0 or item >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for i in range(item):
            current = current.next
        return current.data

    def to_string(self):
        """
        Return the string representation of the BigInteger.
        """
        s = ''
        probe = self.tail
        if self.negative:
            s += '-'
        while probe is not None:
            s += str(probe.data)
            probe = probe.previous
        return s

    def __repr__(self):
        """
        Return the string representation of the BigInteger.
        """
        return self.to_string()

    def __add__(self, other):
        """
        Return the sum of two BigIntegers.
        """
        if self.negative == other.negative:
            res = self._simple_add(other)
        elif self.negative != other.negative and self > other:
            res = self._simple_sub(other)
        elif self.negative != other.negative and self < other:
            res = other._simple_sub(self)
        else:
            return BigInteger('0')
        return res



    def _simple_add(self, other):
        """simple adding two positive BigIntegers"""
        result = BigInteger()
        longer = self if self.length > other.length else other
        shorter = self if longer == other else other
        additional_one = 0
        for i in range(longer.length):
            num1 = longer[i]
            num2 = shorter[i] if i < shorter.length else 0
            to_be_added = num1 + num2 + additional_one
            if result.head is None:
                result.tail = result.head
                if to_be_added >= 10:
                    result.head = TwoWayNode(to_be_added - 10, result.tail)
                    additional_one = 1
                else:
                    result.head = TwoWayNode(to_be_added, result.tail)
                    additional_one = 0
                result.tail = result.head
            else:
                if to_be_added >= 10:
                    result.tail.next = TwoWayNode(to_be_added - 10, result.tail)
                    additional_one = 1
                else:
                    result.tail.next = TwoWayNode(to_be_added, result.tail)
                    additional_one = 0
                result.tail = result.tail.next
            result.length += 1
        if additional_one == 1:
            result.tail.next = TwoWayNode(1, result.tail)
            result.tail = result.tail.next
            result.length += 1
        return result

    def _simple_sub(self, other):
        """simple subtracting two positive BigIntegers"""
        result = BigInteger()
        longer = self if self.length > other.length else other
        if abs(other) > abs(self):
            result.negative = True
            bigger = other
            smaller = self
        else:
            bigger = self
            smaller = other
        additional_one = 0
        for i in range(longer.length):
            num1 = bigger[i] if i < self.length else 0
            num2 = smaller[i] if i < other.length else 0
            to_be_added = num1 - num2 - additional_one
            if result.head is None:
                result.tail = result.head
                if to_be_added < 0:
                    result.head = TwoWayNode(to_be_added + 10, result.tail)
                    additional_one = 1
                else:
                    result.head = TwoWayNode(to_be_added, result.tail)
                    additional_one = 0
                result.tail = result.head
            else:
                if to_be_added < 0:
                    result.tail.next = TwoWayNode(to_be_added + 10, result.tail)
                    additional_one = 1
                else:
                    result.tail.next = TwoWayNode(to_be_added, result.tail)
                    additional_one = 0
                result.tail = result.tail.next
            result.length += 1
        return result._delete_leading_zeros()

    def _delete_leading_zeros(self):
        '''
        Delete the leading zeros of the BigInteger.
        '''
        probe = self.tail
        while probe is not None and probe.data == 0:
            self.tail = probe.previous
            self.length -= 1
            probe = self.tail
        return self

    def __sub__(self, other):
        """
        Return the difference of two BigIntegers.
        """
        other.negative = not other.negative
        return self + other
