# I'm not sure what is meant by extra space...

# but I took it to mean, use as little memory as possible.

# I solve the problem whilst using as few variables as possible, just one variable,

# and

# having that one variable grow no larger than int(log10(A) + 1) / 2

# I must note, that using as little memory as possible, means being very inefficient
# with computations, often recomputing the same value twice. This is because computations
# cannot be saved onto a variable.

from math import log10

class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return False
        
        if A < 10:
            return True
                       # ---len(str(A))---       
        for i in xrange( int(log10(A) + 1) / 2 ):
            
               # -----ith digit------    ---------------- -(1+i)th digit ----------------
            if ( ( (A / 10**i) % 10 ) != ( ( A / 10**( int(log10(A) + 1) -1 -i ) ) % 10 ) ):
                return False
        
        # { ith digit == -(1+i)th digit for all i in [0, n/2] inclusive }
        # therefore A is a palindrome
        
        return True