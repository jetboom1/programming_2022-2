import unittest
from flower import *
import coverage

class TestFlowers(unittest.TestCase):
    def setUp(self) -> None:
        self.flower_attributes = ['Custom', 'ultramarine', 15, 100]
        self.flower_attributes1 = [123, 'ultramarine', 15, 100]
        self.flower_attributes2 = ['Custom', 123, 15, 100]
        self.flower_attributes3 = ['Custom', 'ultramarine', '15', -100]
        self.flower_attributes4 = ['Custom', 'ultramarine', -15, '100']

        self.tulip_attributes = [15, 100]
        self.tulip_attributes1 = [15, '100']
        self.tulip_attributes2 = ['15', 100]

        self.rose_attributes = [15, 100]
        self.rose_attributes1 = [15, '100']
        self.rose_attributes2 = ['15', 100]

        self.chamomile_attributes = [15, 100]
        self.chamomile_attributes1 = [15, '100']
        self.chamomile_attributes2 = ['15', 100]

    def test_Flower(self):
        self.assertEqual(Flower(*self.flower_attributes).name, 'Custom')
        with self.assertRaises(AttributeError):
            Flower(*self.flower_attributes1)
        with self.assertRaises(AttributeError):
            Flower(*self.flower_attributes2)
        with self.assertRaises(AttributeError):
            Flower(*self.flower_attributes3)
        with self.assertRaises(AttributeError):
            Flower(*self.flower_attributes4)

    def test_Tulip(self):
        self.assertEqual(Tulip(*self.tulip_attributes).name, 'Tulip')
        with self.assertRaises(AttributeError):
            Tulip(*self.tulip_attributes1)
        with self.assertRaises(AttributeError):
            Tulip(*self.tulip_attributes2)

    def test_Chamomile(self):
        self.assertEqual(Chamomile(*self.chamomile_attributes).name, 'Chamomile')
        with self.assertRaises(AttributeError):
            Chamomile(*self.chamomile_attributes1)
        with self.assertRaises(AttributeError):
            Chamomile(*self.chamomile_attributes2)

    def test_Rose(self):
        self.assertEqual(Rose(*self.rose_attributes).name, 'Rose')
        with self.assertRaises(AttributeError):
            Rose(*self.rose_attributes1)
        with self.assertRaises(AttributeError):
            Rose(*self.rose_attributes2)

    def test_FlowerSet(self):
        flower_set = FlowerSet()
        flower_set.add_flowers(Flower(*self.flower_attributes))
        self.assertEqual(str(flower_set), 'Number of flowers in set: 1')
        rose = Rose(12,24)
        rose1 = Rose(15,30)
        tulip = Tulip(*self.tulip_attributes)
        chamomile = Chamomile(*self.chamomile_attributes)
        flower_set = FlowerSet()
        flower_set.add_flowers(rose)
        flower_set.add_flowers(rose1)
        self.assertEqual(str(flower_set), 'Number of flowers in set: 2')
        with self.assertRaises(AttributeError):
            flower_set.add_flowers(tulip)
        with self.assertRaises(AttributeError):
            flower_set.add_flowers(chamomile)
        with self.assertRaises(AttributeError):
            flower_set.add_flowers(123)
        with self.assertRaises(AttributeError):
            flower_set.add_flowers(Flower(*self.flower_attributes))
    def test_bucket(self):
        bucket = Bucket()
        flower_set = FlowerSet()
        rose = Rose(12, 24)
        rose1 = Rose(15, 30)
        rose2 = Rose(20, 50)
        flower_set.add_flowers(rose)
        flower_set.add_flowers(rose1)
        flower_set.add_flowers(rose2)
        bucket.add_set(flower_set)
        self.assertEqual(str(bucket), 'Number of sets in bucket: 1')
        with self.assertRaises(AttributeError): bucket.add_set(rose)
        with self.assertRaises(AttributeError): bucket.add_set('flowerset')
        with self.assertRaises(AttributeError): bucket.add_set(123)
        with self.assertRaises(AttributeError): bucket.add_set(bucket)
        with self.assertRaises(AttributeError): bucket.add_set(['Rose red 12 24', 'Rose red 15 30', 'Rose red 20 50'])
        total_price = bucket.total_price()
        self.assertEqual(total_price, 104)

if __name__ == '__main__':
    unittest.main()
