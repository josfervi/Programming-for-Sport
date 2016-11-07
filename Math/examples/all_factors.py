from math import ceil

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        
        if A == 1: return [1]
        
        fwd_factors= [1]
        bwd_factors= [A]
                           #  A | sqrt_ 
        sqrt_= int(A**0.5) # 24 |   4
                           # 25 |   5
                           # 26 |   5
        
        
        
        for a in xrange(2, sqrt_ +1): 
            
            if A % a == 0:
                fwd_factors.append(a)
                bwd_factors.append(A / a)
        
        if fwd_factors[-1] == bwd_factors[-1]:
            # A is a perfect square
            return fwd_factors + list( reversed( bwd_factors[:-1] ) )
        
        # A is not a perfect square
        return fwd_factors + list( reversed( bwd_factors) )