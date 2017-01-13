# https://www.interviewbit.com/problems/sorted-insert-position/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if B is []:   return 0
        if B < A[0]:  return 0
        if B > A[-1]: return len(A)
        
        l= 0
        r= len(A) -1
        
        mid= (l+r)/2
        # INVARIANT:
        # A[:l]   < B
        # A[r+1:] > B
        while l<=r:
            current= A[mid]
            if B < current:
                r= mid-1
            elif B == current:
                return mid
            else: # B > current
                l= mid+1
            mid= (l+r)/2
        assert l == r + 1
        # A[:l] < B
        # A[r+1:] = A[l:] > B
        #
        #         l 
        #         |
        #  _______v________
        # [  <B  |   >B    ]
        #  ----------------
        return l