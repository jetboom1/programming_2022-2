import unittest
from linkedbst import LinkedBST

class test_linkedbst(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = LinkedBST()
        self.tree.add(1)
        self.tree.add(2)
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(5)
        self.tree.add(6)
        self.tree.add(7)
        print(self.tree)
    def test_height(self):
        self.assertEqual(self.tree.height(), 7)
    def test_is_balanced(self):
        self.assertFalse(self.tree.is_balanced())
    def test_rebalancing(self):
        self.assertTrue(self.tree.rebalance())
        self.assertTrue(self.tree.is_balanced())
    def test_predecessor(self):
        self.tree.rebalance()
        self.assertEqual(self.tree.predecessor(1), None)
        self.assertEqual(self.tree.predecessor(2), 1)
        self.assertEqual(self.tree.predecessor(3), 2)
        self.assertEqual(self.tree.predecessor(4), 3)
        self.assertEqual(self.tree.predecessor(5), 4)
        self.assertEqual(self.tree.predecessor(6), 5)
        self.assertEqual(self.tree.predecessor(7), 6)
    def test_successor(self):
        self.tree.rebalance()
        self.assertEqual(self.tree.successor(1), 2)
        self.assertEqual(self.tree.successor(2), 3)
        self.assertEqual(self.tree.successor(3), 4)
        self.assertEqual(self.tree.successor(4), 5)
        self.assertEqual(self.tree.successor(5), 6)
        self.assertEqual(self.tree.successor(6), 7)
        self.assertEqual(self.tree.successor(7), None)
    def test_rangeFind(self):
        self.tree.rebalance()
        self.assertEqual(self.tree.rangeFind(1, 7), [4, 2, 1, 3, 6, 5, 7])
        self.assertEqual(self.tree.rangeFind(1, 5), [4, 2, 1, 3, 5])
        self.assertEqual(self.tree.rangeFind(1, 3), [2, 1, 3])
        self.assertEqual(self.tree.rangeFind(3, 4), [4, 3])
        self.assertEqual(self.tree.rangeFind(3, 3), [3])
        self.assertEqual(self.tree.rangeFind(3, 2), [])



if __name__ == '__main__':
    unittest.main()