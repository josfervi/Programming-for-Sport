# https://www.hackerrank.com/contests/projecteuler/challenges/euler001


#!/bin/python

import sys


def one_answer(x, y, n):
  ''' Returns the sum of all the multiples of
        x and y below or equal to n.
  '''
  
  if x == y:
    return sum_of_multiples(x, n)
  
  return sum_of_multiples(x, n) + sum_of_multiples(y, n) - sum_of_multiples(x*y, n)


def sum_of_multiples(x, n):
  ''' Returns the sum of all the multiples of
        x below or equal to n.
  '''
  
  # number of mutiples of x below or equal to n
  num_of_multiples = n/x
  
  return x * sum_of_ints_from_1_to( num_of_multiples)


def sum_of_ints_from_1_to(x):
  
  return ((x+1) * x) / 2


t = int(raw_input().strip())
for _ in xrange(t):
    n = int(raw_input().strip())

    print one_answer(3, 5, n-1)
