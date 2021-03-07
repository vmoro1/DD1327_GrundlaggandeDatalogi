#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:39:42 2020

@author: viggomoro
"""

def mode(vector):
    """Calculates the mode of a vector containing integers. If several 
    elements occur equaly frequent the smallest is returned."""
    dict_elem = {}
    for element in vector:
        if str(element) in dict_elem:
            dict_elem[str(element)] += 1
        else:
            dict_elem[str(element)] = 1
    
    element = None
    frequency = 0
    for key in dict_elem:
        if dict_elem[key] > frequency:
            element = int(key)
            frequency = dict_elem[key]
        elif dict_elem[key] == frequency:
            if int(key) < element:
                element = int(key)
                frequency = dict_elem[key]
    return element, frequency
    # Denna funktion är O(n) ty dictionaries i python är hashtabeller och 
    #för dem gäller att hitta ett element är O(1).
        

def main():
    element, frequency = mode([])
    assert frequency == 0
    assert element == None
    
    element, frequency = mode([2])
    assert element == 2
    assert frequency == 1
    
    element, frequency = mode([1,2,3,6,3,1,6,7,6,6])
    assert element == 6
    assert frequency == 4
    
    
if __name__ == '__main__':
    main()   