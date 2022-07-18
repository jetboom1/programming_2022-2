# Implementation of the Polynomial ADT using a sorted linked list.
import copy


class Polynomial :
    # Create a new polynomial object.
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._poly_head = None
        else :
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    def __len__(self):
        count = 0
        probe = self._poly_head
        while probe is not None:
            count += 1
            probe = probe.next
        return count

    # Return the degree of the polynomial.
    def degree(self):
        if self._poly_head is None :
            return -1
        else:
            return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree > degree :
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree :
            return 0.0
        else:
            return cur_node.coefficient

    def __setitem__(self, key, value):
        if self._poly_head is None:
            self._poly_head = _PolyTermNode(key, value)
            self._poly_tail = self._poly_head
        else:
            probe = self._poly_head
            while probe is not None:
                if probe.degree == key:
                    probe.coefficient = value
                    return self
                probe = probe.next
            self._append_term(key, value)

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None :
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: newPoly = self + rhs_poly.
    def __add__(self, rhs_poly):
        assert isinstance(rhs_poly, Polynomial), "Only polynomials can be added."
        new_poly = copy.deepcopy(self)
        probe2 = rhs_poly._poly_head
        while probe2 is not None:
            probe2_added = False
            probe = self._poly_head
            while probe is not None:
                if probe.degree == probe2.degree:
                    new_poly[probe.degree] = probe.coefficient + probe2.coefficient
                    probe2_added = True
                    probe = probe.next
                else:
                    probe = probe.next
            if not probe2_added:
                new_poly._append_term_sorted(probe2.degree, probe2.coefficient)
            probe2 = probe2.next
        return new_poly

    # Polynomial subtraction: newPoly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        assert isinstance(rhs_poly, Polynomial), "Only polynomials can be added."
        new_poly = copy.deepcopy(self)
        probe2 = rhs_poly._poly_head
        while probe2 is not None:
            probe2_added = False
            probe = self._poly_head
            while probe is not None:
                if probe.degree == probe2.degree:
                    new_poly[probe.degree] = probe.coefficient - probe2.coefficient
                    probe2_added = True
                    probe = probe.next
                else:
                    probe = probe.next
            if not probe2_added:
                new_poly._append_term_sorted(probe2.degree, -1 * probe2.coefficient)
            probe2 = probe2.next
        return new_poly

    # Polynomial multiplication: newPoly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        assert isinstance(rhs_poly, Polynomial), "Only polynomials can be multiplied."
        middle_poly = None
        probe1 = self._poly_head
        while probe1 is not None:
            probe2 = rhs_poly._poly_head
            while probe2 is not None:
                if not middle_poly:
                    middle_poly = Polynomial(probe1.degree + probe2.degree, probe1.coefficient * probe2.coefficient)
                else:
                    middle_poly._append_term_sorted(probe1.degree + probe2.degree, probe1.coefficient * probe2.coefficient)
                probe2 = probe2.next
            probe1 = probe1.next
        return middle_poly

    def simple_add(self, rhs_poly):
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly._append_term(i, value)
            i += 1
        return new_poly
    
    # Helper method for appending terms to the polynomial.
    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_term =_PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term 
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def _append_term_sorted(self, degree, coefficient):
        if coefficient != 0.0:
            new_term =_PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                probe = self._poly_head
                while probe is not None:
                    if probe.degree > degree and probe.next and probe.next.degree < degree: #probe.degree - degree == 1:
                        new_term.next = probe.next
                        probe.next = new_term
                        return self
                    elif probe.degree == degree:
                        probe.coefficient += coefficient
                        return self
                    probe = probe.next
                self._poly_tail.next = new_term
                self._poly_tail = new_term
                return self

    def __repr__(self):
        probe = self._poly_head
        res = ''
        while probe is not None:
            if res:
                if probe.coefficient > 0:
                    res += ' + '
                else:
                    res += ' - '
            if probe.degree == 0:
                res += str(probe.coefficient)
            elif probe.coefficient < 0:
                res += str(-probe.coefficient) + 'x^' + str(probe.degree)
            elif probe.coefficient > 0:
                res += str(probe.coefficient)+ 'x^' + str(probe.degree)
            probe = probe.next
        return res

    
# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
