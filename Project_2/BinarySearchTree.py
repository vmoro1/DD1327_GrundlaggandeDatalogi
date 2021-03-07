#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:34:51 2020

@author: viggomoro
"""

class _Node:
    """Creates nodes for the treap."""  
    def __init__(self, key):
        self._key = key # Stores the key of each node
        self._left = None # Left child
        self._right = None # Right child
    
    
class unbalancedBNT:
    """Creates an unbalanced binary serach tree."""
     
    def __init__(self):
        self._root = None # root of the tree.
        self._size = 0 # Number of elements in tree.

    def add(self, key):
        """Inserts the given element in the tree."""
        if key not in self._traversal(self._root, []):
            self._size += 1
            if self._root == None:
                self._root = _Node(key)
            else:
                self._add(self._root, key)
    # Denna metod är O(n) eftersom den använder sig av _add() som är O(n), dvs. 
    #den har linjär tidskomplexitet.
    
    def _add(self, node, key):
        """Private help method for add()."""
        if key < node._key:
            if node._left != None:
                self._add(node._left, key)
            else:
                node._left = _Node(key)
        else:
            if node._right != None:
                self._add(node._right, key)
            else:
                node._right = _Node(key)
    # Denna metod är =(n) och har därför linjär .
                
    def size(self):
        """Returns the number of elements in the treap."""
        return self._size
    #Denna metod är O(1) dvs. konstant tidskomplexitet.
    
    def string(self):
        """Returns a string representation of the treap."""
        if self._root == None:
            data = []
        else:
            data = self._traversal(self._root, [])
        StringRepresentation = ''
        for i in range(len(data)):
            if i == len(data) - 1:
                StringRepresentation += data[i]
            else:
                StringRepresentation += data[i] + ', '
        return StringRepresentation       
    # Denna metod är O(n) då den använder sig av _traversal() som är O(n).
    # Vi har alltså linjär tidskomplexitet.
             
    def _traversal(self, node, data):
        """Travels through the three in order and returns a sorted list of the 
        elements in the tree."""
        if node != None:
            self._traversal(node._left, data)
            data.append(node._key)
            self._traversal(node._right, data)
        return data
    # Denna metod är O(n) har linjär tidskomplexitet.
           

def main():
    tree = unbalancedBNT()
    assert tree.size() == 0
    assert tree.string() == ''
    assert tree._root == None
    
    tree.add('a')
    tree.add('a')
    assert tree.size() == 1
    assert tree.string() == 'a'
    assert tree._root._key == 'a'
    
    tree.add('c')
    tree.add('v')
    tree.add('h')
    assert tree.size() == 4
    assert tree.string() == 'a, c, h, v'
    assert tree._root._left == None
    assert tree._root._right._key == 'c'
    assert tree._root._right._right._key == 'v'

    data = 'adcisoe'
    newTree = unbalancedBNT()
    for elem in data:
        newTree.add(elem)
    
    assert newTree.size() == len(data)
    assert newTree.string() == 'a, c, d, e, i, o, s'
        

if __name__ == '__main__':
    main()
    
    
# 2.2
    
# A = [1,2,3,4,5,6]
# B = []
# B[0]  = A[0]
# n = len(A)
# for i in range(1, n):
#     B[i] = B[i-1] + A[i]
