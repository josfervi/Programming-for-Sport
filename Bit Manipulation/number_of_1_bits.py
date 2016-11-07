# https://www.interviewbit.com/problems/number-of-1-bits/

class Solution:
    # @param A : integer
    # @return an integer
    
    # O(result)
    def numSetBits(self, A):
        
        num= 0
        while A != 0:
            A= A & (A-1)
            num+= 1
        
        return num
    
    # O( the position of the most significant set bit )
    def my_numSetBits(self, A):
        
        num= 0
        while A != 0:
            num+= A & 1
            A= A >> 1
        
        return num