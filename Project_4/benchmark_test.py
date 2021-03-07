#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:53:34 2020

@author: viggomoro
"""
import time
import random
from matplotlib import pyplot as plt

def pow(n):
	"""Return 2**n, where n is a nonnegative integer."""
	if n == 0:
		return 1
	x = pow(n//2)
	if n%2 == 0:
		return x*x
	return 2*x*x


def sum1(a):
	"""Return the sum of the elements in the list a."""
	n = len(a)
	if n == 0:
		return 0
	if n == 1:
		return a[0]
	return sum1(a[:n//2]) + sum1(a[n//2:])


def sum2(a):
	"""Return the sum of the elements in the list a."""
	return _sum(a, 0, len(a)-1)

def _sum(a, i, j):
	"""Return the sum of the elements from a[i] to a[j]."""
	if i > j:
		return 0
	if i == j:
		return a[i]
	mid = (i+j)//2
	return _sum(a, i, mid) + _sum(a, mid+1, j)


size = [10, 100, 1000, 10000, 100000, 1000000]
    
def time_test(function, test_data):
    elapsed_time = []
    for n in test_data:
        start = time.time()
        function(n)
        elapsed_time.append(time.time() - start)
    return elapsed_time

test_lists = []    
for i in range(len(size)):
    new_list = []
    for j in range(size[i]):
        new_list.append(random.random())
    test_lists.append(new_list)
    

time_pow = time_test(pow, size)
time_sum1 = time_test(sum1, test_lists)
time_sum2 = time_test(sum2, test_lists)
      

plt.plot(size, time_pow)
plt.xlabel('Size of input')
plt.ylabel('Runtime pow')

# plt.plot(size, time_sum1)
# plt.xlabel('Size of input')
# plt.ylabel('Runtime sum1')

# plt.plot(size, time_sum2)
# plt.xlabel('Size of input')
# plt.ylabel('Runtime sum2')