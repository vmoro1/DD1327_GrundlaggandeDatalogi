#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 06:45:41 2020

@author: viggomoro
"""

class _ListElement:
    """A list element that stores a value of type T."""
    
    def __init__(self, data):
        """Innitiates a list element with a value and and the next list element."""
        self._data = data
        self._next = None


class LinkedList:
    """A singly linked list of elements of type T."""
    
    def __init__(self):
        """Create an empty list."""
        self._first = None # first element in list
        self._last = None  # last element in list
        self._size = 0    # number of elements in list

    def addFirst(self, element):
        """Insert the given element at the beginning of this list."""
        list_element = _ListElement(element)
        if self._first is None:
            self._first = list_element
            self._last = list_element
        elif self._first._next is None:
            list_element._next = self._last
            self._first = list_element
        else:    
            list_element._next = self._first
            self._first = list_element
        self._size += 1     
# Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
        
    def addLast(self, element):
        """Insert the given element at the end of this list."""
        list_element = _ListElement(element)
        if self._last is None:
            self._first = list_element
            self._last = list_element
        elif self._first._next is None:
            self._last = list_element
            self._first._next = self._last
        else:
            self._last._next = list_element
            self._last = list_element
        self._size += 1       
# Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
        
    def getFirst(self):
        """Return the first element of this list. Return null if the list is empty."""
        if self._first == None:
            return None
        return self._first._data
# Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
    
    def getLast(self):
        """Return the last element of this list. Return null if the list is empty."""
        if self._last == None:
            return None
        return self._last._data
#Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
    
    def get(self, index):
        """Return the element at the specified position in this list. 
        Return null if index is out of bounds."""
        if index <= 0:
            return None
        currentElement = self._first
        if currentElement is None:
            return None
        for i in range(index-1):
            currentElement = currentElement._next
            if currentElement == None:
                return None         
        return currentElement._data 
#Dennaa metod har linjär värstafallstid dvs. T(n) tillhör O(n).
    
    def removeFirst(self):
        """Remove and returns the first element from this list.
        Return null if the list is empty."""
        if self._size == 0:
            return None
        self._size -= 1
        firstElement = self._first
        secondElement = self._first._next
        if self._first._next is None:
            self._first = None
            self._last = None
            return firstElement
        self._first._next = None
        self._first  = secondElement
        return firstElement     
# Dennaa metod har konstant värstafallstid dvs. T(n) tillhör O(1).
    
    def clear(self):
        """Remove all elements from this list."""
        # while self._first:
        #     nextElement = self._first._next
        #     self._first._next = None
        #     self._first = nextElement
        # self._size = 0
        # # self._last = None
        self._size = 0
        self._first = None
        self._last = None     
#Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
        
    def size(self):
        """Return the number of elements in this list."""
        return self._size 
        # length = 0
        # currentElement = self._first
        # while currentElement:
        #     currentElement = currentElement._next
        #     length += 1
        # return length  
# Denna metod har konstant värstafallstid dvs. T(n) tillhör O(1).
    
    def string(self):
        """Return a string representation of this list. The elements are 
        enclosed in square brackets ("[]"). Adjacent elements are separated 
        by ", "."""
        StringRepresentation = ''
        currentElement = self._first
        while currentElement:
            if currentElement._next == None:
                StringRepresentation += "[" + str(currentElement._data) + "]"
            else:
                StringRepresentation += "[" + str(currentElement._data) +"], "
            currentElement = currentElement._next
        return StringRepresentation
#Denna metod har linjär värstafallstid dvs. T(n) tillhör O(n).
    
    def healthy(self):
        """Tests that the list hasn't been broken."""
        length = 0
        currentElement = self._first
        while currentElement:
            currentElement = currentElement._next
            length += 1
        
        if length != self._size:
            return False
        if self._size == 0 and (self._first != None or self._last != None):
            return False
        if self._last != None and self._last._next != None:
            return False
        return True
# Denna metod har linjär värstafallstid dvs. T(n) tillhör O(n).
    
def main():
    """Test code for class LinkedList."""
    linked_list = LinkedList()
    assert linked_list.size() == 0
    assert linked_list.string() == ''
    assert linked_list.getFirst() == linked_list.getLast() == None
    assert linked_list.healthy()
    
    linked_list.addFirst('Hello')
    assert linked_list.size() == 1
    assert linked_list.getFirst() == linked_list.getLast() == 'Hello'
    assert linked_list.get(2) == None
    assert linked_list.string() == '[Hello]'
    assert linked_list.healthy()
    
    linked_list.addLast('world!')
    assert linked_list.size() == 2
    assert linked_list.getFirst() == 'Hello'
    assert linked_list.getLast() == 'world!'
    assert linked_list.healthy()
    
    linked_list.removeFirst()
    assert linked_list.size() == 1
    linked_list.removeFirst()
    assert linked_list.size() == 0
    assert linked_list.string() == ''
    assert linked_list.getFirst() == linked_list.getLast() == None
    assert linked_list.healthy()
    
    data = 'abcde'
    string = ''     
    for i in range(len(data)):
        if i == len(data)-1:
            string += "[" + str(data[i]) + "]"
        else:
            string += "[" + str(data[i]) + "], "
    for element in data:
        linked_list.addLast(element)       
    assert linked_list.getFirst() == data[0]
    assert linked_list.getLast() == data[len(data)-1]
    assert linked_list.get(3) == data[2]
    assert linked_list.string() == string
    linked_list.clear()
    assert linked_list.size() == 0
    assert linked_list.healthy()
    
if __name__ == '__main__':
    main()               