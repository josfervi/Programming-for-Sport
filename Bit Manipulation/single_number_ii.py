# https://www.interviewbit.com/problems/single-number-ii/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        
        ones, twos, threes= 0, 0, 0
        
        # for a in A:
        #     twos|=   ones & a
        #     ones^=   a
        #     threes=  ones & twos # alternative
        #     ones&=   ~threes
        #     twos&=   ~threes
        
        for a in A:
            threes=  twos & a # alternative
            twos|=   ones & a
            ones^=   a
            ones&=   ~threes
            twos&=   ~threes
        
        return ones