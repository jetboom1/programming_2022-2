import unittest
from validator import Validator
import coverage

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid = Validator()
    def test_validate_name_surname(self):
        self.assertEqual(self.valid.validate_name_surname("Elvis Presley"), True)
        self.assertEqual(self.valid.validate_name_surname("ElvisPresley"), False)
        self.assertEqual(self.valid.validate_name_surname("Elvis Presley forever"), False)

        # should be only first uppercase letter in name and surname
        self.assertEqual(self.valid.validate_name_surname("elvis Presley"), False)
        self.assertEqual(self.valid.validate_name_surname("Elvis presley"), False)
        self.assertEqual(self.valid.validate_name_surname("Elvis PResley"), False)

        # size of both name and surname shoulb be between 2 and 30
        self.assertEqual(self.valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"), False)
        self.assertEqual(self.valid.validate_name_surname("Elvis P"), False)

        # no digits or punctuation in name or surname
        self.assertEqual(self.valid.validate_name_surname("Elvis P,resley"), False)
        self.assertEqual(self.valid.validate_name_surname("El1vis Presley"), False)
    def test_age(self):
        # self.valid age id digit berween 16 and 99
        self.assertEqual(self.valid.validate_age("20"), True)
        self.assertEqual(self.valid.validate_age("7"), False)
        self.assertEqual(self.valid.validate_age("100"), False)
        self.assertEqual(self.valid.validate_age("20."), False)
        self.assertEqual(self.valid.validate_age("20a"), False)
    def test_country(self):
        # self.valid country - between 2 and 10 chars, first letter should be uppercase, can`t contain numbers
        self.assertEqual(self.valid.validate_country("Ukraine"), True)
        self.assertEqual(self.valid.validate_country("U"), False)
        self.assertEqual(self.valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU"), False)
        self.assertEqual(self.valid.validate_country("Ukraine1"), False)
        self.assertEqual(self.valid.validate_country("ukraine"), False)
        self.assertEqual(self.valid.validate_country("USA"), True)
        self.assertEqual(self.valid.validate_country("USA1"), False)
    def test_region(self):
        # self.valid region - the same as country, but can contain numbers
        self.assertEqual(self.valid.validate_region("Lviv"), True)
        self.assertEqual(self.valid.validate_region("Lviv1"), True)
        self.assertEqual(self.valid.validate_region("L"), False)
        self.assertEqual(self.valid.validate_region("lviv"), False)
    def test_living_place(self):
        # living place - should be in format: "Koselnytska st. 2a"
        # name of street - between 3 and 20 chars, first character uppercase, no digits in it
        # type of street - should be "st.", "av.", "prosp." or "rd."
        # number of building - exactly 2 symbols, first should be number, second can be number or small letter
        self.assertEqual(self.valid.validate_living_place("Koselnytska st. 2a"), True)
        self.assertEqual(self.valid.validate_living_place("koselnytska st. 2a"), False)
        self.assertEqual(self.valid.validate_living_place("Koselnytska provulok 2a"), False)
        self.assertEqual(self.valid.validate_living_place("Koselnytska st. 2"), False)
        self.assertEqual(self.valid.validate_living_place("Koselnytska st. a2"), False)
        self.assertEqual(self.valid.validate_living_place("Koselnytska st. 22"), True)
    def test_index(self):
        # self.valid index - exactly 5 digits
        self.assertEqual(self.valid.validate_index("79000"), True)
        self.assertEqual(self.valid.validate_index("7900"), False)
        self.assertEqual(self.valid.validate_index("790000"), False)
        self.assertEqual(self.valid.validate_index("7900q"), False)
        self.assertEqual(self.valid.validate_index("790 00"), False)
    def test_phone(self):
        # valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
        # starts wit "+" and has from 9 to 12 numbers
        self.assertEqual(self.valid.validate_phone("+380951234567"), True)
        self.assertEqual(self.valid.validate_phone("+38 (095) 123-45-67"), True)
        self.assertEqual(self.valid.validate_phone("38 (095) 123-45-67"), False)
        self.assertEqual(self.valid.validate_phone("380951234567"), False)
        self.assertEqual(self.valid.validate_phone("-380951234567"), False)
        self.assertEqual(self.valid.validate_phone("+3810951234567"), False)
        self.assertEqual(self.valid.validate_phone("+20951234567"), True)
    def test_email(self):
        # self.valid email should be in format "username@domain.type"
        # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~", dots (provided that it, not the first or last
        # character and provided also that it does not appear consecutively), at least 1, at most 64
        # domain - only lowercase letters, at least 1, at most 255, but
        # be careful - can be also "." - for example @ucu.edu.ua
        # type : "com", "org", "edu", "gov", "net", "ua",....
        self.assertEqual(self.valid.validate_email("username@domain.com"), True)
        self.assertEqual(self.valid.validate_email("username+usersurname@domain.com"), True)
        self.assertEqual(self.valid.validate_email("username@ucu.edu.ua"), True)
        self.assertEqual(self.valid.validate_email("usernamedomain.com"), False)
        self.assertEqual(self.valid.validate_email("username@domaincom"), False)
        self.assertEqual(self.valid.validate_email("username@domain.aaa"), False)
        self.assertEqual(self.valid.validate_email("username@aaa"), False)
        self.assertEqual(self.valid.validate_email("@domain.com"), False)
    def test_id(self):
        # self.valid id - exactly 6 digits, but should contain exactly one zero - at any position
        self.assertEqual(self.valid.validate_id("123450"), True)
        self.assertEqual(self.valid.validate_id("011111"), True)
        self.assertEqual(self.valid.validate_id("123456"), False)
        self.assertEqual(self.valid.validate_id("123006"), False)
        self.assertEqual(self.valid.validate_id("1230916"), False)
        self.assertEqual(self.valid.validate_id("12306"), False)
    def test_data(self):
        # data - string in format "name_surname,age,country,region,living_place,index,phone,email,id"
        # can also be whitespaces between sections and allowed separator ші ";"
        # all previous criteria are self.valid
        self.assertEqual(self.valid.validate(
            "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"), True)
        self.assertEqual(self.valid.validate(
            "Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450"), True)
        self.assertEqual(self.valid.validate(
            "Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450"), True)
        self.assertEqual(self.valid.validate(
            "Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"), True)

if __name__ == '__main__':
    unittest.main()