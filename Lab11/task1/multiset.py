from node import *

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        '''removes all elements and returns the list of item of removed elements'''
        probe = self._head
        lst = []
        while probe is not None:
            lst.append(probe.item)
            self.delete(probe.item)
            probe = probe.next
        return lst

    def split_half(self):
        '''splits the multiset into two multisets with equal number of elements. If total number of elements is odd,
        the first multiset will have one more element than the second'''
        probe = self._head
        length = 0
        while probe is not None:
            length += 1
            probe = probe.next
        if length % 2 == 0:
            first_half = Multiset()
            second_half = Multiset()
            probe = self._head
            for i in range(length // 2):
                first_half.add(probe.item)
                probe = probe.next
            for i in range(length // 2):
                second_half.add(probe.item)
                probe = probe.next
            return first_half, second_half
        else:
            first_half = Multiset()
            second_half = Multiset()
            probe = self._head
            for i in range(length // 2 + 1):
                first_half.add(probe.item)
                probe = probe.next
            for i in range(length // 2):
                second_half.add(probe.item)
                probe = probe.next
            return first_half, second_half

    def extend(self, multiset1):
        '''extends the multiset with the elements of the multiset1'''
        assert isinstance(multiset1, Multiset), 'Given multiset is not a Multiset instance'
        probe = multiset1._head
        lst = []
        while probe is not None:
            lst.append(probe.item)
            probe = probe.next
        for i in lst[::-1]:
            self.add(i)
        return self


if __name__ == '__main__':
    multiset_1 = Multiset()
    multiset_2 = Multiset()
    multiset_1.add('p')
    multiset_1.add('y')
    multiset_1.add('t')
    multiset_2.add('h')
    multiset_2.add('o')
    multiset_2.add('n')
    assert multiset_1.extend(multiset_2).remove_all() == ['n', 'o', 'h', 't', 'y', 'p']
    m3 = Multiset()
    m4 = Multiset()
    m3.add('a')
    m3.add('b')
    m4.add('c')
    m4.add('d')
    assert m3.extend(m4).split_half()[0].remove_all() == ['c', 'd']