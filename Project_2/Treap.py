#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:43:00 2020

@author: viggomoro
"""
import random

class _Node:
    """Creates a node for the treap."""
    
    def __init__(self, key, priority=random.random()):
        self._key = key # Stored data
        self._left = None # Left child
        self._right = None # Right child
        self._priority = priority # Priority number to rebalance the tree.
        
    def _right_rotation(self):
        """Performes a right rotatoin of the treap."""
        current_parentNode = self
        inserted_node = current_parentNode._left
        current_parentNode._left = inserted_node._right
        inserted_node._right = current_parentNode
        current_parentNode = inserted_node
        inserted_node = current_parentNode._right
        return current_parentNode
    # Denna metod är O(1).
    
    def _left_rotation(self):
        """Performs a left rotation of the trep."""
        current_parentNode = self
        inserted_node = current_parentNode._right
        current_parentNode._right = inserted_node._left
        inserted_node._left = current_parentNode
        current_parentNode = inserted_node
        inserted_node = current_parentNode._left
        return current_parentNode
    # Denna metod är O(1).
    
class Treap:
    """Creates a treap consisting of strings."""
     
    def __init__(self):
        self._root = None # Root of the tree
        self._size = 0 #Number of elements in the treap

    def add(self, key, *priority):
        """Inserts the given element in the treap. The optional argument 
        priority is only used for testing purposes."""
        if not self._search(key, self._root):   
            self._size += 1
            if priority:
                new_node = _Node(key, priority)
            else:          
                new_node = _Node(key)
            self._root = self._add(self._root, new_node)
    #Denna metod är O(log(n)) då den använder sig av _add() och _search() som 
    #båda är O(log(n)) eftersom trädet är ordnat och balanserat.

    def _add(self, node, new_node):
        """Private help method for add()."""
        if node == None:
            return new_node
        if new_node._key < node._key:
            node._left = self._add(node._left, new_node)
            if node._priority > node._left._priority:
                node = node._right_rotation()          
        else:
            node._right = self._add(node._right, new_node)
            if node._priority > node._right._priority:
                node = node._left_rotation()
        return node
    #Denna metod är O(log(n)) eftersom trädet är ordnat och balanserat.
    
    def _search(self, value, root):
        """Returns True if the value is found in the tree and False otherwise."""
        if root == None:
            return False
        if value == root._key:
            return True
        if value < root._key:
            return self._search(value, root._left)
        else:
            return self._search(value, root._right)
    # Denna metod är O(log(n))           
        
    def size(self):
        """Returns the number of elements in the treap."""
        return self._size
    # Denna metod är O(1).
    
    def string(self):
        """Returns a string representation of the element in the treap in 
        alphabetical order."""
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
    # Denna metod är O(n) eftersom vi har en for-loop över antalet element i 
    # trädet medan _traversal är O(log(n)).
             
    def _traversal(self, node, data):
        """Travels through the tree in order and returns a sorted list of the 
        elements in the treap."""
        if node != None:
            self._traversal(node._left, data)
            data.append(node._key)
            self._traversal(node._right, data)
        return data
    # Denna metod är O(log(n)).
         
            
def main():
    treap = Treap()
    assert treap.size() == 0
    assert treap.string() == ''
    
    treap.add('E', 3)
    treap.add('E')
    assert treap.size() == 1
    assert treap.string() == 'E'

    treap.add('H', 7)
    treap.add('B', 5)
    treap.add('A', 6)
    assert treap.size() == 4
    assert treap._root._key == 'E'
    assert treap._root._right._key == 'H'
    assert treap._root._left._right == None
    assert treap._root._left._key == 'B'
    
    treap.add('K', 8)
    treap.add('F', 9)
    treap.add('G', 2)
    assert treap.size() == 7
    assert treap.string() == 'A, B, E, F, G, H, K'
    
    assert treap._root._key == 'G'
    assert treap._root._right._key == 'H'
    assert treap._root._left._key == 'E'
    assert treap._root._right._right._key == 'K'
    assert treap._root._left._right._key == 'F'


if __name__ == '__main__':
    main()