# https://www.interviewbit.com/problems/single-number/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    # O( n ) time complexity
    # O( 1 ) extra space complexity
    def singleNumber(self, A):
        
        res= 0
        for a in A:
            res^= a
        return res