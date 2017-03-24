#!/bin/python

import sys

def biggest_prime_factor_of( num):
  return biggest_prime_factor_of_iterative( num)


# Iterative solution, adapted from the
#   tail recursive solution. Not as
#   easy to understand, but a bit more
#   time efficient.
# O(1) space.
def biggest_prime_factor_of_iterative( num):
  
  if num < 0:
    return biggest_prime_factor_of_(-1*num)
  
  if num <= 3:
    return num
    
  divisor = 2
  while divisor <= 3:
    if num % divisor == 0:
      num /= divisor
      if num == 1:
        return divisor
    else:
      divisor += 1
  
  # Picture num as it's prime factorization,
  #   or, more specifically, as an ordered list of
  #   (non-decreasing) prime numbers (with duplicity if necessary)
  #   whose product is num.
  # This loop removes primes from that list one by one and in order.
  # Each time a prime is removed, num becomes the product of the remaining primes.
  # Finally when only one prime remains, which is necessarily the biggest prime
  #   factor of the original value of num, we return it.
  divisor = 5
  add2 = True
  while divisor <= int(num ** 0.5):
    
    if num % divisor == 0:
      num /= divisor
    else:
      if add2:
        divisor += 2
      else:
        divisor += 4
      add2 = not add2
    
  # num is prime
  return num


# Tail recursive solution, easier to understand
#   than the iterative solution, but
#   also a bit less efficient.
# O(num_prime_factors_of( num)) space (on the call stack)
def biggest_prime_factor_of_tailRecursive( num):
  
  if num < 0:
    return biggest_prime_factor_of_(-1*num)
  
  if num <= 3:
    return num
  
  for divisor in range(2,3+1):
    if num % divisor == 0:
      return biggest_prime_factor_of( num/divisor)
  
  # A common trick is to check for
  # divisibility against only odd divisors,
  # skipping even diviosrs. In addition,
  # to skipping over divisors that are
  # divisible by 2, I also skip over
  # divisors that are divisible by 3.
  
  # Starting at 5
  #   divisor will take on
  #   all values that are
  #   not divisible by 2 nor 3.
  divisor = 5
  add2 = True
  s = int(num ** 0.5)
  while divisor <= s:
    
    if num % divisor == 0:
      return biggest_prime_factor_of( num/divisor)
    
    if add2:
      divisor += 2
    else:
      divisor += 4
    add2 = not add2
  
  # num is prime
  return num


t = int(raw_input().strip())
for _ in xrange(t):
    n = long(raw_input().strip())
    
    print biggest_prime_factor_of( n)