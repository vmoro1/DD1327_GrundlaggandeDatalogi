#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 09:44:25 2020

@author: viggomoro
"""

def dna():
    """Regex that matches a string if and only if it's a DNA sequense. 
    (Only the capital letter ACGT)"""
    return '^[AGCT]+$'

def sorted(): 
    """Regex that matches a string consisting of the character 0-9 if and only 
    if the characters are sorted in descending order."""      
    return "^(?=\d*$)9*8*7*6*5*4*3*2*1*0*$"

def hidden1(x):
    """Regex that matches if and only if the given string x is a substring."""
    return "\w*" + x + "\w*"

def hidden2(x):
    """Regex that matches if and oly if x is a partial sequens. That is, we 
    can remove characters from the string to form x."""
    a = ""
    for character in x:
        a += ".*" + character
    a += ".*"
    return a

def equation():
    return ""


from sys import stdin
import re

def main():
    def hidden1_test(): return hidden1('test')
    def hidden2_test(): return hidden2('test')
    tasks = [dna, sorted, hidden1_test, hidden2_test, equation, parentheses, sorted3]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '': break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE ' 
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))
    
# if __name__ == '__main__':
#     main()