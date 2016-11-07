my solution is hinged on the following observation:

# A != 1 can be written as B^P where B>1, P>1 are ints

# if there exists int b in [2...int(sqrt(A))] inclusive
# s.t. log_b_A is a whole number

# actually, we can forgo checking all b in [2...int(sqrt(A))] and only check those b that themselves can't be written as a base>1 to a power>1
# to see why, take b= c**d, c>1, d>1, if A can be written as b**p, then it can also be written as c**(d*p).
# Checking such b's that can be written as b=c**d, c>1, d>1 is wasteful and should be avoided if possible.

# <=>

# if there exists prime p in [2...int(log_2_A)] inclusive
# s.t. A**(1/p) is a whole number

# if you don't have a list of primes lying around, you can just check for all integer p in [2...int(log_2_A)]

from math import sqrt, log

class Solution:
    # @param A : integer
    # @return a boolean
    
    # if A is 1, then it can be written as 1^P for any P>=0
    
    # A != 1 can be written as B^P where B>1, P>1 are ints
    
    # if there exists int b in [2...int(sqrt(A))] inclusive
    #  s.t. log_b_A is a whole number
    
    # <=>
    
    # if there exists prime p in [2...int(log_2_A)] inclusive
    #  s.t. A**(1/p) is a whole number
    
    def isPower(self, A):
        
        if A == 1:
            return True
        
        for b in xrange( 2, int(sqrt(A)) +1):
            
            # is_integer() fails when A = 536870912, b = 2
            # if log( A, b).is_integer(): 
                # return True
            
            c= log(A, b)
            if b**int(c) == A:
                return True
        
        return False