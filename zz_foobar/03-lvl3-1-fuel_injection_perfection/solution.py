# Submission: SUCCESSFUL. Completed in: 1 day, 5 hrs, 58 mins, 37 secs.

# INDEX
# 
# THE IDEA BEHIND MY STRATEGY
#   [1] when num == 2k     for some int k > 0, always div
#   [2] when num == 4k + 1 for some int k > 0, always -1
#   [3] when num == 4k - 1 for some int k > 1, always +1
#       - special case, num == 4k - 1 and k == 1 and num == 3
#
# TIME COMPLEXITY is O(lg(n))
#
# SOLUTION
# - class NumStr(str)
#   - def toBinary(self)
#   - def modBy2(self)
#   - def divModBy(self, divisor)
# - def removeLeadingZeros(digits)
# 
# - def answer(n)
# - def add1(bits)
# 
# TESTING
# - TESTING answer(n)
#   - def test_answer()
#   - def printFailStr(num, expected_result, actual_result)
# 
# - TESTING divModBy(self, divisor)
#   - def test_divModBy(number_of_tests)
#   - def run_random_tests_for_divModBy(number_of_tests)
#   - def test_divModBy_once()
#   - def getFailStr(dividend, divisor, expected_result, actual_result)

# IDEA BEHIND MY STRATEGY ------------------------------------------------------
# This section states the strategy used in the solution and
# I also convince you why the strategy is correct.

# shorthand:
#  '-1'  or  '/'   means perform a minus 1     operation
# 'div'  or  '|'   means perform a divide by 2 operation
#  '+1'  or  '\'   means perform a plus 1      operation

# [1] when num == 2k for some int k > 0
#     it is always best to div
# 
# num
# of
# ops
#
# 0             2*k
#              / | \
# 1        2k-1  k  2k+1
#         /     / \     \
# 2   2k-2   k-1   k+1   2k+2
#       |                  |
# 3    k-1                k+1
#         \              /
# 4        k            k
#
# Fig 1. Exploring operations that can be done when you start with num of the form 2k, k>0 
# 
# The thing to note about the diagram in figure 1 is that
# 
#  - by  -1'ing  you can get from 2k to (k-1, k, k+1) in (3, 4, 5) operations respectively
#  - by div'ing  you can get from 2k to (k-1, k, k+1) in (2, 1, 2) operations respectively
#  - by  +1'ing  you can get from 2k to (k-1, k, k+1) in (5, 4, 3) operations respectively
# 
# From this analysis it is easy to see that you are always best off div'ing when num is of the form 2k, k>0


# [2] when num == 4k + 1 for some int k > 0
#     it is always best to -1
# 
# num
# of
# ops
#
# 0             4k+1
#              /    \
# 1          4k      4k+2
#             |        |
# 2          2k      2k+1
#             |     /    \
# 3           k   2k      2k+2
#                  |        |
# 4                k       k+1
#
# Fig 2. Exploring operations that can be done when you start with num of the form 4k+1, k>0
#        Using our knowledge from [1] when a node is even we just div
# 
# The thing to note about the diagram in figure 2 is that
# 
#  - by  -1'ing  you can get from 4k+1 to (k-1, k, k+1) in (4, 3, 4) operations respectively
#  - you can't div from the onset, because 4k+1 is odd
#  - by  +1'ing  you can get from 4k+1 to (k-1, k, k+1) in (5, 4, 4) operations respectively
# 
# From this analysis it is easy to see that you are always best off -1'ing when num is of the form 4k+1, k>0


# [3] when num == 4k - 1 for some int k > 1
#     it is always best +1
# 
# num
# of
# ops
#
# 0             4k-1
#              /    \
# 1        4k-2      4k
#            |        |
# 2        2k-1      2k
#         /    \      |
# 3   2k-2      2k    k
#       |        |
# 4    k-1       k      
#
# Fig 3. Exploring operations that can be done when you start with num of the form 4k-1, k>1
#        Using our knowledge from [1] when a node is even we just div
# 
# The thing to note about the diagram in figure 3 is that
# 
#  - by  -1'ing  you can get from 4k-1 to (k-1, k, k+1) in (4, 4, 5) operations respectively
#  - you can't div from the onset, because 4k-1 is odd
#  - by  +1'ing  you can get from 4k-1 to (k-1, k, k+1) in (4, 3, 4) operations respectively
# 
# From this analysis it is easy to see that you are always best off +1'ing when num is of the form 4k-1, k>1


# Those of you with an eye for detail will have noticed that for
# [1] and [2], we allowed k to equal 1, while for [3], we did not.
# 
# The reason for this restriction on k for [3] becomes clear if we plug in k == 1 into figure 3.
# 
# num
# of
# ops
#
# 0              3
#              /  \
# 1           2    4
#             |    |
# 2    2k-1 = 1    2
#            / \   |
# 3         0   2  1 = k
#           |   |
# 4    k-1= 0   1 = k
#
# Fig 4. Special case of the diagram of figure 3, where k == 1
#        Using our knowledge from [1] when a node is even we just div
# 
# The analysis of [3] (stated in lines 116 - 118) is still correct;
# the salient point is that when k == 1, 2k-1 == 1 and 1 is our objective!
# So in this one special case, it is best to -1 then div.

# TIME COMPLEXITY --------------------------------------------------------------
#
#  It takes O(lg(n)) time to convert n to its binary representation.
#
#  Once we have the binary represenation, it is time to get rid of all but one bit.
# 
#  From the analysis stated in IDEA BEHIND MY STRATEGY, we can see that it is always
#  possible to reduce the number of bits of n by 2 in at most 3 operations.
#  
#  Noting that there are lg(n) bits in the binary representation of n, we can say
#  it takes O(3/2 * number_of_bits_of_n) = O(lg(n)) to get rid of all but one bit.
#
#  Therefore we have an O(lg(n)) + O(lg(n)) = O(lg(n)) time algorithm

# SOLUTION ---------------------------------------------------------------------

class NumStr(str):
    
    # O(lg(num) * lg(num)) time
    # = O(lg(num))
    # 
    # self :: decimal representation
    #         of num, a positive integer
    def toBinary(self):
        ''' Returns bits, a list of 0's and 1's,
            where bits[i] is the ith bit of the binary
            representation of num '''
        
        # I think we can convert to any base, b,
        # by replacing the 2 with b,
        # but I'd have to think about it a little bit more. 
        
        n = self
        
        bits = []
        
        while not (n == '' or n == '0'):                                          # lg2(num) iterations
            n_divBy_2, n_modBy_2 = n.divModBy(2) # n/2 as a NumStr, n%2 as an int # O(lg10(n))
            bit = n_modBy_2
            bits.append(bit)
            
            n = n_divBy_2
            
        return bits
    
    # self :: decimal representation
    #         of num, a positive integer
    def modBy2(self):
        ''' Returns num % 2 as an int '''
        
        lsd = int( self[-1] ) # least significant digit
                              # of the decimal represenation of num
        return lsd % 2
    
    # self :: decimal representation
    #         of num, a positive integer
    def divModBy(self, divisor):
        ''' Returns (num / divisor, num % divisor) as (NumStr, int) tuple '''
        
        BASE = 10
        
        _div = [None] * len(self)
        
        c_out = 0 # carry_out
        
        for i, digit in enumerate(self):              # lg10 num iterations
            
            c_in = c_out # carry_in
            current_dividend = BASE*c_in + int(digit)
            
            _div[i] = str(current_dividend / divisor)
            c_out   =     current_dividend % divisor
        
        # remove leading zeros from _div, but if _div was all '0's don't remove the last '0', accomplished by i < len(_div)-1
        _div = removeLeadingZeros(_div)
        
        div = NumStr(''.join(_div))
        mod = c_out
        
              # num/divisor, num%divisor
        return (  div,         mod      )

# digits :: a list of strings or ints
def removeLeadingZeros(digits):
    
    i = 0
    while i < len(digits)-1 and int(digits[i]) == 0:
        i += 1
    
    # { digits[:i] == ['0']*i } <- the leading zeros
    
    return digits[i:]



# n :: decimal string representation
#      of a positive integer, num
#      of at most 309 digits
def answer(n):
    
    # num can be very large so leave it as
    # and process it as a string, a NumStr
    n = NumStr(n)
    
    # this is a binary-math problem at heart,
    # so change num's representation to binary
    bits = n.toBinary() # lists of 0's and 1's where bits[i] is the ith bit of num
    
    number_of_operations = 0
    
    FIRST, SECOND = 0, 1
    
    while not (bits == [1] or bits == [1, 1]):
        
        lsb  = bits[FIRST] # least-significant bit
        
        number_of_operations += 1
        
        if lsb == 0:
            # { bits.repr == 1...0 }
            #
            # perform divide by 2 operation
            
            bits = bits[1:] # this can conceivably be done in O(1) time by pointing the pointer to the bits[1] instead of bits[0]
                            # if it turns out it is not actually done in O(1), I could work with the reversed list or use a collections.deque
            
            # { bits.repr == 1... }
            continue
        
        # { lsb == 1 }
        
        slsb = bits[SECOND] # second-least-significant bit
        
        if slsb == 0:
            # { bits.repr == 1...01 }
            #
            # perform a minus 1 operation
            
            bits[FIRST] = 0
            
            # { bits.repr == 1...00 }
            #
            # note: in the next two iterations, you will do two divide by 2 operations
        
        else: # slsb == 1
            # { bits.repr == 1...11 }
            #
            # perform a plus 1 operation
            
            bits[FIRST]  = 0
            bits[SECOND] = 0
            bits[2:]     = add1(bits[2:])
            
            #                   1...00
            #    1...11             11         1...00
            #    +    1  ==          1  ==        100
            # ---------      ---------      ---------
            # bits.repr      bits.repr      bits.repr
            #
            # note: in the next two iterations, you will do two divide by 2 operations
    
    # { bits.repr == 1 or bits.repr == 11 }
    
    if bits == [1, 1]:
        
        # This is the one exception to the rule:
        # Normally, when lsb == 1 and slsb == 1,
        # you would perfom a plus 1 operation.
        # If you do that here,
        # you'd need 3 operations overall
        # to get from 11 (in binary) to 1;
        # however, this can be done in jut 2 opeations by
        #    performing a minus 1 operation and then
        #    performing a divide by 2 operation
        
        number_of_operations += 2
    
    # else: bits == [1]: do nothing
    
    return number_of_operations


# in-place
# bits :: a list of 0's and 1's
#         where bits[i] is the ith bit
def add1(bits):
    
    i = 0
    while i < len(bits) and bits[i] == 1:
        bits[i] = 0
        i+= 1
    
    if i == len(bits):
        bits.append(1)
        return bits
    
    # { bits[i] == 0 }
    
    bits[i] = 1
    return bits

# TESTING ----------------------------------------------------------------------
# to run tests
# uncomment everything below this line exactly one time and run: python solution.py


# # TESTING answer(n) ------------------------------------------------------------

# def test_answer():
    
#     # expected_results[0] == None because answer(0) is undefined
#     expected_results= [None, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, \
#                           4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 7, 6, 7, 6, 6, \
#                           5, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 8, 7, 8, 7, 7, \
#                           6, 7]
    
#     number_of_defined_expected_results = len(expected_results)
    
#     failed_tests = []
    
#     uptothisNum = 50 # expected_results[i] is defined for all i up to 49,
#                      # expected_results[i] must be defined for all i up to uptothisNum-1
    
#     for num in range(1, uptothisNum):
        
#         n = str(num)
        
#         actual_result   = answer(n)
#         expected_result = expected_results[num] if num < number_of_defined_expected_results else None # None indicates that the expected result is unknown
        
#         test_passed = actual_result == expected_result
        
#         if not test_passed:
            
#             failed_tests.append(num)
            
#             printFailStr(num, expected_result, actual_result)
    
#     number_of_failed_tests = len(failed_tests)
    
#     if number_of_failed_tests == 0:
#         print "Passed all {0} tests.".format(uptothisNum)
#     else:
#         print "Failed {0}/{1} tests.".format(number_of_failed_tests, uptothisNum)
#         print "{0}/{1} failed because the expected result is unknown".format(uptothisNum - number_of_defined_expected_results, number_of_failed_tests)

# def printFailStr(num, expected_result, actual_result):
    
#     print "Failed test for answer({0})".format(num)
#     print "  expected: {0}".format(expected_result)
#     print "  got     : {1}".format(actual_result)
#     print


# # TESTING divModBy(self, divisor) ----------------------------------------------

# def test_divModBy(number_of_tests):
    
#     print NumStr(1000).divModBy(100) == ('10', 0)    # w/o removing leading zeros,  prints ('0010', 0)
#                                                      # w/  removing leading zeros*, prints (  '10', 0)
    
#     print NumStr(1000).divModBy(1001) == ('0', 1000) # w/o removing leading zeros,  prints ('0000', 1000)
#                                                      # w/  removing leading zeros*, prints (   '0', 1000)
                                      
#                                                      # * := does not however remove the last element even if it would
#                                                      #      otherwise be considered part of the set of leading zeros
#                                                      #      because doing so would leave us with an empty string instea of '0'
    
#     run_random_tests_for_divModBy(number_of_tests)

# def run_random_tests_for_divModBy(number_of_tests):
    
#     number_of_failed_tests = 0
    
#     for i in range(number_of_tests):
        
#         test_passed, failStr = test_divModBy_once()
        
#         if not test_passed:
#             number_of_failed_tests += 1
#             print failStr
    
#     if number_of_failed_tests == 0:
#         print "Passed all {0} random test cases! :)".format(number_of_tests)
#     else:
#         print "Failed {0}/{1} random test cases. :(".format(number_of_tests, number_of_failed_tests)

# from random import randint

# def test_divModBy_once():
    
#     dividend = randint(0, 10**9)
#     divisor  = randint(1, 2*dividend)
    
#     expected_result = ( dividend / divisor, dividend % divisor )
    
#     act_div, act_mod = actual_result = NumStr(dividend).divModBy(divisor) # no need to str(.) in NumStr(str(dividend))
#     actual_result    = (int(act_div), act_mod)
    
#     test_passed = expected_result == actual_result
#     failStr     = None if test_passed else getFailStr(dividend, divisor, expected_result, actual_result)
    
#     return (test_passed, failStr)

# def getFailStr(dividend, divisor, expected_result, actual_result):
    
#     exp_div, exp_mod = expected_result
#     act_div, act_mod = actual_result
    
#     failStr = \
#     "Failed for {0}/{1}\n".format(dividend, divisor)      + \
#     "\t     expected \t\t got\n"                          + \
#     "\tDIV: {0}      \t\t {1}\n".format(exp_div, act_div) + \
#     "\tMOD: {0}      \t\t {1}\n".format(exp_mod, act_mod)
    
#     return failStr


# if __name__ == "__main__":
    
#     test_answer()
    
#     number_of_tests = 10**6
#     test_divModBy(number_of_tests)