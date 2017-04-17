# https://www.interviewbit.com/problems/different-bits-sum-pairwise/

class Solution:
    # @param A : list of integers
    # @return an integer
    
    # O( n * l ) where n = len(A), l = bitlength A[0] (assume all elements of A have the same bitlength, namely l)
    def cntBits(self, A):
        
        n= len(A)
        res= 0
        for i in xrange(0, 32):
            num_ones= 0
            for a in A:
                num_ones+= (a >> i) & 1
            # num_ones = the number of ones at bit position i
            res+= num_ones*(n-num_ones) # num_ones * num_zeros
        
        return (res << 1) % (10**9 + 7)
    
    # times out, not efficient enough
    # O( n**2 * l ) where n = len(A), l = bitlength of A[0] (assume bitlength of A[i] = l for all i in range(0,n) )
    def my_cntBits(self, A):
        
        res= 0
        for i in xrange(len(A)):
            for j in xrange(i +1, len(A)): # j > i,
                #                            avoid j == i, f(A[i], A[j]) == 0
                #                            avoid j <  i, since f(A[i], A[j]) == f(A[j], A[i]), only compute it once
                #                                          and then double res at the end to account for j < i contributions
                res+= self.numSetBits( A[i] ^ A[j] ) # f(a,b) = numSetBits(a^b)
                                                     # in a^b there's a 1 in each position where a and b differ
        
        #       res *  2
        return (res << 1) % (10**9 + 7)
    
    # from:
    #https://www.interviewbit.com/problems/number-of-1-bits/
    # O(result)
    def numSetBits(self, A):
        
        num= 0
        while A != 0:
            A= A & (A-1)
            num+= 1
        
        return num