#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:36 2020

@author: viggomoro
""" 

def separation(vector):
    """Loop invariant för den andra loopen: vector[:current_position - 1] < 0"""
    first_negative = None
    for i in range(len(vector)):
        if vector[i] < 0 and first_negative == None:
            first_negative = i
            break    
        
    if first_negative == None:
        return vector  
    if first_negative != 0:
        tmp = vector[0]
        vector[0] = vector[first_negative]
        vector[first_negative] = tmp

    current_position = 1
    for i in range(1, len(vector)):
        if vector[i] < 0:
            tmp = vector[i]
            vector[i] = vector[current_position]
            vector[current_position] = tmp
            current_position += 1
    return vector       
    #Denna funktoin är O(n).

# def separation(vector):
#     """Invariant: vector[0], ..., vector[current_position - 1] < 0. """
#     current_position = 0
#     for i in range(len(vector)):
#         if vector[i] < 0:
#             tmp = vector[i]
#             vector[i] = vector[current_position]
#             vector[current_position] = tmp
#             current_position += 1
#     return vector
    # Denna funktion är O(n).


def main():
    v1 = [-1, 2, 5, -6, 3, -7, 6, 0]
    sep_v1 = separation(v1)
    assert (sep_v1[0] and sep_v1[1] and sep_v1[2]) < 0
    assert (sep_v1[3] and sep_v1[4] and sep_v1[5] and sep_v1[6] and sep_v1[7]) >= 0
    
    v2 = [-1, 4, -7, 111, -7, -998, 2, 0]
    sep_v2 = separation(v2)
    assert sep_v2[3] < 0
    assert sep_v2[4] >= 0


if __name__ == '__main__':
    main()