#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 06:28:33 2020

@author: viggomoro
"""

def factorial(n):
    """Calculates the factorial of a non-negative integer and returns the value."""
    if n == 0:
        return 1
    for i in range(n-1,0,-1):
        n *= i
    return n

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
assert factorial(5) == 120
