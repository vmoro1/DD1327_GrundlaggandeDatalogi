#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:10:13 2020

@author: viggomoro
"""

def recursive_factorial(n):
    """Returns de factorial of the non negative integer n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
# Låt algoritmen vara P(n) där n >= 0. För basfallen n = 0 och n = 1 stämmer 
#algoritmen, dvs P(0) = P(1) = 1. Om vi antar att algoritmen stämmer för 
#n = i < k, dvs. P(i) = i!. Då får vi P(k) som P(k) = k * P(i) = k * i! = k!
#Genom induktion kan vi således konstatera att P(n) retunerar n fakultet, n!.
    

assert recursive_factorial(0) == 1
assert  recursive_factorial((1)) == 1
assert recursive_factorial(2) == 2
assert recursive_factorial(3) == 6
assert recursive_factorial(4) == 24
assert recursive_factorial(5) == 120