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
# if space were an issue, we could trade some we can use the generator descFactors_gen(N)
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

# tests


print answer("abccbaabccba") == 2
print answer("abcabcabcabc") == 4

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
print answer(s) == len(s)

s = "yyyyyyyyyyyyyyyyyya"
print answer(s) == 1

# Some random testing to increase our confidence

from random import randint

def test_answer_once():
  
  # first generate the basic substring, sub
  
  l = randint(1,20) # length of basic substring
  sub = []
  
  # note that ASCII codes 33 thru 126 correspond to printable symbols,
  # and that code remains within 33..126 in the for loop
  #
  # make sure that sub itself cannot be cut into smaller identical subsubstrings
  # by having the sequence of chars in sub be a monotonically increasing sequence
  code = 33
  for i in range(l):
    step = randint(1,4)
    code += step
    sub.append(chr(code))
  sub = ''.join(sub)
  
  # now construct the input s by replicating sub m times
  m = randint(1,25)
  s = sub * m
  
  # print answer(s) == m
  return True

NUMBER_OF_TEST_CASES = 100

number_of_failed_test_cases = 0

for i in range(NUMBER_OF_TEST_CASES):
  test_passed = test_answer_once()
  if not test_passed:
    number_of_failed_test_cases += 1

if number_of_failed_test_cases == 0:
  print "Passed all random test cases! :)"
else:
  print "Failed {0} random test cases. :(".format(number_of_failed_test_cases)