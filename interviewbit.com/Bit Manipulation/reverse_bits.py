# https://www.interviewbit.com/problems/reverse-bits/

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    
    # O( log(n) ) where n is the number of bits
    def reverse(self, A):
        A= ( (A & 0x55555555) << 1 ) | ( (A & 0xaaaaaaaa) >> 1 )
        A= ( (A & 0x33333333) << 2 ) | ( (A & 0xcccccccc) >> 2 )
        A= ( (A & 0x0f0f0f0f) << 4 ) | ( (A & 0xf0f0f0f0) >> 4 )
        A= ( (A & 0x00ff00ff) << 8 ) | ( (A & 0xff00ff00) >> 8 )
        A= ( (A & 0x0000ffff) <<16 ) | ( (A & 0xffff0000) >>16 )
        return A
    
    # O( the position of the most significant set bit )
    def my_reverse(self, A):
        
        res= 0
        i= 32
        while A != 0:
            res= res << 1
            res+= A & 1
            A= A >> 1
            i-= 1
        return res << i