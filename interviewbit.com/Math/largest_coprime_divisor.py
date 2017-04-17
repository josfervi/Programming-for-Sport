from fractions import gcd

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        
        while gcd(A,B) != 1:
            A/= gcd(A,B)
            
        return A
        
        #gcd_= gcd(A,B)
        #while gcd_ != 1:
        #    A/= gcd_
        #    gcd_= gcd(A,B)
        #
        #return A    