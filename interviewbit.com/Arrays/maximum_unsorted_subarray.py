# https://www.interviewbit.com/problems/maximum-unsorted-subarray/
# misnomer: should be minimum_unsorted_subarray

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        
        n= len(A)
        
        max_= [None]*n # max[i] will contain max( A[:i+1] )
        min_= [None]*n # min[i] will contain min( A[i:] )
        
        max_[0]= A[0]
        for i in xrange(1, n):
            max_[i]= max(max_[i-1], A[i])
        
        min_[n -1]= A[n -1]
        for i in xrange(n -1 -1, 0 -1, -1):
            min_[i]= min(A[i], min_[i+1])
        
        l= 0
        while l+1<n and max_[l] <= min_[l+1]:
            l+= 1
        
        if l == n-1:
            return [-1]
        
        r= n-2
        while r>=0 and max_[r] <= min_[r+1]:
            r-= 1
        
        return [l,r+1]