#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:23:11 2020

@author: viggomoro
"""

def p(n, h):
    """Returns the maximal earning that can be made by by knitting scarfs of n 
    meter yarn. The price of a scarft of length n meters is h[n]. It is 
    required that n <= len(h) + 1."""
    if n == 0:
        return 0
    else:
        return max(h[i] + p(n - i, h) for i in range(1, n + 1))


assert p(0, []) == 0
assert p(1, [0, 3, 4]) == 3
assert p(3, [0, 2, 3, 4]) == 6
assert p(5, [0, 2, 5, 6, 9, 0]) == 12


def p_memo(n, h, mem):
    """Returns the maximal earning that can be made by by knitting scarfs of n 
    meter yarn. The price of a scarft of length n meters is h[n]. It is 
    required that n <= len(h) + 1."""
    if n in mem:
        return mem[n]
    if n == 0:
        return 0
    else:
        p = max(h[i] + p_memo(n - i, h, mem) for i in range(1, n + 1)) 
    mem[n] = p
    return p


assert p_memo(0, [], {}) == 0
assert p_memo(1, [0, 3, 4], {}) == 3
assert p_memo(3, [0, 2, 3, 4], {}) == 6
assert p_memo(5, [0, 2, 5, 6, 9, 0], {}) == 12
