# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/submissions/code/1301063240

#!/bin/python

import sys


def one_answer(n):
  ''' By considering the terms in the Fibonacci
        sequence whose values do not exceed n,
        find the sum of the even-valued terms.
  '''
  
  fib_im1, fib_i, sum_up_to_fib_i = sum_of_fibonacci_terms_up_to( n)
  
  if is_even(fib_i):
    return sum_up_to_fib_i >> 1
  
  # is_odd(fib_i)
  
  if is_even(fib_im1):
    return (sum_up_to_fib_i - fib_i) >> 1
  
  # is_odd(fib_im1)
  
  fib_im2 = fib_i - fib_im1
  assert is_even(fib_im2)
  
  return (sum_up_to_fib_i - fib_i - fib_im1) >> 1


def is_even(num):
  return num % 2 == 0


def is_odd(num):
  return not is_even(num)


def sum_of_fibonacci_terms_up_to( n):
  ''' Returns the sum of the fibonacci numbers
        that do no exceed n.
        Also returns the last two numbers of that sum.
  '''
  
  if n == 0:
    return (0, 0, 0)
  
  fib_i   = 0
  fib_ip1 = 1
  
  while fib_ip1 <= n:
    
    fib_i, fib_ip1 = fib_ip1, fib_i + fib_ip1
  
  # {fib_i   <= n}
  # {fib_ip1 >  n}
  
  # fib_i is the last fibonacci
  # number to include in our sum.
  # 
  # The sum of the first i fibonacci
  # numbers (i.e. up to fib_i) is
  # fib_ip2 - 1
  
  fib_im1 = fib_ip1 - fib_i
  
  fib_ip2 = fib_i + fib_ip1
  
  return (fib_im1, fib_i, fib_ip2 - 1)


t = int(raw_input().strip())
for _ in xrange(t):
    n = int(raw_input().strip())
    
    print one_answer(n)