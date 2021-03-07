#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:59:09 2020

@author: viggomoro
"""

"""
This library provides a skip list data structure which stores a sorted sequence
of elements of the same type.

A skip list is a data structure is an efficient data structure for search, 
insertion and removal of elements in the Skip list. More specifically, all of 
the above operations have O(log n) in average case time complexity.

A skip list is built in layers where the bottom layer is an ordinary linked 
list. Each higher level acts an “express lane” for the lists below enabling 
fast search, insert and removal of elements. The number of layers for a given 
element is determined probabilistically with the probability 1 that it is in 
the lowest level and the probability p that it will be in the level x + 1 
given that it is in level x. In this implementation p = 0.5. Thus the skip list
contains log n in the base 1 / p sub lists. 
"""

import random


class _ListElement:
    """A list element in SkipList."""
    
    def __init__(self, data, below, level, Next=None):
        self._next = Next # Points at the next list element# Pekar på nästa element
        self._data = data # Stores the value of the list element.
        self._below = below # Points at an object with the same value one level belove. If level equals zero it points at None.
        self._level = level # The level of the list element.
                

class SkipList:
    """A skip list. All elements must me of the same type."""
    
    def __init__(self):
        """Creates an empty skip list."""
        self._head = _ListElement(None, None, 0) # The header for Skiplist. It will point at the highest level.
        self._size = 0 # Number of elements in the lowest level, level zero.
    
    def insert(self, element, level=None):
        """Inserts a given element in the skip list. If the same element is 
        already present in the list, it will be inserted after the the element 
        already present in the skip list."""
        if level == None:
            level = self._generate_level()
        if self._size == 0: # If the SkipList is empty.       
            self._head._next = _ListElement(element, None, 0)
            for level in range(1,level + 1):
                self._head = _ListElement(None, self._head, level) #  Creates additional levels if level is greater than zero.
                below = self._head._below._next
                self._head._next = _ListElement(element, below, level) # Adds the element at each level and sets the below pointer.  
            self._size += 1
        
        else:               
            max_level = self._head._level
            if level > max_level: # Creates additional levels if needed.
                for level in range(max_level + 1, level + 1):
                    self._head = _ListElement(None, self._head, level)

            reference_pointer = None
            current_node = self._head
            while current_node != None: # As long as we are on level zero or above.
                current_level = current_node._level
                if current_level <= level: # If we are going to make an insertion at this level.
                    if current_node._data == None and current_node._next == None: # If the level is empty.
                        current_node._next = _ListElement(element, None, current_level)
                        if reference_pointer != None and current_node._level >= 0: # Sets the below pointer for the inserted element as long as we are not at max_level.
                            reference_pointer._below = current_node._next 
                        reference_pointer = current_node._next                         
                    else:
                        
                        while True: # Iterates to the correct place for insertion for the given level.
                            if current_node._data == None: # If we are in the head-stack.
                                if element < current_node._next._data:
                                    current_node._next = _ListElement(element, None, current_level, current_node._next) # Insättning av elementet
                                    if reference_pointer != None and current_node._level >= 0:
                                        reference_pointer._below = current_node._next # Sets the below pointer.
                                    reference_pointer = current_node._next                                        
                                    break
                                else:
                                    current_node = current_node._next                                    
                            else:
                                if current_node._next == None or current_node._data <= element < current_node._next._data: # If we are at the right place for inserion.
                                    current_node._next = _ListElement(element, None, current_level, current_node._next)
                                    if reference_pointer != None and current_node._level >= 0:
                                        reference_pointer._below = current_node._next
                                    reference_pointer = current_node._next                                      
                                    break
                                else:
                                    current_node = current_node._next                                   
                current_node = current_node._below
            self._size += 1
     
    def _generate_level(self):
        """Private help method for insert. It generates the the level for an 
        element to be inserted by randomness. The probability of level x is 
        (1/2)^x. """
        level = 0
        while True:
            if random.random() <= 0.5:
                break
            level += 1
        return level
            
    def search(self, element):      
        """Searches the skip list for an given element and return True if the 
        element if found and False otherwise."""
        if self._size == 0:
            return False
        current_node = self._head
        while current_node != None:
            if current_node._next == None:
                current_node = current_node._below             
            else:
                if current_node._next._data == element:
                    return True
                elif current_node._next._data < element:
                    current_node = current_node._next
                else:
                    current_node = current_node._below
        return False
        
    def remove(self, element):
        """Removes and returns the given element at all levels in the skip 
        list. If the element isn't present in the skip list None is returned. 
        If there are more than one element with the same value the one in the 
        highest level i removed. If there are more elements with the same value 
        in the same upmost level the first element is returned. ."""
        if self._size == 0:
            return None
        current_node = self._head
        node_below = None
        while current_node != None: # As long as we are at level zero or above.
            if current_node._next == None: # If we are at the last list element at a given level. 
                current_node = current_node._below             
            else:
                if current_node._next._data == element and (current_node._next == node_below or node_below == None): # If it's the same value and the same object, not only the same value, so that we remove the object which had which was pointed at by the last previous removed object.   
                    node_below = current_node._next._below
                    current_node._next = current_node._next._next
                    if current_node._level == 0:
                        self._size -= 1
                        while self._head._next == None and self._head._level > 0: # Remove empty stacks.
                            self._head = self._head._below
                        return current_node._data 
                    current_node = current_node._below                          
                elif current_node._next._data < element:
                    current_node = current_node._next
                elif current_node._next._data > element:
                    current_node = current_node._below
                else:
                    current_node = current_node._next
        return None
    
    def getFirst(self, level=0):
        """Returns the first elemnt for a given level. None is returned if the 
        skip list is empty for the given level or if level is greater than the 
        maximum level in the skip list."""
        if self._size == 0 or level > self._head._level:
            return None
        current_head = self._head
        while current_head._level > level:
            current_head = current_head._below
        return current_head._next._data
    
    def getLast(self, level=0):
        """Returns the last elemnt for a given level. None is returned if the 
        skip list is empty at the given level or if level is greater than the 
        maximum level in the skip list."""
        if self._size == 0 or level > self._head._level:
            return None       
        current_node = self._head
        while current_node._level > level:
            while current_node._next != None:
                current_node = current_node._next
            current_node = current_node._below        
        while current_node._next != None:
            current_node = current_node._next
        return current_node._data
        
    def getElement(self, index, level):
        """Returns the element at position index at given level. None is 
        returned if level or index is out of range for the skip list. The skip 
        list is zero indexed."""
        if level > self._head._level:
            return None
        current_node = self._head       
        while current_node._level > level:
            current_node = current_node._below
        counter = -1 # Ty listan defineras som nollindexerad
        while counter < index:
            current_node = current_node._next
            counter += 1
            if current_node == None:
                return None
        return current_node._data
    
    def clear(self):
        """Remove all elemnts at all levels so that the skip list becomes empty."""
        self._head = _ListElement(None, None, 0)
        self._size = 0
    
    def getSize(self):
        """Returns the number of elements in the skip list att level zero."""
        return self._size
    
    def stringRepresentation(self):
        pass
    
    
def main():
    skiplist = SkipList()
    assert skiplist._head._data == None
    assert skiplist._head._next == None
    assert skiplist.getSize() == 0
    assert skiplist.getFirst(0) == skiplist.getLast(0) == None
    assert skiplist.search(3) == False
    assert skiplist.remove(3) == None
    assert skiplist.getElement(3, 2) == None

    skiplist.insert(1, 3)
    assert skiplist._head._data == skiplist._head._below._data == skiplist._head._below._below._data == None
    assert skiplist._head._level == 3
    assert skiplist._head._next._data == 1
    assert skiplist._head._next._below._data == 1
    assert skiplist._head._below._below._below._next._below == None
    assert skiplist.getSize() == 1
    assert skiplist.getFirst(4) == None
    assert skiplist.getFirst(3) == skiplist.getFirst(2) == skiplist.getLast(1) == 1
    assert skiplist.search(1) == True
    assert skiplist.search(2) == False
    assert skiplist.getElement(0, 2) == 1
    
    skiplist.insert(2, 1)
    assert skiplist._head._level == 3
    assert skiplist._head._next._data == 1
    assert skiplist._head._below._below._next._next._data == 2
    assert skiplist._head._below._below._next._next._data == 2
    assert skiplist._head._below._below._below._next._next._data == 2
    assert skiplist._head._next._below._below._below._data == 1 
    assert skiplist._head._below._below._next._next._below._data == 2
    assert skiplist._head._below._below._next._next._below._below == None
    assert skiplist.getSize() == 2
    assert skiplist.getLast(3) == 1
    assert skiplist.getLast(1) == 2 
    assert skiplist.getLast(0) == 2
    assert skiplist.search(2) == True
    assert skiplist.search(5) == False
    assert skiplist.getElement(1,0) == 2

    skiplist.insert(2,4)
    assert skiplist._head._level == 4
    assert skiplist._head._next._below._next == None
    assert skiplist._head._next._below._data == 2
    assert skiplist._head._next._below._below._data == 2
    assert skiplist._head._next._below._below._below._data == 2
    assert skiplist._head._next._below._below._below._below._data == 2
    assert skiplist._head._below._below._below._next._next._below._data == 2
    assert skiplist._head._next._below._below._below._level == 1
    assert skiplist.getSize() == 3
    assert skiplist.getFirst(5) == skiplist.getLast(5) == None
    assert skiplist.getFirst(0) == 1
    assert skiplist.getLast(0) == 2
    assert skiplist.search(1) == skiplist.search(2) == True
    assert skiplist.search(8) == False
    assert skiplist.getElement(2, 4) == None
    assert skiplist.getElement(1, 3) == 2

    skiplist.insert(5, 3)
    skiplist.insert(8,2)
    skiplist.insert(6,0)
    assert skiplist.getSize() == 6
    assert skiplist.getLast() == 8
    skiplist.remove(8)
    assert skiplist.remove(8) == None
    assert skiplist.getSize() == 5
    assert skiplist.getLast() == 6
    assert skiplist._head._level == 4
    assert skiplist._head._next._data == 2
    skiplist.remove(2)
    assert skiplist._head._level == 3
    assert skiplist._head._next._data == 1
    
    
if __name__ == '__main__':
    main()
    print('main körd')