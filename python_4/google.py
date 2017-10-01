#!/usr/bin/env python3

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, child):
        self.left = child
        child.parent = self

    def set_right(self, child):
        self.right = child
        child.parent = self

def insert(tree, item):
    if not tree:
        return TreeNode(item)
    if tree.value > item:
        tree.set_left(insert(tree.left, item))
    else:
        tree.set_right(insert(tree.right, item))
    return tree

def create_tree(items):
    tree = None
    for item in items:
        tree = insert(tree, item)
    return tree

class AbstractTreeIterator:
    def __init__(self, root):
        self.root = root
        self.current = root

    @staticmethod
    def left_most(node):
        while node.left:
            node = node.left
        return node

    @staticmethod
    def right_most(node):
        while node.right:
            node = node.right
        return node

    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        return self

def inorder(tree):
    if tree:
        yield from inorder(tree.left)
        yield tree.value
        yield from inorder(tree.right)

class InOrder(AbstractTreeIterator):
    def __iter__(self):
        return inorder(self.root)

class LevelOrder(AbstractTreeIterator):
    raise NotImplementedError

def print_tree(iterator, msg=''):
    print(msg, ' '.join(str(i) for i in iterator))

if __name__ == '__main__':
    tree = create_tree([2, 1, 3, 5, 8, 7])
    print_tree(InOrder(tree), 'In order:')
    print_tree(LevelOrder(tree), 'Level order:')
