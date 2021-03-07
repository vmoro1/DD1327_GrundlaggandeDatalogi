#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:22:42 2020

@author: viggomoro
"""

def sort(a):
    """This algorithm sorts the integers x1, x2,..., xn and returns a sorted 
    list. Returns None if the list is empty. All integers xi where i = 1, 2,...,
    n satisfy that 0 <= xi <= k. The worst case time complexity of the 
    algorithm is O(n + k)."""
    if a == []:
        return None
    k = max(a)
    count = (k+1) * [0]
    for i in range(len(a)):
        count[a[i]] += 1
    
    output = []
    for i in range(k+1):
        new = count[i] * [i]
        output += new
    return output
   

# Algortimen blir linjär då k tillhör O(n) för då kommer O(n+k) tillhöra O(n+n)
# = O(2n) = O(n) som är linjär.
        
    


assert sort([]) == None
assert sort([4]) == [4]
assert sort([1,2,2,4,2,3,1,6]) == [1, 1, 2, 2, 2, 3, 4, 6]
assert sort([1,2,3,4,3,4,8,6]) == [1, 2, 3, 3, 4, 4, 6, 8]
assert sort([1,3,2,4,1,1,9]) == [1, 1, 1, 2, 3, 4, 9]


def sort2(a):
    """This algorithm sorts a list of n integers where repetitions may occur 
    and returns a sorted list. The total number of distict element are k. The 
    algoruthm has time complexity O(n + klogk)."""
    elem_dict = {}
    for i in range(len(a)):
        if str(a[i]) in elem_dict:
            elem_dict[str(a[i])] += 1
        else:
            elem_dict[str(a[i])] = 1
    
    distict_elem = []
    for key in elem_dict:
        distict_elem.append(key)
    
    sorted_distict = sorted(distict_elem) # Detta steg är O(klogk)
    output = len(a) * []
    for elem in sorted_distict:
        new = elem_dict[elem] * [int(elem)]
        output += new
    return output

# Algortimen blir linjär då klogk tillhör O(n) för då kommer O(n+klogk) tillhöra O(n+n)
# = O(2n) = O(n) som är linjär.


assert sort2([]) == []
assert sort2([4]) == [4]
assert sort2([1,2,2,-1,4,2,3,1,6]) == [-1, 1, 1, 2, 2, 2, 3, 4, 6]
assert sort2([1,2,3,4,3,4,8,6]) == [1, 2, 3, 3, 4, 4, 6, 8]
assert sort2([1,3,2,4,1,1,9]) == [1, 1, 1, 2, 3, 4, 9]   