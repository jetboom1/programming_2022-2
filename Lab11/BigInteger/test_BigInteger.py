import unittest
from bigInteger import BigInteger


class test_BigInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.big_int = BigInteger('123456789')
        self.big_int2 = BigInteger('987654321')
        self.big_int3 = BigInteger('0')
        self.big_int4 = BigInteger('-123456789')
        self.big_int5 = BigInteger('-987654321')
        self.big_int6 = BigInteger('-0')
        self.big_int7 = BigInteger('-98765431')
        self.big_int8 = BigInteger('98765431')

    def test_add(self):
        self.assertEqual(self.big_int + self.big_int2, BigInteger('1111111110'))
        self.assertEqual((self.big_int + self.big_int3), BigInteger('123456789'))
        self.assertEqual((self.big_int + self.big_int4), BigInteger('0'))
        self.assertEqual((self.big_int + self.big_int5), BigInteger('-864197532'))
        self.assertEqual(self.big_int + self.big_int6, BigInteger('-123456789'))
        self.assertEqual(self.big_int + self.big_int7, BigInteger('-24691358'))

    def test_sub(self):
        self.assertEqual(self.big_int - self.big_int2, BigInteger('-864197532'))
        self.assertEqual((self.big_int - self.big_int3), BigInteger('123456789'))
        self.assertEqual((self.big_int - self.big_int4), BigInteger('246913578'))
        self.assertEqual((self.big_int - self.big_int5), BigInteger('1111111110'))
        self.assertEqual(self.big_int - self.big_int6, BigInteger('123456789'))
        self.assertEqual(self.big_int - self.big_int8, BigInteger('24691358'))
