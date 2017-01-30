# INDEX
#  
#  FUNCTIONS
#  - def answer(s)
#  - def getFactors(N)
#  - def descFactors_gen{N}
#  - def possible(s, m)
#  
#  ASIDE - unexplored idea - conjecture
#  
#  TESTING
#  - directed
#  - random


# N := len(s)
# F := number of factors of N
#
# O(F * N) time,
#                O(F) space if we use getFactors(N)
#                O(1) space if we use descFactors_gen(N)
#                           but we'd be sacrificing some constant time
'''PRECONDITION: 1 <= N < 200'''
def answer(s):
  
  N = len(s)
  
  # check PRECONDITION, just check the problematic part though, i.e. when N = 0
  if N == 0:
    return 0
  
  # notice that the answer must be a factor of N = len(s),
  # otherwise, we'd have leftovers
  
  # since we want the max,
  # we check candidates in descending order,
  # and return the first candidate that works
  # for factor in reversed(getFactors(N)):
  for factor in descFactors_gen(N): # O(F) iterations
    
    if possible(s, factor): # O(N)
      return factor

# F := number of factors of N
# 
# O(N) time, O(F) space for the result
#
# if space were an issue, we could sacrifice some constant time (of function calls) for using less space,
# by using the generator descFactors_gen(N)
def getFactors(N):
  
  factors = [1] # "optimization", can be incoorporated into for loop
  for candidate in range(2, N):
    if N % candidate == 0:
      factor = candidate
      factors.append(factor)
  factors.append(N)
  return factors

# O(N) time, O(1) space
def descFactors_gen(N):
  
  yield N
  for candidate in reversed(range(2, N)): # like '(N-1).downto 2' in ruby
    if N % candidate == 0:
      factor = candidate
      yield factor
  yield 1

# N := len(s)
#
# O(N) time, O(1) space
'''Returns true if it is possible
   to cut string s into m idential substrings.
   Otherwise, returns false.
   PRECONDITION: len(s) % m == 0'''
def possible(s, m):
  
  N = len(s)
  
  # check PRECONDITION just to be safe
  if not N % m == 0:
    return False
  
  l = N/m # substring length
  ref_substring = s[:l]
  
  for i in range(m): # O(m) iterations
    
    current_substring = s[i*l : (i+1)*l]
    
    if current_substring != ref_substring: # O(l)
      return False
  
  return True


# ASIDE - unexplored idea
# 
# 1. Find the prime factorization of N = len(s).
# 2. Say the prime factorization of N is p_0^a_0 * p_1^a_1 * p_2^a_2 ...
#    where p_0,p_1,p_2,... are prime and a_0,a_1,a_2,... are integers >= 1.
# 
#    I have an unproven conjecture that:
#    if
#      string s can be broken into p' identical substrings, where p' is one of p_0,p_1,p_2,... and
#      string s can be broken into q' identical substrings, where q' != p' is another of p_0,p_1,p_2,...
#    then
#      string s can be broken into p'*q' identical substrings.
# 
#    A stronger version of this conjecture says that:
#    if
#      string s can be broken into p_i^a_i' identical substrings, where p_i is one of p_0, p_1, p_2,... and a_i' satisfies 1 <= a_i' <= a_i and
#      string s can be broken into p_j^a_j' identical substrings, where p_j != p_i is another of p_0, p_1, p_2,... and a_j' satisfies 1 <= a_j' <= a_j
#    then
#      string s can be broken into p_i^a_i' * p_j^a_j' identical substrings.
# 
# If both of these conjectures were true, we could use them to come up with a
# O(K * N) time algorithm instead of our current O(F * N) time algorithm given that we can get the prime factorization of N in O(K * N) or less.
#   where K = a_0 + a_1 + a_2 + ... = the sum of the duplicities of the prime factors of N
#   Recall that F is the number of factors of N.
#   It can be shown that F = (a_0 + 1) * (a_1 + 1) * (a_2 + 1) * ...
#   Note that K < F.


# TESTING - tests are only ran if __name__ == "__main__" (see ln 145-146)
# to run tests, uncomment everything below this line once and make sure you can import random

# def run_tests():
  
#   print answer("abccbaabccba") == 2
#   print answer("abcabcabcabc") == 4
  
#   s = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
#   print answer(s) == len(s)
  
#   s = "yyyyyyyyyyyyyyyyyya"
#   print answer(s) == 1
  
#   run_random_tests()

# # Some RANDOM TESTING to increase our confidence

# def run_random_tests():
  
#   NUMBER_OF_TEST_CASES = 100
  
#   number_of_failed_test_cases = 0
  
#   for i in range(NUMBER_OF_TEST_CASES):
#     test_passed = test_answer_once()
#     if not test_passed:
#       number_of_failed_test_cases += 1
  
#   if number_of_failed_test_cases == 0:
#     print "Passed all random test cases! :)"
#   else:
#     print "Failed {0} random test cases. :(".format(number_of_failed_test_cases)

# from random import randint

# def test_answer_once():
  
#   # first generate the basic substring, sub
  
#   l = randint(1,20) # length of basic substring
#   sub = []
  
#   # note that ASCII codes 33 thru 126 correspond to printable symbols,
#   # and that code remains within 33..126 in the for loop
#   #
#   # make sure that sub itself cannot be cut into smaller identical subsubstrings
#   # by having the sequence of chars in sub be a monotonically increasing sequence
#   code = 33
#   for i in range(l):
#     step = randint(1,4)
#     code += step
#     sub.append(chr(code))
#   sub = ''.join(sub)
  
#   # now construct the input s by replicating sub m times
#   m = randint(1,25)
#   s = sub * m
  
#   # print answer(s) == m
#   return True

# if __name__ == "__main__":
#   run_tests()