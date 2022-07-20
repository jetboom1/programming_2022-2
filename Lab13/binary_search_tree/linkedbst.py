"""
File: linkedbst.py
Author: Ken Lambert
"""
import math
import random
import time

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from math import log


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def inorder_iterative(self):
        """Inorder traversal of the tree. Iterative version."""
        stack = LinkedStack()
        current = self._root
        while current or not stack.isEmpty():
            if current:
                stack.push(current)
                current = current.left
            else:
                current = stack.pop()
                yield current.data
                current = current.right
    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        root = self._root
        while self._root != None:
            if item > root.data:
                root = root.right

            elif item < root.data:
                root = root.left
            else:
                return True
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""
        # Begin main part of the method
        node = BSTNode(item)
        if self._root is None:
            self._root = node
            self._size += 1
            return
        prev = None
        temp = self._root
        while temp != None:
            if temp.data > item:
                prev = temp
                temp = temp.left
            elif temp.data < item:
                prev = temp
                temp = temp.right
        if prev.data > item:
            prev.left = node
        else:
            prev.right = node
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None

        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right

        # Return None if the item is absent
        if itemRemoved == None: return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
                and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:

            # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right

                # Case 3: The node has no right child
            else:
                newChild = currentNode.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''

        def height1(top):
            '''
            Helper function
            :param top:
            :return:
            '''
            if top == None:
                return 0
            return 1 + max(height1(top.left), height1(top.right))

        root = self._root
        if root is None:
            return 0
        return height1(root)

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''
        n = self._size
        tree_height = self.height()
        if tree_height < 2 * math.log2(n + 1) - 1:
            return True
        return False

    def rangeFind(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''
        def recurse(node):
            if node is None:
                return []
            elif low <= node.data <= high:
                return [node.data] + recurse(node.left) + recurse(node.right)
            elif node.data < low:
                return recurse(node.right)
            else:
                return recurse(node.left)
        return recurse(self._root)

    def rebalance(self):
        '''
        Rebalances the tree. Iterative version.
        :return:
        '''
        nodes_array = []
        for node in self.inorder_iterative():
            nodes_array.append(node)
        self.clear()

        self._size = len(nodes_array)
        size = self._size
        # Add to the stack a node that will be a root of the tree:
        root_node = BSTNode(None)

        # Stack stores tuples of the current node, and the first and the last indices of half-segments:
        stack = LinkedStack()
        stack.push((root_node, 0, size - 1))

        while not stack.isEmpty():
            node, first, last = stack.pop()

            if last < first:
                # The segment is degenerated. Do nothing.
                continue
            elif last == first:
                # Assign the value, it is the last bottom node.
                node.data = nodes_array[last]
                continue

            mid = (first + last) // 2
            node.data = nodes_array[mid]
            node.left = BSTNode(None)
            node.right = BSTNode(None)

            # Update the stack with the left and the right half-segment:
            stack.push((node.right, mid + 1, last))
            stack.push((node.left, first, mid - 1))

        self._root = root_node
        # def recurse(array):
        #     if len(array) == 0:
        #         return None
        #     mid = len(array) // 2
        #     root = BSTNode(array[mid])
        #     self._size += 1
        #     root.left = recurse(array[:mid])
        #     root.right = recurse(array[mid + 1:])
        #     return root
        #
        # new_root = recurse(nodes_array)
        # self._root = new_root
        return self.is_balanced()

    def findMinimum(self, root):
        while root.left:
            root = root.left
        return root.data

    def findMaximum(self, root):
        while root.right:
            root = root.right
        return root.data

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        if self.isEmpty():
            return None
        probe = self._root
        succ = None
        while probe is not None:
            if probe.data == item:
                if probe.right is not None:
                    return self.findMinimum(probe.right)
                else:
                    if succ is None:
                        return None
                    return succ.data
            elif probe.data > item:
                succ = probe
                probe = probe.left
            elif probe.data < item:
                probe = probe.right
        return succ.data  # case where item is not in the tree

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        if self.isEmpty():
            return None
        probe = self._root
        pred = None
        while probe is not None:
            if probe.data == item:
                if probe.left is not None:
                    return self.findMaximum(probe.left)
                else:
                    if pred is None:
                        return None
                    return pred.data
            elif probe.data > item:
                probe = probe.left
            elif probe.data < item:
                pred = probe
                probe = probe.right
        return pred.data  # case where item is not in the tree or is the minimum

    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        """
        WORDS_COUNT = 10000
        DICTIONARY_WORDS_MAX = 25000
        def read_file_to_list(path):
            with open(path, 'r') as f:
                return f.read().split()[:DICTIONARY_WORDS_MAX]

        def get_random_words(list_words):
            return random.sample(list_words, WORDS_COUNT)

        def search_list(words_list, words):
            start_time = time.time()
            for word in words:
                words_list.index(word)
            end_time = time.time()
            return end_time - start_time

        def search_bst(bst, words):
            start_time = time.time()
            for word in words:
                bst.find(word)
            end_time = time.time()
            return end_time - start_time

        def search_random_bst(words_list, words):
            random.shuffle(words_list)
            bst = LinkedBST()
            for word in words_list:
                bst.add(word)
            start_time = time.time()
            for word in words:
                bst.find(word)
            end_time = time.time()
            return end_time - start_time

        def search_balanced_bst(bst, words):
            bst.rebalance()
            start_time = time.time()
            for word in words:
                bst.find(word)
            end_time = time.time()
            return end_time - start_time

        def generate_bst(words_list):
            bst = LinkedBST()
            c = 0
            for word in words_list:
                bst.add(word)
                c += 1
            return bst
        print('Reading file & building a tree...')
        words_list = read_file_to_list(path)
        random_words = get_random_words(words_list)
        bst = generate_bst(words_list)
        print('Welcome to our dashboard!')
        print('Please, choose one of the following options:')
        print('1. Search list of words')
        print('2. Search binary search tree')
        print('3. Search random binary search tree')
        print('4. Search balanced binary search tree')
        print('5. Exit')
        while True:
            try:
                option = int(input('Your choice: '))
                if option == 1:
                    print('Time of search:')
                    print(search_list(words_list, random_words))
                elif option == 2:
                    print('Time of search:')
                    print(search_bst(bst, random_words))
                elif option == 3:
                    print('Time of search:')
                    print(search_random_bst(words_list, random_words))
                elif option == 4:
                    print('Time of search:')
                    print(search_balanced_bst(bst, random_words))
                elif option == 5:
                    print('Bye!')
                    break
                else:
                    print('Invalid option!')
            except ValueError:
                print('Invalid option!')



if __name__ == '__main__':
    bst = LinkedBST()
    bst.demo_bst('words.txt')